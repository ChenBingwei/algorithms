def insertion_sort_a(nums):
    n = len(nums)
    if n < 2:
        return nums
    for i in range(1, n):
        while i >= 1 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1
    return nums


if __name__ == '__main__':
    print(insertion_sort_a([5, 4, 8, 9, 3]))
