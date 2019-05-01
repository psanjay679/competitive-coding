from heapq import heapify, heappop, heappush, nlargest, nsmallest, _heapify_max
import random

ar = [random.randint(45, 55) for _ in range(10)]
print ar

_heapify_max(ar)

print ar

