from __future__ import print_function

n, h = map(int, raw_input().split())

ar = map(int, raw_input().split())

ans = 0

for el in ar:
	if el > h: ans += 2
	else: ans += 1

print (ans)