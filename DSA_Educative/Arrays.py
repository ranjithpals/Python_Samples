
# Add a given digit to Indices of an Array
def arbitrary_increment(lst_input, increment):
    # Reverse the provided list for easy adding
    rev_list = lst_input
    rev_list.reverse()
    mod_list = []
    inc = increment
    for i in rev_list:
        add_i = i + inc
        num = add_i//10
        rem = add_i % 10
        mod_list.append(rem)
        inc = num
    # Reverse the mod_list
    mod_list.reverse()
    return mod_list


# Add two numbers of a given array to match up a given number
# Assumption: There is only one solution to the problem
def two_sum(lst_input, sum_num):
    for i, val in enumerate(lst_input):
        diff = sum_num - val
        lst_input.remove(val)
        if diff in lst_input and (diff != lst_input[i]):
            return val, diff


# Given two sorted arrays, A and B, determine their intersection.
# What elements are common to A and B?
def intersect_two_arrays(A, B):
    intersection = []
    srta = sorted(A)
    srtb = sorted(B)
    i = 0
    j = 0

    while i < len(srta) and j < len(srtb):
        if srta[i] == srtb[j]:
            intersection.append((srta[i], srtb[j]))
            i += 1
            j += 1
        elif srta[i] > srtb[j]:
            j += 1
        elif srta[i] < srtb[j]:
            i += 1
    return intersection


def diff_two_arrays(A, B):
    srta = sorted(A)
    srtb = sorted(B)
    i = 0
    j = 0

    while i < len(srta) and j < len(srtb):
        if srta[i] == srtb[j]:
            srta.remove(srta[i])
            srtb.remove(srtb[i])
        elif srta[i] > srtb[j]:
            j += 1
        elif srta[i] < srtb[j]:
            i += 1
    return srta


if __name__ == "__main__":
    # Arbitrary Increment
    lst = [1, 4, 9]
    number = 17
    print(f'Arbitrary Increment {arbitrary_increment(lst, number)}')

    # Add two numbers of Array to a specific number
    lst = [2, 1, 2, 4, 7, 11]
    req_num = 13
    print(f'Two Numbers-sum up to {req_num} is {two_sum(lst, req_num)}')

    A = [2, 3, 3, 5, 7, 11]
    B = [3, 3, 7, 15, 31]
    print(intersect_two_arrays(A, B))

    A = [1, 2, 2]
    B = [1]
    print(diff_two_arrays(A, B))