package main

import "fmt"

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

func main() {
	res1 := findMedianSortedArrays([]int{1, 3}, []int{2})
	fmt.Println(res1)
	res2 := findMedianSortedArrays([]int{1, 2}, []int{3, 4})
	fmt.Println(res2)
}
