t = int(raw_input())

for __ in range(t):
	n, d = map(int, raw_input().split())

	ar = list()

	ar.append(map(int, raw_input().split()))
	ar.sort(key=lambda k: k[2], reverse=True)

	i = 0
	for _d in range(d):
		if _d > ar[i]