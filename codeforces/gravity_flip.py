n = int(raw_input())

ar = map(int, raw_input().split())

for i in range(n - 1):
	for j in range(n - 1):
		if ar[j] > ar[j + 1]:
			ar[j], ar[j + 1] = ar[j + 1], ar[j]

print ' '.join(str(k) for k in ar)
