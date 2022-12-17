from collections import deque
from itertools import zip_longest

def merge_sort(a, b):
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

def ver_compare(v_first, v_second):
    ver_1 = [int(i) for i in v_first.split('-')[0].split('.')]
    ver_2 = [int(i) for i in v_second.split('-')[0].split('.')]
    for pair in zip_longest(ver_1, ver_2, fillvalue=0):
        if pair[0] > pair[1]:
            return 1
        elif pair[0] < pair[1]:
            return -1
    return 0
