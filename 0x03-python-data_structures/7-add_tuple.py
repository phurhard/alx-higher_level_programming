#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 or len(tuple_b) == 1:
        tuple_a = list(tuple_a)
        tuple_a.append(0)
        tuple_a = tuple(tuple_a)
        tuple_b = list(tuple_b)
        tuple_b.append(0)
        tuple_b = tuple(tuple_b)
        return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    elif len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    elif len(tuple_a) == 0:
        tuple_a = (0, 0)
        return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
        return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
