def length_of_longest_substring(s):
    n = len(s)
    occ = set()

    rk = -1  # right key
    res = 0
    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        res = max(res, rk - i + 1)
    return res


if __name__ == '__main__':
    print(length_of_longest_substring("abcabcbb"))
