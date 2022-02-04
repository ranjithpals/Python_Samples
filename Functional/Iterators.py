a = [1, 8, 7]

b = iter(a)
print(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
# print(next(b)) #StopIteration

print('Sort using Sorted Function')
#print(sorted(a))

# Infinite prime numbers


def prime(n):
    i = 2
    while i<n:
        if n % i == 0:
            return None  # return False
        i += 1
    return n  # return True


# print(prime(5))
# l = range(1000)
# primes = filter(prime, l)
# print(list(primes))


lst = iter(range(1000))

# while lst:
#    print(prime(next(lst)))

for i in iter(range(100)):
    pass
    # print(prime(next(lst)))

# Fibonacci Iterator


class myFibonacci:
    first = 0
    second = 1
    count = 0
    nxt = 0

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            nxt = self.first + self.second
            self.first, self.second = self.second, self.first + self.second
            self.count += 1
            return nxt
        else:
            raise StopIteration


# print('=========Fibonacci Starts=========')
fib = 0
cnt = 0
n = 100

for nxt_val in myFibonacci(100):
    pass
    # print(nxt_val)


class Fibonacci:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        nxt = self.first
        self.first, self.second = self.second, self.first + self.second
        return nxt


print('=========Fibonacci Starts=========')
c = 0
for i in Fibonacci():
    if c < 10:
        #print(i)
        c += 1
    else:
        break

from operator import itemgetter

a = [2, 3, 5, 6, 7, 2]

c = filter(itemgetter(2), a)
c1 = filter(lambda x: x!=2, a)
print(list(c1))
#for c1 in c:
    #print(c1)

a = (1, 2, 3, 4)
b = ('ranjith', 'madhuri', 'srinika')

print(list(zip(a, b)))


def my_func(a,b,c):
    return a+b+c


a = [20, 30, 40]
b = [50, 70, 40]
c = [60, 80, 90]

y = map(my_func, a, b, c)
print(y)
print(list(y))

print(*zip(a,b,c))

import functools

def numbers():
    for num in [1,2,3,4]:
        print("hi")
        yield num

print("here 1")
g = numbers()
print("here 2")

next(g)
print("here 3")

next(g)
print("here 4")

def chain(it1, it2):
    for x in it1:
        yield x
    for x in it2:
        yield x

for i in chain(range(2), range(3)):
    print(i)


def quad(a, b, c, x):
    return a * x * x + b * x + c


def quad_ac(a, c):
    def f(b, x):
        return quad(a, b, c, x)

    return f


myquad = quad_ac(1, 2)
print(myquad(3, 4))

