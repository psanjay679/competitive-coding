from heapq import _heapify_max

t = int(raw_input())

for _ in range(t):
	n = int(raw_input())

	ar = map(int, raw_input().split())
	ar.sort()

	print ' '.join(str(k) for k in ar[1:n + 1])

	#
	# _heapify_max(ar)
	#
	# ans = list()
	# k = 0
	# last_el = -2
	# while k < n:
	# 	ans.append(ar[last_el])
	# 	k += 1
	# 	last_el -= 1
	#
	# print ' '.join(str(k) for k in ans)

