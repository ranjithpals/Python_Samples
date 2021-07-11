import re

ss = 'Wonderful'
p = 'Wonder'
ans = re.match(p, ss)
print(ans)

# Wild characters
p = '.onder'
ans = re.match(p, ss)
print(ans)

# escape character
ss1 = '12-01-2020'
p = '^[0-9]+\-'
ans = re.match(p, ss1)
print(ans)

# White space Characters
ss2 = '\t56n'
p = '\s\d'
print(re.match(p, ss2))

# Previous pattern (Single or Group of Characters) can be repeated zero or more than zero times (0 or > 0)
ss3 = '7489w'
p = '[\d]*'
print(re.match(p, ss3))

# Previous pattern (Single or Group of Characters) can repeated one or more times (1 or >1)
ss3 = '68uws'
p = '[\d]+'
print(re.match(p, ss3))