package main

import (
	"fmt"
	"math"
)

func minOfArr(arr []int) int {
	min := 201
	for i := range arr {
		if arr[i] < min {
			min = arr[i]
		}
	}
	return min
}

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func minFallingPathSum(arr [][]int) int {
	n := len(arr)
	if n == 1 {
		return arr[0][0]
	}
	dp := make([][]int, n)
	for i := range dp {
		if i == 0 {
			dp[i] = arr[0]
		} else {
			dp[i] = make([]int, n)
		}
	}

	for i := 1; i < n; i++ {
		for j := 0; j < n; j++ {
			tmpArr := make([]int, n)
			copy(tmpArr, dp[i-1])
			valid_arr := append(tmpArr[:j], tmpArr[j+1:]...)
			dp[i][j] = minOfArr(valid_arr) + arr[i][j]
		}
	}

	return minOfArr(dp[n-1])
}

func minFallingPathSumPlus(arr [][]int) int {
	n := len(arr)
	if n == 1 {
		return arr[0][0]
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0] = arr[0]

	for i := 1; i < n; i++ {
		for j := 0; j < n; j++ {
			dp[i][j] = math.MaxInt32
			v := arr[i][j]
			for z := 0; z < n; z++ {
				if z != j {
					dp[i][j] = min(dp[i-1][z]+v, dp[i][j])
				}
			}
		}
	}

	ans := math.MaxInt32
	for i := 0; i < n; i++ {
		ans = min(ans, dp[n-1][i])
	}
	return ans

}

func minFallingPathSumPlusPlus(arr [][]int) int {
	n := len(arr)
	firstSum, firstPos, secondSum := 0, -1, 0
	for i := 0; i < n; i++ {
		fs, fp, ss := math.MaxInt32, -1, math.MaxInt32
		for j := 0; j < n; j++ {
			curSum := arr[i][j]
			if j != firstPos {
				curSum += firstSum
			} else {
				curSum += secondSum
			}
			if curSum < fs {
				ss, fs, fp = fs, curSum, j
			} else if curSum < ss {
				ss = curSum
			}
		}
		firstSum, firstPos, secondSum = fs, fp, ss
	}
	return firstSum
}

func main() {
	res1 := minFallingPathSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}})
	fmt.Println(res1)
	res2 := minFallingPathSumPlus([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}})
	fmt.Println(res2)
	res3 := minFallingPathSumPlusPlus([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}})
	fmt.Println(res3)
}
