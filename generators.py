import os.path

def csv_read(loc):
    f = open(loc, 'r')
    for ln in f:
        yield ln


first = csv_read("C:/Users/Owner/Documents/Trendy_Tech/Week-13/Datasets/bigLogNew.txt")
## csv_read(os.path.dirname(__file__)+'/data_files/filegen.txt')

for i in range(10):
    print(next(first))

# print(next(first))
# print(next(first))

