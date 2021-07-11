# print('Hello, world!')

d = {"flipkart.com":("clothes", "handbag", "laptop"), "amazon.com":("clothes", "mobile", "purse"), \
"myntra.com": ("purse", "clothes", "tv")}

revd = {v:k for k, v in d.items()}
print(d)

from collections import defaultdict

rev_d = defaultdict(list)
for k, v in d.items():
    if len(v) == 1:
        rev_d[v].append(k)
    elif len(v) > 1:
        for i in v:
            rev_d[i].append(k)

# print(type(rev_d))

print("inverted index:")
for i in rev_d.items():
    print(i) # rev_d.items())

