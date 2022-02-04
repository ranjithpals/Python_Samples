def make_print(x):

    def printx():
        print(x)

    return printx


f = make_print(7)
f()


# closure with bracket types
def support_brackets(start, end):

    def add_brackets(x):
        print(start + str(x) + end)

    return add_brackets


f = support_brackets('<', '>')
f(5)


# add a number to every element of a list
def add():

    def inner(x):
        x=x+1
        return x

    return inner


lst = [1, 2, 5, 7, 9]
b = map(add(), lst)
print(list(b))

# add 1 to every element
'''
ops = {'+': 'add', '-': 'subtract'}
def operation(o):
    def add(x):
        return x[0]+x[1]
    def subtract(x):
        return x[0]-x[1]
    return ops[o]


c = map(operation('+'), lst)
print(list(c))
'''


def my_print():
    def print_hi():
        print('hi')

    return print_hi


fn = my_print()
fn()

def simple():
    def simple_1():
        return 'Hi'
    return simple_1()

fh = simple()
print(fh)
