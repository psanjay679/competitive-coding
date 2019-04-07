import math
import string

t = int(raw_input())

ans_fmt = 'Case #{}: {}'

for case in range(t):
	case += 1
	n, l = map(int, raw_input().strip().split())
	ct = map(int, raw_input().strip().split())

	first = 0
	primes = []

	for i in range(3, int(math.sqrt(ct[0])) + 1):
		if ct[0] % i == 0:
			primes.append(i)
			break

	for i, c in enumerate(ct):
		primes.append(c / primes[-1])

	pts = sorted(set(primes))

	dt = {}

	for c, pt in zip(string.ascii_uppercase, pts):
		dt[pt] = c

	ans = ""

	for value in primes:
		ans += dt[value]

	print (ans_fmt.format(case, ans))
