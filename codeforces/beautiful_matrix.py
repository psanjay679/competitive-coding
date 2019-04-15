matrix = []
for _ in range(5):
	row = map(int, raw_input().split())
	matrix.append(row)

row, column = 0, 0
for _row in range(5):
	for _column in range(5):
		if matrix[_row][_column] == 1:
			row, column = _row, _column
			break

print (abs(row - 2) + abs(column - 2))
