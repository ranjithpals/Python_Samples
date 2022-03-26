# Factorial using Recursion
facto = 0
def fact(x):
    if x == 1:
        return 1
    facto = x * fact(x-1)
    return facto

x = 5
print(f'Factorial of {x} is {fact(x)}')

# Fibonacci using Regular Loops
def fibonacci(x):
    f1, f2 = 0, 1
    for i in range(x-1):
        f1, f2 = f2, (f2+f1)
    return f2
# print('fibonacci', fibonacci(8))


# flatten complex list
print(f'Flatten Logic Starts')

def flatten(elem):
    flat = []
    for e in elem:
        if isinstance(e, int):
            flat += [e]
        else:
            flat += flatten(e)
    return flat

cl = [1, [2, 3], 4, [[5,6],7]]
print(flatten(cl))