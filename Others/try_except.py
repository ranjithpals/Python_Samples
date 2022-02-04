def try_except(num):
    try:
        ans = num/(num-1)
    except:
        ans = 0
    else:
        ans += 1
    finally:
        print("The Result of the Operation is: ", ans)


if __name__ == '__main__':
    try_except(4)