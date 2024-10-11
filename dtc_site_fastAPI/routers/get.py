from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from typing import Annotated

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
async def get_dashboard_page(request: Request):
    return templates.TemplateResponse('dashboard.html', {
        'request': request,
        'image_feeds': [],
        'user': request.session.get('user', None)
    })


@router.get('/add_image')
async def get_image_feed_page(request: Request):
    return templates.TemplateResponse('add_image_feed.html', {
        'request': request,
        'user': request.session.get('user', None)
    })
