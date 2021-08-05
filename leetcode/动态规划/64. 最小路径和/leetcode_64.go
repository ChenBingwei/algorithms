package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func minPathSum_1(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	dp[0][0] = grid[0][0]
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i > 0 && j > 0 {
				if dp[i-1][j] > dp[i][j-1] {
					dp[i][j] = dp[i][j-1] + grid[i][j]
				} else {
					dp[i][j] = dp[i-1][j] + grid[i][j]
				}
			} else if i > 0 {
				dp[i][j] = dp[i-1][j] + grid[i][j]
			} else if j > 0 {
				dp[i][j] = dp[i][j-1] + grid[i][j]
			}
		}
	}
	return dp[m-1][n-1]
}

func minPathSum_plus(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0][0] = grid[0][0]

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i > 0 && j > 0 {
				dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
			} else if i > 0 {
				dp[i][j] = dp[i-1][j] + grid[i][j]
			} else if j > 0 {
				dp[i][j] = dp[i][j-1] + grid[i][j]
			}
		}
	}
	return dp[m-1][n-1]
}

func main() {
	res1 := minPathSum_1([][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}})
	fmt.Println(res1)
	res2 := minPathSum_plus([][]int{{1, 2, 3}, {4, 5, 6}})
	fmt.Println(res2)
}
