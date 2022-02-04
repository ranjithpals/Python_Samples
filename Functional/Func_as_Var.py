f = lambda x:x+1
print(f(2))


import operator
add = operator.add
add1 = add(3, 4)
print(add1)

from functools import partial
fn = partial(operator.add, 3)
print(fn(4))

fnc = operator.itemgetter(3)
a = fnc([1, 2, 3, 4, 5, 6])
print(a)


def mut_func(x):
    x[2] = 0

l = [1, 2, 3, 4, 5]
l_tup = (1, 2, 3, 4, 5)
mut_func(l[:])
print(l,)

def tail(x):
    # y = list(x)
    # del y[0]
    return x[1:]

ll = tail(l_tup)
print(l, ll)

# Factorial using Recursion
factorial = 0
def fact(x):
    if x == 1:
        return 1
    factorial = x * fact(x-1)
    return factorial

print(fact(8))

# Fibonacci using Recursion


def fibonacci(x):
    f1, f2 = 0, 1
    for i in range(x-1):
        f1, f2 = f2, (f2+f1)
    return f2


print('fibonacci', fibonacci(8))

# flatten complex list
'''
flat = []
c_list = []
def flatten(elem):
    for c_elem in elem:
        if isinstance(c_elem, int):
            flat.append(c_elem)
        else:
            flatten(elem)
    return flat

cl = [1, [2, 3], 4, [[5,6],7]]
print(flatten(cl))
'''

