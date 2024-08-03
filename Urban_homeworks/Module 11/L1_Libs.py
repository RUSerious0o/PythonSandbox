import json
from numpy import array
import pandas
from random import randint


def generate_data():
    _TABLE_HEIGHT = 6
    _TABLE_WIDTH = 12
    data = array([randint(5000, 15000) for _ in range(_TABLE_WIDTH * _TABLE_HEIGHT)]).reshape(_TABLE_HEIGHT, _TABLE_WIDTH)
    with open('data.txt', 'w', encoding='utf-8') as file:
        json.dump(data.tolist(), file)


def numpy_test():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = array(json.load(file))
    #
    #
    print(data, data.__class__, sep='\n')
    print(data.dtype.name, data.shape, data.ndim)
    print(data.cumsum(0), f'\n sum = {data.sum()}, min = {data.min()}, max = {data.max()}, mean = {data.mean():.2f}'
                          f', std = {data.std():.2f}')


def pandas_test():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = array(json.load(file))

    frame_ = pandas.DataFrame(data,
                              index=pandas.date_range('20240701', periods=data.shape[0]),
                              columns=[i + 8 for i in range(data.shape[1])])
    print(frame_)
    print(frame_.describe())
    slice_ = pandas.DataFrame(frame_.iloc[0:4, 4:11])
    print(slice_.sort_index(axis=1, ascending=False))
    print(slice_[slice_ > 10000])
    print(slice_.cumsum(axis=1))
    print(slice_.sum().sum())


if __name__ == '__main__':
    # generate_data()
    numpy_test()
    pandas_test()
