'''
You can build your solution based on division by 2 method.
Your solution should return the correct binary equivalent of dec_num as a string from the convert_int_to_bin(dec_num)
in order to pass the tests.

Make sure that you use stack while solving this challenge.
The stack.py has been imported to the code.
You can make use of the implementation while coding your solution.
Remove the pass statement if you start implementing your solution.
'''

from stack import Stack


def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 1:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2
    s.push(dec_num)
    len_str = len(s.get_stack())
    con_str = [str(s.pop()) for i in range(len_str)]
    ans = ''.join(con_str)
    return ans