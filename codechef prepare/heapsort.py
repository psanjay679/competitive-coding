import random
ar = [random.randint(1, 100) for _ in range(10)]
print ar
def heapify(n, i):
	global ar
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2

	if (left < n) and ar[left] > ar[largest]:
		largest = left
	if (right < n) and ar[right] > ar[largest]:
		largest = right

	if largest != i:
		ar[i], ar[largest] = ar[largest], ar[i]
		heapify(n, largest)

def heapsort():
	global ar
	n = len(ar)
	for i in range(n/2 - 1, -1, -1):
		heapify(n, i)

	print ar

	for i in range(n-1, -1, -1):
		ar[0], ar[i] = ar[i], ar[0]
		heapify(i, 0)

heapsort()

print ar