import asyncio
from time import sleep

async def start_strongman(name: str, power: int | float):
    globes = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(globes):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1}-й шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Котик', 2)),
        asyncio.create_task(start_strongman('Аполлон', 6)),
        asyncio.create_task(start_strongman('Лев', 4)),
    ]

    for task in tasks:
        await task


asyncio.run(start_tournament())
