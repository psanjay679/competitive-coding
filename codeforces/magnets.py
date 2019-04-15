n = int(raw_input())

ar = [0] * n

for i in range(n):
	ar[i] = raw_input()

groups = 1

for i in range(1, n):
	if ar[i][0] == ar[i - 1][1]: groups += 1

print groups
