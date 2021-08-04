package main

import "fmt"

func twoSum(nums []int, target int) []int {
	itemDict := map[int]int{}
	for i, v := range nums {
		if p, ok := itemDict[target-v]; ok {
			return []int{p, i}
		}
		itemDict[v] = i
	}
	return nil
}

func main() {
	res1 := twoSum([]int{2, 7, 11, 15}, 9)
	fmt.Println(res1)
}
