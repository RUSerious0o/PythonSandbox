from fastapi import FastAPI, Path
from typing import Annotated

import uvicorn

app = FastAPI()

users = {
    '1': 'Имя: Example, возраст: 18',
    '2': 'Имя: Test, возраст: 65',
}

annotations = {
    'user_id': Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
    'user_name': Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
    'user_age': Annotated[int, Path(ge=18, le=120, description='Enter age')]
}

@app.get('/')
async def get_main_page() -> str:
    return 'Главная страница.'


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: annotations['user_name'],
                        age: annotations['user_age']) -> str:
    try:
        user_id = int(max(users, key=int)) + 1
    except:
        user_id = 1

    users.update({str(user_id): f'Имя: {username}, возраст: {age}'})
    return f"User {user_id} is registered"


# почему-то ругается на int-овую аннотацию user_id
@app.put('/user/{user_id}/{user_name}/{user_age}')
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter ID')],
# async def update_user(user_id: annotations['user_id'],
                      user_name: annotations['user_name'],
                      user_age: annotations['user_age']) -> str:
    try:
        if 1 <= int(user_id) <= 100:
            pass
        else:
            raise Exception('Id must me in (1, 100)')
    except:
        raise Exception('Id must me in (1, 100)')

    if user_id in users:
        users[str(user_id)] = f'Имя: {user_name}, возраст: {user_age}'
        return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: annotations['user_id']) -> str:
    try:
        del users[str(user_id)]
    except:
        raise Exception(f'Deletion of user_id #{user_id} failed!')

    return f'The user #{user_id} has been deleted!'


if __name__ == '__main__':
    uvicorn.run(app, port=8000, log_level='info')