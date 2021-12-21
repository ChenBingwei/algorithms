package main

import (
	"fmt"
	"sort"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	copy(nums1[m:], nums2)
	sort.Ints(nums1)
}

func merge_p(nums1 []int, m int, nums2 []int, n int) {
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
	copy(nums1, nums3)
}

// 严格来说，在此遍历过程中的任意一个时刻，
// nums1数组中有 m-p1-1 个元素放入nums1的后半部分
// nums2数组中有 n-p2-1 个元素放入nums1的后半部分
// 而在指针p1后面，nums1数组还有 m+n-p1-1 个位置
// 需要满足 m+n-p1-1 >= m-p1-1 + n-p2-1
// 等价于 p2 >= -1 所以永远成立
func merge_pp(nums1 []int, m int, nums2 []int, n int) {
	for p1, p2, tail := m-1, n-1, m+n-1; p1 >= 0 || p2 >= 0; tail-- {
		var cur int

		if p1 == -1 {
			cur = nums2[p2]
			p2--
		} else if p2 == -1 {
			cur = nums1[p1]
			p1--
		} else if nums1[p1] > nums2[p2] {
			cur = nums1[p1]
			p1--
		} else {
			cur = nums2[p2]
			p2--
		}
		nums1[tail] = cur
	}
}
func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	m, n := 3, 3
	//merge(nums1, m, nums2, n)
	//merge_p(nums1, m, nums2, n)
	merge_pp(nums1, m, nums2, n)
	fmt.Println(nums1)

}
