import os

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Annotated

from db import get_db
from models import ImageFeed
from routers.post import UPLOAD_DIRECTORY, PROCESSED_IMG_DIR
from utils import process_image as utils_process_image

router = APIRouter(prefix='', tags=['Get'])
templates = Jinja2Templates(directory='./templates')


@router.get('/')
@router.get('/home')
async def get_welcome_page(request: Request):
    return templates.TemplateResponse('home.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


@router.get('/login')
async def get_login_page(request: Request):
    return templates.TemplateResponse('login.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


@router.get('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse('/home')


@router.get('/register')
async def get_register_page(request: Request):
    return templates.TemplateResponse('register.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


@router.get('/dashboard')
async def get_dashboard_page(
        request: Request,
        db: Annotated[Session, Depends(get_db)]
):
    user_id = request.session.get('user_id', None)
    return templates.TemplateResponse('dashboard.html', {
        'request': request,
        'image_feeds': db.scalars(select(ImageFeed).where(ImageFeed.user_id == user_id)),
        'user': request.session.get('user', None)
    })


@router.get('/add_image')
async def get_image_feed_page(request: Request):
    if not request.session.get('user', None):
        return RedirectResponse('/login')

    return templates.TemplateResponse('add_image_feed.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


@router.get('/media/images/{image_name}')
async def get_image(image_name: str):
    return FileResponse(os.path.join(UPLOAD_DIRECTORY, image_name))


@router.get('/media/processed_images/{image_name}')
async def get_processed_image(image_name: str):
    return FileResponse(os.path.join(PROCESSED_IMG_DIR, image_name))


@router.get('/process_image/{image_id}')
async def process_image(
        request: Request,
        image_id: int,
        db: Annotated[Session, Depends(get_db)]
):

    image = db.scalar(select(ImageFeed).where(ImageFeed.id == image_id))
    if not image.processed_image:
        utils_process_image(image_id, image.image, PROCESSED_IMG_DIR, db)

    return RedirectResponse('/dashboard')
