# coding: utf-8
"""
При сортировке Шелла сначала сравниваются и сортируются между собой значения, стоящие один от другого
на некотором расстоянии. После этого процедура повторяется для некоторых меньших значений d,
а завершается сортировка Шелла упорядочиванием элементов при d=1 (то есть обычной сортировкой вставками).
Эффективность сортировки Шелла в определённых случаях обеспечивается тем, что элементы «быстрее»
встают на свои места.



Худшее время
O(n2)
Лучшее время
O(n log2 n)
https://www.toptal.com/developers/sorting-algorithms/shell-sort
"""
from decorator_time import decorator_time


a = [0, 2, 3, -4, 6, 9, 7, 8]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class EmptyData(Exception):
    """Raises when data is None or not sequence."""


def make_steps(data=None):
    if all((data is None,
            not any([isinstance(data, _type) for _type in [list, tuple]]))):
        raise EmptyData()
    steps = []
    step = len(data)
    while step != 1:
        step /= 2
        steps.append(step)
    return steps


@decorator_time
def shell(data):
    for step in make_steps(data):
        for i in xrange(len(data)):
            if step == 1:
                for k in xrange(1, len(data)):
                    for j in xrange(len(data[:k])):  # sorted part
                        if data[j] > data[k]:
                            data[j], data[k] = data[k], data[j]
            else:
                try:
                    if data[i] > data[i + step]:
                        data[i], data[i + step] = data[i + step], data[i]
                except IndexError:
                    break
    return data


assert shell(a) == [-4, 0, 2, 3, 6, 7, 8, 9], 'It\'s failed'
assert shell(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
assert shell(c) == [1, 2, 3, 4, 5, 6, 7, 8, 9], 'It\'s failed'
