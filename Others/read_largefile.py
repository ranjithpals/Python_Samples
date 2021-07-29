from pathlib import Path
from collections import defaultdict

# Use Generator Function to read a large file
def read_largeFile(file_obj):
    for line in file_obj:
        yield line

# Read the file line by line
file_path = 'C:/Users/Owner/Documents/Trendy_Tech/Week-13/Datasets/bigLogNew.txt'
f_obj = open(file_path, 'r')
f = read_largeFile(f_obj)

# Calculate the number of entries for each status
d = defaultdict(int)
n = next(f)
while n:
    status = next(f).split(':')[0]
    #print(next(f))
    d[status] += 1
    try:
        n = next(f)
    except:
        break

print(d.items())

