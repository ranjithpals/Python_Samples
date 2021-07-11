# Tuple & Dictionaries
x = (1, 2, 3)
print(x[2])

x, y, z = (1, 3, 5)
print(x, y)

from collections import namedtuple
# Named Tuple
stock = namedtuple('Symbol', 'value max min')
fb = stock('45', '56', '34')

print(fb.value)

# Dictionary
stocks = {'RIL': (45, 56, 23),
          'GOOG': (230, 350, 125)}

print(stocks['GOOG'])
print(stocks['RIL'][1])

# Without the get access key, we will get an error for an non-existent value
try:
    print(stocks['ABC'])
except:
    print("Key not available")

# Using Get keyword there will be no exceptions
print(stocks.get('ABC'))
# Can have a default value if not found
print(stocks.get('ABC'), "Not Found")

# Get Keys
print(stocks.keys())
# Get Values
print(stocks.values())

# Get all items of a Dictionary
print(stocks.items())

from collections import defaultdict
# Default Dict
word_count = defaultdict(int)

file = open('filegen.txt', 'r')

for ln in file:
    for w in ln.split():
        word_count[w] += 1
# print(word_count)

l = [w for w in ln.split() for ln in file]
print(l)