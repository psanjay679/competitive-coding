ar = map(int, raw_input().split())

s = raw_input().strip()

total = 0
for c in s:
	total += ar[int(c) - 1]

print total