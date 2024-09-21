from fastapi import FastAPI
import uvicorn

from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()
app.include_router(task_router)
app.include_router(user_router)

@app.get('/')
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8000, reload=True)
