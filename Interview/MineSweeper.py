# Teladoc Interview
# Minesweeper game
#

from collections import defaultdict

b_dict = defaultdict(int)
bombs = []
def matrix(N, R, C):
    bombs = list(zip(R, C))
    for bx, by in bombs:
        if bx-1 >= 0 and by-1 >=0: b_dict[bx-1, by-1] += 1
        if bx-1 >= 0: b_dict[bx-1, by] += 1
        if by-1 >= 0: b_dict[bx, by-1] += 1
        if bx+1 < N: b_dict[bx+1, by] += 1
        if by+1 < N: b_dict[bx, by+1] += 1
        if bx+1 < N and by+1 < N: b_dict[bx+1, by+1] += 1
        if bx-1 >= 0 and by+1 < N: b_dict[bx-1, by+1] += 1
        if bx+1 < N and by-1 >= 0: b_dict[bx+1, by-1] += 1
    return dict(b_dict)

if __name__ == "__main__":
    #N = 3
    #R = [2, 0, 1, 2]
    #C = [0, 1, 2, 2]
    N = 5
    R = [1, 2, 3, 1, 3, 1, 2, 3]
    C = [1, 1, 1, 2, 2, 3, 3, 3]
    d = matrix(N, R, C)
    print(d)
    for x in range(N):
        for y in range(N):
            if (x, y) in list(zip(R, C)):
                print("B", end="")
            else:
                print(d[x, y], end="")
        print()
