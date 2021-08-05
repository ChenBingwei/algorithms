package main

import (
	"fmt"
	"math"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, i+1)
	}
	dp[0][0] = triangle[0][0]
	for i := 1; i < n; i++ {
		dp[i][0] = dp[i-1][0] + triangle[i][0]
		for j := 1; j < i; j++ {
			dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
		}
		dp[i][i] = dp[i-1][i-1] + triangle[i][i]
	}

	ans := math.MaxInt32
	for i := 0; i < n; i++ {
		ans = min(ans, dp[n-1][i])
	}
	return ans

}

func minimumTotal_plus(triangle [][]int) int {
	n := len(triangle)
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0][0] = triangle[0][0]
	for i := 1; i < n; i++ {
		dp[i&1][0] = dp[(i-1)&1][0] + triangle[i][0]
		for j := 1; j < i; j++ {
			dp[i&1][j] = min(dp[(i-1)&1][j], dp[(i-1)&1][j-1]) + triangle[i][j]
		}
		dp[i&1][i] = dp[(i-1)&1][i-1] + triangle[i][i]
	}

	ans := math.MaxInt32
	for i := 0; i < n; i++ {
		ans = min(ans, dp[(n-1)&1][i])
	}
	return ans
}

func minimumTotal_plus_plus(triangle [][]int) int {
	n := len(triangle)
	for i := 1; i < n; i++ {
		triangle[i][0] += triangle[i-1][0]
		for j := 1; j < i; j++ {
			triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
		}
		triangle[i][i] += triangle[i-1][i-1]
	}
	ans := math.MaxInt32
	for i := 0; i < n; i++ {
		ans = min(ans, triangle[n-1][i])
	}
	return ans
}

func main() {
	res1 := minimumTotal([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}})
	fmt.Println(res1)
	res2 := minimumTotal_plus([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}})
	fmt.Println(res2)
	res3 := minimumTotal_plus_plus([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}})
	fmt.Println(res3)
}
