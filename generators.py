def csv_read(loc):
    f = open(loc, 'r')
    for ln in f:
        yield ln


first = csv_read('filegen.txt')

print(next(first))
print(next(first))
print(next(first))
# print(next(first))
# print(next(first))

