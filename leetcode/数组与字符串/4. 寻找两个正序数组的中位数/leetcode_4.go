package main

import (
	"fmt"
	"math"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) (ans float64) {
	m, n := len(nums1), len(nums2)
	nums3 := make([]int, 0, m+n)
	p1, p2 := 0, 0
	for {
		if p1 == m {
			nums3 = append(nums3, nums2[p2:]...)
			break
		}
		if p2 == n {
			nums3 = append(nums3, nums1[p1:]...)
			break
		}
		if nums1[p1] < nums2[p2] {
			nums3 = append(nums3, nums1[p1])
			p1++
		} else {
			nums3 = append(nums3, nums2[p2])
			p2++
		}
	}
	ans = float64(nums3[(m+n)/2]+nums3[(m+n-1)/2]) / 2
	return
}

func findMedianSortedArrays_p(nums1 []int, nums2 []int) (ans float64) {
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}
	m, n := len(nums1), len(nums2)

	// 分割线左边的元素需要满足的个数
	// 由于是整数除向下取整，在约定total为奇数时左边做一个的情况，
	// 分割线左边的数量均可以表示为如下
	totalLeft := (m + n + 1) / 2

	// 在nums1的区间[0,m]里查找恰当的分割线，
	// 假定i,j分别为nums1和Nums2在分割线右边元素的下标，同时也是nums1和nums2在分割线左边元素个数
	// 使得 nums1[i-1]<=nums2[j] && nums1[i] >= nums2[j-1]
	left := 0
	right := m
	for {
		if left >= right {
			break
		}
		i := left + (right-left+1)/2
		j := totalLeft - i
		if nums1[i-1] > nums2[j] {
			// 下一轮搜索区间 [left, i - 1]
			right = i - 1
		} else {
			// 下一轮搜索区间 [i, right]
			// [left(i), right]
			left = i
		}
	}
	i := left
	j := totalLeft - i
	var nums1LeftMax, nums1RightMin, nums2LeftMax, nums2RightMin int
	if i == 0 {
		nums1LeftMax = math.MinInt32
	} else {
		nums1LeftMax = nums1[i-1]
	}
	if i == m {
		nums1RightMin = math.MaxInt32
	} else {
		nums1RightMin = nums1[i]
	}
	if j == 0 {
		nums2LeftMax = math.MinInt32
	} else {
		nums2LeftMax = nums2[j-1]
	}
	if j == n {
		nums2RightMin = math.MaxInt32
	} else {
		nums2RightMin = nums2[j]
	}

	if (m+n)%2 == 1 {
		ans = float64(max(nums1LeftMax, nums2LeftMax))
	} else {
		ans = float64(max(nums1LeftMax, nums2LeftMax)+min(nums1RightMin, nums2RightMin)) / 2
	}
	return

}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	res1 := findMedianSortedArrays([]int{1, 3}, []int{2})
	fmt.Println(res1)
	res2 := findMedianSortedArrays_p([]int{1, 2}, []int{3, 4})
	fmt.Println(res2)
}
