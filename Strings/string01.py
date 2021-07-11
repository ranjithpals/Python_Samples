# Strings are immutable
s = "all is well"
# Find the count of the substring found in the string
print(s.count('l'))
# Find the first occurrence of the substring in the string
print(s.find('l'))
print(s.find('7'))
# Find the first occurrence using index function - if not found will throw ValueError
# print(s.index('7'))

# Split the string
ss = s.split()
print(ss)
# Join the list elements
s = ' '.join(ss)
print(s)
# Rsplit - Split starting from Right Side
rs = s.rsplit(' ', 1)
print(rs)
# Only N number of Splits are needed - 1 split
s1 = s.split(' ', 1)
print(s1)
# Partition the string - Output would be Tuple (prior string, partition string, post string)
ps = s.partition('l')
print(ps)
# Strip and rstrip
s2 = "I am doing Ok today "
print(s2.strip())

print(s2+'How about you?')
print(s2.strip()+'How about you?')