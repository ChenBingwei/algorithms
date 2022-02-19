package main

import "fmt"

func mySqrt(x int) int {
	low, high, res := 0, x, -1
	for low <= high {
		mid := low + (high-low)/2
		if mid*mid <= x {
			res = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return res
}

func main() {
	fmt.Println(mySqrt(8))
}
