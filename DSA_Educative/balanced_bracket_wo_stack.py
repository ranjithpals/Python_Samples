def flip_bracket(s:str) -> str:
    if s == '}':
        return '{'
    elif s == ']':
        return '['
    elif s == ')':
        return '('
    else:
        return 'n/a'

def is_brackets_balanced(pattern):
    '''
    Validate if the brackets are balanced
    Can have other characters apart from opening and closing brackets
    Ignore the other characters
    '''
    val_list = []
    bool_balanced = True
    for elem in pattern:
        if elem in '([{':
            val_list.append(elem)
        elif len(val_list) == 0:
            bool_balanced = not bool_balanced
            break
        elif elem in ')]}':
            # Check if the flipped value is same as the last character in val_list
            if flip_bracket(elem) != val_list[-1]:
                bool_balanced = not bool_balanced
                break
            else:
                # Remove the last added value
                val_list.pop()

    if bool_balanced and len(val_list) == 0:
        return True
    else:
        return False

string = '{{{[(9)]}}}{[]}}'
result = is_brackets_balanced(string)
ans = 'balanced' if result else 'unbalanced'

print(f'The brackets in the provided pattern {string} are {ans}')
