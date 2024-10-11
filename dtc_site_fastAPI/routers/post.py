from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from typing import Annotated

from db import get_db
from models.user import User


router = APIRouter(prefix='', tags=['Post'])
templates = Jinja2Templates(directory='./templates')

fake_users_db = {
    'user1': 'pwd1'
}


@router.post("/login")
async def login(
        request: Request,
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)]
):
    if db.scalar(select(User).where(User.name == username, User.password == password)):
        request.session["user"] = username
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

    return templates.TemplateResponse('home.html', {
        'request': request,
        'user': request.session.get('user', None),
    })
