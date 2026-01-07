from functools import reduce

numbers = [12,45,33,67,89,30]

def num_even(n):
    return n % 2 == 0      # filter

def num_add(n):
    return n + 1           # map

def add(a, b):
    return a + b           # reduce

filter_num = list(filter(num_even, numbers))
print(filter_num)

map_num = list(map(num_add, filter_num))
print(map_num)

reduce_num = reduce(add, map_num)
print(reduce_num)



