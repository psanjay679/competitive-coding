class Heap:

	def __init__(self,  max_size):
		self.size = 0
		self.max_size = max_size
		self.ar = [float('inf')] * self.max_size

	def parent(self, i):
		return i / 2

	def left(self, i):
		return i * 2 + 1

	def right(self, i):
		return i * 2 + 1

	def get_min(self):
		return self.ar[0]

	def insert(self, key):
		assert self.size < self.max_size

		self.size += 1
		i = self.size - 1
		self.ar[i] = key

		while i != 0 and self.ar[self.parent(i)] > self.ar[i]:
			self.ar[self.parent(i)], self.ar[i] = self.ar[i], self.ar[self.parent(i)]
			i = self.parent(i)

	def decrease_key(self, i, new_val):
		self.ar[i] = new_val

		while i != 0 and self.ar[self.parent(i)] > self.ar[i]:
			self.ar[self.parent(i)], self.ar[i] = self.ar[i], self.ar[self.parent(i)]
			i = self.parent(i)

	def extract_min(self):
		assert self.size > 0

		root = self.ar[0]
		self.ar[0] = self.ar[self.size - 1]
		self.size -= 1
		self.min_heapify(0)

		return root

	def min_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		smallest = i

		if l < self.size and self.ar[l] < self.ar[i]:
			smallest = l

		if r < self.size and self.ar[r] < self.ar[smallest]:
			smallest = r

		if smallest != i:
			self.min_heapify(smallest)

	def delete_key(self, i):
		self.decrease_key(i, float('-inf'))
		self.extract_min()



def main():
	h = Heap(11)
	h.insert(3)
	h.insert(2)
	print h.ar
	h.delete_key(1)
	h.insert(15)
	h.insert(5)
	h.insert(4)
	h.insert(45)

	print h.ar

if __name__ == '__main__':
	main()
