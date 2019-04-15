n = int(raw_input())

ar = list()

for _ in range(n):
	a, b = map(int, raw_input().split())
	ar.append((a, b))

count = 0

for i in range(n):
	for j in range(i + 1, n):
		if ar[i][1] == ar[j][0]:
			count += 1
		if ar[i][0] == ar[j][1]:
			count += 1

print count