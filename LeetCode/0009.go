package solutions

import "strconv"

func isPalindrome(x int) bool {
	// 不管有沒有迴文，負數的永遠錯
	if x < 0 {
		return false
	}

	// 小於 10，沒有必要判斷
	if x < 10 {
		return true
	}

	// [0 1 2 3]	length=4	/2=2	i=[0 1]	str[length-1-i]=[3 2]
	// [0 1 2 3 4]	length=5	/2=2.5	i=[0 1]	str[length-1-i]=[4 3]	2在最中間不用多判斷
	str := strconv.Itoa(x)
	length := len(str)
	for i := 0; i < length/2; i++ {
		if str[i] != str[length-1-i] {
			return false
		}
	}

	return true
}

