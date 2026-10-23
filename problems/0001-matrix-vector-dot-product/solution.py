def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	columns = len(a[0])
	rows = len(a)
	if columns != len(b):
		return -1

	res = [0] * rows
	for i in range(rows):
		entry = 0
		for j in range(columns):
			entry += a[i][j] * b[j]
		res[i] = entry

	return res 