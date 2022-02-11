package main

import "fmt"

func maxSlidingWindowA(nums []int, k int) []int {

	n := len(nums)

	if k < 1 || n == 0 {
		return []int{}
	}

	if n == 1 {
		return []int{nums[0]}
	}

	queue := []int{}
	res := []int{}

	for i := 0; i < n; i++ {
		if len(queue) > 0 && queue[0] == i-k {
			queue = queue[1:]
		}

		for len(queue) > 0 && nums[i] > nums[queue[len(queue)-1]] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, i)
		fmt.Println(queue)

		if i >= k-1 {
			res = append(res, nums[queue[0]])
		}

	}
	return res

}

func main() {
	fmt.Println(maxSlidingWindowA([]int{1, 3, -1, -3, 5, 3, 6, 7}, 3))
}
