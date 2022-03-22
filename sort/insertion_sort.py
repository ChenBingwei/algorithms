def insertion_sort_a(nums):
    n = len(nums)
    if n < 2:
        return nums
    for i in range(1, n):
        j = i
        while j >= 1 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


def insertion_sort_b(nums):
    n = len(nums)
    if n < 2:
        return nums
    for i in range(1, n):
        key = nums[i]
        j = i
        while j > 0 and nums[j - 1] > key:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = key
    return nums


if __name__ == '__main__':
    print(insertion_sort_a([5, 4, 8, 9, 3]))
    print(insertion_sort_b([5, 4, 8, 9, 3]))
