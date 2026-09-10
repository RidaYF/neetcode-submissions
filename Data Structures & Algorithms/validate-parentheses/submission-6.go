func isValid(s string) bool {

	if len(s) == 0 || len(s) == 1 {
		return false
	}

	if len(s) == 2 {
		if int(s[0]) == int(s[1])-1 || int(s[0]) == int(s[1])-2 {
			return true
		} else {
			return false
		}
	}

	// Using stack
	var brackets = []byte{}
	var stack = []rune{}

	for i := 0; i < len(s); i++ {
		if s[i] == '(' || s[i] == '{' || s[i] == '[' ||
			s[i] == ')' || s[i] == '}' || s[i] == ']' {

			brackets = append(brackets, s[i])
		}
	}

	if len(brackets)%2 != 0 {
		return false
	}

	for _, char := range brackets {

		// Opening bracket → push into stack
		if char == '(' || char == '{' || char == '[' {
			stack = append(stack, rune(char))
			continue
		}

		// Closing bracket → get the top
		if len(stack) == 0 {
			return false
		}

		top := stack[len(stack)-1]

		// Check if top matches current character
		if (top == '(' && char == ')') ||
			(top == '{' && char == '}') ||
			(top == '[' && char == ']') {

			// Remove top from stack
			stack = stack[:len(stack)-1]

		} else {
			return false
		}
	}

	return len(stack) == 0
}