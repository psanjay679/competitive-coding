n = int(raw_input())

ar = map(int, raw_input().split())

sereja = dima = 0

start = 0
end = n - 1

for i in range(n):
	if i % 2 == 0:
		# sereja's turn
		if ar[start] > ar[end]:
			sereja += ar[start]
			start += 1
		else:
			sereja += ar[end]
			end -= 1
	else:
		if ar[start] > ar[end]:
			dima += ar[start]
			start += 1
		else:
			dima += ar[end]
			end -= 1
print sereja, dima