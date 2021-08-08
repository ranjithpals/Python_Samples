import operator

l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
l3 = [5, 6, 7, 8]

lr = map(operator.mul, l1, l2)

print(list(lr))