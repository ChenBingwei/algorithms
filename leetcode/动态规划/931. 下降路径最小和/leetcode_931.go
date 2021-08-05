package main

import "fmt"

func min(x int, y int) int {
	if x > y {
		return y
	}
	return x
}

func minFallingPathSum(matrix [][]int) int {
	n := len(matrix)
	//if n == 1 {
	//	return matrix[0][0]
	//}
	dp := make([][]int, n)
	dp[0] = matrix[0]
	for i := 1; i < n; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if j == 0 {
				dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
			} else if j == n-1 {
				dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
			} else {
				dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i-1][j+1]) + matrix[i][j]
			}
		}
	}

	ans := 200
	for i := 0; i < n; i++ {
		ans = min(ans, dp[n-1][i])
	}

	return ans
}

func main() {
	res1 := minFallingPathSum([][]int{{-19, 57}, {-40, -5}})
	//res1 := minFallingPathSum([][]int{{2, 1, 3}, {6, 5, 4}, {7, 8, 9}})
	fmt.Println(res1)
}
