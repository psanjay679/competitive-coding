from heapq import heappush, heappop, _heapify_max

n = int(raw_input())
ar = map(int, raw_input().split())

heap = []
_heapify_max(heap)

for el in ar:
	heappush(heap, el)
	_heapify_max(heap)

	if len(heap) < 3:
		print -1
	else:
		print heap[0] * heap[1] * heap[2]

