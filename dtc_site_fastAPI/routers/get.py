import os.path

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Annotated

from starlette.responses import FileResponse

from db import get_db
from models import ImageFeed
from routers.post import UPLOAD_DIRECTORY

router = APIRouter(prefix='', tags=['Get'])
templates = Jinja2Templates(directory='./templates')


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
    return templates.TemplateResponse('home.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


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
    return templates.TemplateResponse('add_image_feed.html', {
        'request': request,
        'user': request.session.get('user', None)
    })


@router.get('/media/images/{image_name}')
async def get_image(image_name: str):
    return FileResponse(os.path.join(UPLOAD_DIRECTORY, image_name))
