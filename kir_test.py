from collections import deque
from itertools import zip_longest
from time import perf_counter

def merge_sort(a, b):

    if a and b:
        if a[-1] < b[0]:
            return a + b
        elif b[-1] < a[0]:
            return b + a
    
    merge = deque()
    while a and b:
        if a[-1] >= b[-1]:
            merge.appendleft(a.pop())
        else:
            merge.appendleft(b.pop())
    if a:
        a.extend(merge)
        return a
    b.extend(merge)
    return b

def merge_iter(a, b):
    result = []
    iter_a = iter(a)
    iter_b = iter(b)

    if a:
        next_a = next(iter_a)
    else:
        return b
    if b:
        next_b = next(iter_b)
    else:
        return a
    
    while True:
        if next_a <= next_b:
            result.append(next_a)
            try:
                next_a = next(iter_a)
            except StopIteration:
                result.append(next_b)
                result.extend(iter_b)
                return result
        else:
            result.append(next_b)
            try:
                next_b = next(iter_b)
            except StopIteration:
                result.append(next_a)
                result.extend(iter_a)
                return result

def merge_index(a, b):
    index_a = 0
    index_b = 0
    result = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1
    result.extend(a[index_a:])
    result.extend(b[index_b:])
    return result


def ver_compare(v_first, v_second):
    ver_1 = [int(i) for i in v_first.split('-')[0].split('.')]
    ver_2 = [int(i) for i in v_second.split('-')[0].split('.')]
    for pair in zip_longest(ver_1, ver_2, fillvalue=0):
        if pair[0] > pair[1]:
            return 1
        elif pair[0] < pair[1]:
            return -1
    return 0


TEST_DATA = (
    ([],[],[]),
    ([100,],[],[100,]),
    ([],[100],[100]),
    ([100],[100],[100,100]),
    ([1,2,3],[1,2,3],[1,1,2,2,3,3]),
    ([10,100,1000],[20,200,2000],[10,20,100,200,1000,2000]),
)

def test_merge(func, tests):
    for data in tests:
        assert func(data[0], data[1]) == data[2]

def perf_merge(func, tests):
    time_start = perf_counter()
    for data in tests:
        func(data[0], data[1])
    all_time = round(perf_counter() - time_start, 4)
    return all_time


for func in (merge_sort, merge_iter, merge_index):
    test_merge(func, TEST_DATA)

for func in (merge_sort, merge_iter, merge_index):
    result_time = []
    for times in range(3):
        result_time.append(perf_merge(func, ((list(range(10, 100000000, 20)), list(range(0, 100000000, 20))),)))
    print(f'{func.__name__} -> {result_time}')
