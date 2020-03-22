def firstDuplicate(a):
	pre_filter = set(a)
	if len(pre_filter) == len(a):
		return -1
	new_filter = set()
	for num in a:
		if num in new_filter:
			return num
		new_filter.add(num)
