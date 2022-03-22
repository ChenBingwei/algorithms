def mySqrt(x: int) -> int:
    # if x in [0, 1]:
    #     return x

    low, high, res = 0, x, -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= x:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res


if __name__ == '__main__':
    print(mySqrt(8))
