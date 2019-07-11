package solutions

func longestCommonPrefix(strs []string) string {

	// 沒資料直接回傳空值
	if len(strs) == 0 {
		return ""
	}

	// 找出最短的字
	short := strs[0]

	for _, str := range strs {
		if len(short) > len(str) {
			short = str
		}
	}

	// 比較前綴
	// short = flow
	// 迭代 flow -> [f l o w]
	// f:	flower -> V
	//	flow -> V
	//	flight -> V
	// l:	flower -> V
	//	flow -> V
	//	flight -> V
	// o:	flower -> V
	//	flow -> V
	//	flight -> X return "fl"ight
	for i, r := range short {
		for j := 0; j < len(strs); j++ {
			if strs[j][i] != byte(r) {
				return strs[j][:i]
			}
		}
	}

	return short
}

