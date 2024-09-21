from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Annotated


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()
users: list[User] = []
max_user_id: int = 0


annotations = {
    'user_id': Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
    'user_name': Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
    'user_age': Annotated[int, Path(ge=18, le=120, description='Enter age')]
}


@app.get('/users')
async def get_users() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: annotations['user_name'],
                      age: annotations['user_age']):
    global max_user_id
    max_user_id += 1

    new_user = User(id=max_user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: annotations['user_id'],
                      username: annotations['user_name'],
                      age: annotations['user_age']) -> User:
    try:
        user = next(filter(lambda user_: user_.id == user_id, users), None)
        user.username = username
        user.age = age
        return user
    except:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: annotations['user_id']) -> User:
    try:
        user = next(filter(lambda user_: user_.id == user_id, users), None)
        users.remove(user)
        return user
    except:
        raise HTTPException(status_code=404, detail="User was not found")


if __name__ == '__main__':
    uvicorn.run("L1_FastAPI:app", port=8000, reload=True, log_level='info')
