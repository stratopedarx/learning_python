# coding: utf-8
"""
Алгоритм состоит из следующих шагов:

- найти наименьший элемент в массиве
- поменять местами его и первый элемент в массиве
- найти следующий наименьший элемент в массиве
- и поменять местами его и второй элемент массива
- продолжать это пока весь массив не будет отсортирован

Отсюда и название алгоритма – так как в нем наименьший элемент выбирается поочередно.
https://www.toptal.com/developers/sorting-algorithms/selection-sort
"""
from decorator_time import decorator_time


a = [0, 2, 3, -4, 6, 9, 7, 8]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]


@decorator_time
def selection(data):
    for i in xrange(len(data)):
        min_index = data.index(min(data[i:]))
        if min_index == i:
            # this element takes his correct position
            continue
        data[i], data[min_index] = data[min_index], data[i]

    return data


assert selection(a) == [-4, 0, 2, 3, 6, 7, 8, 9], 'It\'s failed'
assert selection(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
assert selection(c) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
