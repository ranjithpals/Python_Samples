from collections import defaultdict

l = [1, 2, 3, 3, 4, 4, 5]

r = defaultdict(int)

for i in l:
    r[i]+=1

#r = {1:1}
print(r)



