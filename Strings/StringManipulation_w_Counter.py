from collections import Counter
from string import punctuation, whitespace
import sys
import re
from pathlib import Path


def most_common_str(s, n=None):
    # str.maketrans(arg1, arg2, arg3) function creates a rule for translation
    # str is string class, arg1 => string to be replaced, arg2 => string replaced with, arg3 => remove the string
    # string_obj.translate() performs the actual translation
    # punctuation refers to the any of this group of characters !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    words = s.lower().translate(str.maketrans('', '', punctuation)).split()
    print(words[:10])
    return Counter(words).most_common(n)


def most_common_re(s, n=None):
    # [^{}{}] - Negate all the characters within the pattern
    # ^ - Negate character, rest of the characters is selected
    # Counter function is applied on the result
    return Counter(re.findall(rf'[^{punctuation}{whitespace}]+',
                              s.lower())).most_common(n)



def most_common_iter(s, n=None):
    # Remove the punctuation in all the words, passing through each character of a word
    # apply join function on the remaining words after removing punctuation character
    return Counter(''.join(c for c in w if c not in punctuation)
                   for w in s.lower().split()).most_common(n)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        p_path = Path.cwd().parent
        f_path = p_path/'data_files/harry.txt'
        file = f_path

    with open(file, encoding='utf8') as f:
        common_words = most_common_str(f.read(), n=20)

    for word, count in common_words:
        print('{:<4} {}'.format(count, word))

    with open(file, encoding='utf8') as f:
        print(list(most_common_re(f.read(), n=10)))
