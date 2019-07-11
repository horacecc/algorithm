package solutions

func romanToInt(s string) int {
	if s == "" {
		return 0
	}

	total, last := 0, 0
	roman := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	for i := len(s) - 1; i >= 0; i-- {
		val := roman[s[i]]
		if val < last {
			total -= val
		} else {
			total += val
		}
		last = val
	}

	return total
}

