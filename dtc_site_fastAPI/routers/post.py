from fastapi import APIRouter, Request, Form, Depends, UploadFile, File, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from typing import Annotated
import shutil
import os
import random

from db import get_db
from models import User, ImageFeed, DetectedObject


router = APIRouter(prefix='', tags=['Post'])
templates = Jinja2Templates(directory='./templates')

UPLOAD_DIRECTORY = 'media/images'
PROCESSED_IMG_DIR = 'media/processed_images'
SUPPORTED_IMAGE_TYPES = ('.jpg', '.png', '.jpeg')
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
os.makedirs(PROCESSED_IMG_DIR, exist_ok=True)


@router.post("/login")
async def login(
        request: Request,
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)]
):
    if db.scalar(select(User).where(User.name == username, User.password == password)):
        request.session["user"] = username
        request.session['user_id'] = db.scalar(select(User.id).where(User.name == username))
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            'user': request.session.get('user', None)
        })
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            'user': request.session.get('user', None),
            'message': f'Wrong login or password!'
        })


async def check_login(login_: str):
    login_ = login_.lower()
    vocab = 'qwertyuiopasdfghjklzxcvbnm@.+-_'
    for letter in login_:
        if letter not in vocab:
            return False
    return True


@router.post('/register')
async def register(
        request: Request,
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        password_confirmation: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)]
):

    if not await check_login(username):
        return templates.TemplateResponse('register.html', {
            'request': request,
            'user': request.session.get('user', None),
            'message': 'Forbidden symbols in username!'
        })

    if password != password_confirmation:
        return templates.TemplateResponse('register.html', {
            'request': request,
            'user': request.session.get('user', None),
            'message': 'Entered passwords ane not equal!'
        })

    db.execute(insert(User).values(
        name=username,
        password=password,
    ))
    db.commit()
    request.session['user'] = username
    request.session['user_id'] = db.scalar(select(User.id).where(User.name == username))

    return templates.TemplateResponse('home.html', {
        'request': request,
        'user': request.session.get('user', None),
    })


async def generate_filepath(image: UploadFile):
    code_ = ''.join([random.choice("abcdefghijklmnopqrstuvw123456789" if i != 5 else "ABCDEFGHIJKLMNOPQRSTUVW123456798") for i in range(8)])
    filename = image.filename.split('.')
    filename = f'{filename[0]}_{code_}.{filename[1]}'
    return os.path.join(UPLOAD_DIRECTORY, filename)

@router.post('/upload_image')
async def upload_image(
        request: Request,
        db: Annotated[Session, Depends(get_db)],
        image: UploadFile = File()
):
    if not image.filename.endswith(SUPPORTED_IMAGE_TYPES):
        return templates.TemplateResponse('add_image_feed.html', {
            'request': request,
            'message': 'Incorrect image format!'
        })

    user_id = request.session.get('user_id', None)
    if not user_id:
        return templates.TemplateResponse('add_image_feed.html', {
            'request': request,
            'message': 'User ID undetected, please relogin!'
        })

    file_location = await generate_filepath(image)
    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)

    db.execute(insert(ImageFeed).values(
        image=file_location,
        user_id=request.session.get('user_id')
    ))
    db.commit()

    return templates.TemplateResponse('dashboard.html', {
        'request': request,
        'image_feeds': db.scalars(select(ImageFeed).where(ImageFeed.user_id == user_id)),
        'user': request.session.get('user', None)
    })


@router.post('/delete_image/{image_id}')
async def delete_image(image_id: int, db: Annotated[Session, Depends(get_db)]):
    image = db.query(ImageFeed).filter(ImageFeed.id == image_id).first()
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    db.delete(image)
    db.commit()
    os.remove(image.image)
    os.remove(image.processed_image)

    return RedirectResponse('/dashboard', status_code=status.HTTP_303_SEE_OTHER)
