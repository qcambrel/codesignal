def firstNotRepeatingCharacter(s):
	for char in s:
		if s.index(char) == s.rindex(char):
			return char
	return '_'