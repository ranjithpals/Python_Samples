l = [0, 1, 3, 0, 2]
zero_count=l.count(0)
for i in l:
    if i==0:
        l.remove(i)
print(l)
z_l =[]
for _ in range(zero_count):
    z_l.append(0)

f_l = z_l+l
print(f_l)

z_c = l.count(0)
l1 = [0]*z_c
l1.extend([i for i in l if i>0])
print(l1)