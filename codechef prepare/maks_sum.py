from heapq import heappop, heapify, heappush

def main():
	t = int(raw_input())

	for _ in range(t):
		n, k1, k2, k3 = map(int, raw_input().split())

		ar = map(int, raw_input().split())
		sums = [0] * (len(ar) + 1)
		sums[0] = 0
		sums[1] = ar[0]

		for i in range(2, n + 1):
			sums[i] = sums[i - 1] + ar[i - 1]

		h = []
		heapify(h)

		for i in range(1, n + 1):
			for j in range(i + 1, n + 1):
				x = sums[j] - sums[i - 1]
				if len(h) < k1:
					heappush(h, x)
				else:
					if x > h[0]


main()