f = lambda x:x+1
print(f(2))


import operator
add = operator.add
add1 = add(3, 4)
print(add1)

from functools import partial
fn = partial(operator.add, 3)
print(fn(4))

print("Item Getter Operator Function")
fnc = operator.itemgetter(0)
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