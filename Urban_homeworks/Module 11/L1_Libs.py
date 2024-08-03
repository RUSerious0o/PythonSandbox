import json
from numpy import array
import pandas
from random import randint


def generate_data():
    _TABLE_HEIGHT = 30
    _TABLE_WIDTH = 8
    data = array([randint(5000, 15000) for _ in range(_TABLE_WIDTH * _TABLE_HEIGHT)]).reshape(_TABLE_HEIGHT, _TABLE_WIDTH)
    with open('data.txt', 'w', encoding='utf-8') as file:
        json.dump(data.tolist(), file)


# generate_data()
with open('data.txt', 'r', encoding='utf-8') as file:
    data = array(json.load(file))
#
#
print(data, data.__class__, sep='\n')
print(data.dtype.name, data.shape, data.ndim)
print(data.cumsum(0), f'\n sum = {data.sum()}, min = {data.min()}, max = {data.max()}, mean = {data.mean():.2f}'
                      f', std = {data.std():.2f}')

