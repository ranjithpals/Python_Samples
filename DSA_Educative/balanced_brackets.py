'''
https://www.educative.io/courses/ds-and-algorithms-in-python/g7Zp75M7LNk
In this lesson, we’re going to determine whether or not a set of brackets are balanced or not by making use of the stack
data structure that we defined in the previous lesson.

Let’s first understand what a balanced set of brackets looks like.

A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also
properly nested within the string of brackets.

As shown above, our algorithm is as follows:

We iterate through the characters of the string.
If we get an opening bracket, push it onto the stack.
If we encounter a closing bracket, pop off an element from the stack and match it with the closing bracket.
If it is an opening bracket and of the same type as the closing bracket, we conclude it is a successful match and move on.
If it’s not, we will conclude that the set of brackets is not balanced.
The stack will be empty at the end of iteration for a balanced example of brackets while we’ll be left with some elements
 in the stack for an unbalanced example.

 Examples of Balanced Brackets#
{ }
{ } { }
( ( { [ ] } ) )
Examples of Unbalanced Brackets#
( ( )
{ { { ) } ]
[ ] [ ] ] ]
'''

from stack import Stack


def is_match(c, s_elem):
    if c == ')' and s_elem == '(':
        return True
    elif c == ']' and s_elem == '[':
        return True
    elif c == '}' and s_elem == '{':
        return True
    else:
        return False


def bracket_match(b_string):
    s = Stack()
    is_balanced = True
    i = 0
    while i < len(b_string):
        curr_elem = b_string[i]
        if curr_elem in '({[':
            s.push(curr_elem)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(curr_elem, top):
                    is_balanced = False
                    break

        i += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(bracket_match('(((({}))))'))







