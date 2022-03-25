
from collections import Counter
import re
'''
d = {None: 'Ranjith'}
print(d)
e = ''
if e:
    print(e)
else:
    print('empty')

s = "Amazon*6467497"
p = s.partition('*')
print(p)
print(s[-4:])

num = 100101000
num_str = str(num)

l = re.findall('0+', num_str)
lst = sorted(l, key=len, reverse=True)
print("Longest Sequence of 0's: ", len(lst[0]))

l = [1, 2, 3, 5, 7, 5, 9]
print([i for k, i in enumerate(l) if k%2==0])

mystr = 'Srinika'
l = list(mystr)
print(l)
'''
grep = 'trail'
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

lst_out = [vehicle for vehicles in cars.values() for vehicle in vehicles if grep in vehicle.lower()]
print(lst_out)

l = map(lambda x: sorted(x, key=len, reverse=True)[0], cars.values())
print(list(l))

l = [1, 2, 4, -5, -7, 3, 1, -7]

t = set(l)
print(list(t)[-1])
print(len(t))
t = list(t)
t.sort()
print(t)

for i in range(9):
    print(i)

# No of Friends
lst = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'A'), ('E')]

from collections import defaultdict
from collections import Counter

de_d = defaultdict(int)

for d in lst:
    de_d[d[0]]+=1
    if len(d)>1: de_d[d[1]]+=1

print(dict(de_d))
print(Counter(lst))
