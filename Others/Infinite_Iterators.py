
## Use of count iterator for infinite loops
from itertools import count

i = 0
c = count(5, 5)
while c:
    if i > 5:
        break
    else:
        i+=1
        #print(next(c))

## Use of cycle iterator for infinite loops
from itertools import cycle
i = 0
c = cycle('123456')

while c:
    if i > 5:
        break
    else:
        i += 1
        #print(next(c))


## Use of repeat iterator for infinite loops
from itertools import repeat

i = 0
r = repeat(10)

while r:
    if i < 5:
        i += 1
        #print(next(r))
    else:
        break

## Use of repeat iterator with a finite loop
rp = repeat(10, 7)

a = [r for r in rp]
print(a)
'''
rp1 = next(rp)
while rp1:
    print(rp1)
'''