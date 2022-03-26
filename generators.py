import os.path

# Practice the Generators
def gen_func(x):
    i = 0
    while i < x:
        yield i
        i += 1

for iter in gen_func(9):
    print(iter)

# Generators for Large File read
def csv_read(loc):
    f = open(loc, 'r', encoding='utf-8')
    for ln in f:
        yield ln
    f.close()

first = csv_read("C:/Users/Owner/Documents/Trendy_Tech/Week-13/Datasets/bigLogNew.txt")
## csv_read(os.path.dirname(__file__)+'/data_files/filegen.txt')

MAX_LINES = 10
print(f'Reading the first {MAX_LINES} lines of the file')
'''
for i, v in enumerate(first):
    if i < MAX_LINES:
        print(v)
'''
i = 0
while i < MAX_LINES:
    print(next(first))
    i += 1

# print(next(first))
# print(next(first))


