# coding: utf-8

"""
из массива последовательно берется каждый элемент
вставляется в его отсортированную часть(например в начале массива)
https://www.toptal.com/developers/sorting-algorithms/insertion-sort
"""
from decorator_time import decorator_time
a = [0, 2, 3, -4, 6, 9, 7, 8]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]


@decorator_time
def insertion(data):
    for i in xrange(1, len(data)):
        for j in xrange(len(data[:i])):  # sorted part
            if data[j] > data[i]:
                data[j], data[i] = data[i], data[j]

    return data


assert insertion(a) == [-4, 0, 2, 3, 6, 7, 8, 9], 'It\'s failed'
assert insertion(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
assert insertion(c) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
