package solutions

func isValid(s string) bool {

	size := len(s)
	stack := make([]rune, size)
	top := 0

	for _, c := range s {
		switch c {
		case '(':
			stack[top] = c + 1 // '('+1 = ')'
			top++
		case '{', '[':
			stack[top] = c + 2 // +2 = '}' or ']'
			top++
		default: // ')', ']', '}'
			if top > 0 && stack[top-1] == c {
				top--
			} else {
				return false
			}
		}
	}

	return top == 0
}

