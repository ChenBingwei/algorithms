package main

import "fmt"

// function 1: Violent enumeration
func longestPalindrome(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}

	begin, maxLen := 0, 1
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if j-i+1 > maxLen && validPalindrome(s, i, j) {
				maxLen = j - i + 1
				begin = i
			}
		}
	}

	return s[begin : begin+maxLen]
}

func validPalindrome(s string, left int, right int) bool {

	//i,j := left,right
	for {
		if left >= right {
			break
		}
		if s[left] != s[right] {
			return false
		} else {
			left++
			right--
		}
	}
	return true
}

// function 2: Center extension
func longestPalindromeP(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}

	begin, maxLen := 0, 1
	for i := 0; i < n-1; i++ {
		oddLen := expandAroudCenter(s, i, i)
		evenLen := expandAroudCenter(s, i, i+1)
		curLen := func(x int, y int) int {
			if x > y {
				return x
			}
			return y
		}(oddLen, evenLen)
		if curLen > maxLen {
			maxLen = curLen
			// odd: begin = i - (maxlen - 1) / 2
			// even: begin = i - (maxlen - 2) / 2
			begin = i - (maxLen-1)/2
		}
	}
	return s[begin : begin+maxLen]

}

func expandAroudCenter(s string, left int, right int) int {
	n := len(s)
	for {
		if left < 0 || right >= n {
			break
		}
		if s[left] != s[right] {
			break
		} else {
			left--
			right++
		}
	}
	// len = right -left + 1 -2
	return right - left - 1
}

// function 3: 动态规划
func longestPalindromePP(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}

	begin, maxLen := 0, 1
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
		dp[i][i] = true
	}

	for j := 0; j < n; j++ {
		for i := 0; i < j; i++ {
			if s[i] != s[j] {
				dp[i][j] = false
			} else if j-i < 3 {
				dp[i][j] = true
			} else {
				dp[i][j] = dp[i+1][j-1]
			}

			if dp[i][j] && j-i+1 > maxLen {
				maxLen = j - i + 1
				begin = i
			}
		}
	}
	return s[begin : begin+maxLen]

}

func main() {
	testStr := []string{"adbab", "cbbd", "a", "ac"}
	for _, v := range testStr {
		fmt.Println(
			longestPalindrome(v),
			longestPalindromeP(v),
			longestPalindromePP(v),
		)
	}
}
