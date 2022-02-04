class A:
    a = 5

    def change_A():
        a = 5
        return a


print(A.change_A())

a = 'ftw'
b = 'ftw'
print(a is b)

a = 'ftw!'
b = 'ftw!'
print(a is b)

print('atb''')

funcs = []
for x in range(7):
    def some_func(x=x):
        return x * x
    funcs.append(some_func)

funcs_results = [func() for func in funcs]
print(funcs_results)

def a():
    print(1)

print(id(a))
def a():
    print(2)

print(id(a))
b = a()
b