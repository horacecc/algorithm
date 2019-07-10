package solutions

import "math"

func reverse(x int) int {
	sign := 1

	// 處理正負
	if x < 0 {
		sign = -1
		x *= -1
	}

	// 數字反轉
	res := 0

	for x > 0 {
		res = res*10 + x%10
		x = x / 10
	}

	// 還原正負
	res *= sign

	// 處理 overflow
	if res > math.MaxInt32 || res < math.MinInt32 {
		res = 0
	}

	return res
}

