import os.path

def csv_read(loc):
    f = open(loc, 'r')
    for ln in f:
        yield ln


first = csv_read(os.path.dirname(__file__)+'/data_files/filegen.txt')

print(next(first))
print(next(first))
print(next(first))
# print(next(first))
# print(next(first))

