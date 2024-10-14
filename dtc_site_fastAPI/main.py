from fastapi import FastAPI
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

from routers.get import router as get_router
from routers.post import router as post_router

app = FastAPI()
app.include_router(get_router)
app.include_router(post_router)
key_ = 'pqeWGIs5A8vao8XFLHfmTfZb0g3vjmLv'
app.add_middleware(SessionMiddleware, secret_key=key_)


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8001, reload=True)