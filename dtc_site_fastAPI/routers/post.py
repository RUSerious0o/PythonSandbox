from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from typing import Annotated


router = APIRouter(prefix='', tags=['Post'])
templates = Jinja2Templates(directory='./templates')

fake_users_db = {
    "user1": "password1",
    "user2": "password2"
}


@router.post("/login")
async def login(request: Request, username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username in fake_users_db and fake_users_db[username] == password:
        request.session["user"] = username
        print(username)
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            'user': request.session.get('user', None)
        })
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            'user': request.session.get('user', None)
        })
