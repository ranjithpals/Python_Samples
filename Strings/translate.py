str1 = "wy"

# specify to replace with
str2 = "gf"

# delete chars
str3 = "us"

# target string
trg = "weeksyourweeks"

# using maketrans() to
# construct translate
# table
# str1 -> the characters which need to be replaced (represented as character set)
# str2 -> the character in the character set needs to be replaced with respect to the position count of the str1
# in the above ex. replace w -> g, y -> f
# str3 -> characters need to be avoided (represented as a character set)
table = trg.maketrans(str1, str2, str3)

print(table)

print(trg.translate(table))