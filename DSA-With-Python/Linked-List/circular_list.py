from traverse_list import List
from node import Node
import random

class CircularList(List):
	def __init__(self):
		super(CircularList, self).__init__()

		self.head.set_next(self.head)

	def get_last_node(self):
		curr = self.head
		while curr.get_next() != self.head:
			curr = curr.get_next()

		return curr

	def add_pos(self, pos, data):
		node = Node()
		node.set_data(data)
		if pos == 0:
			if self.head.get_data() is not None:
				last_node = self.get_last_node()
				last_node.set_next(node)
				node.set_next(self.head)
			else:
				self.head.set_data(node.get_data())
		elif pos == -1: # add to last
			last_node = self.get_last_node()
			node.set_next(self.head)
			last_node.set_next(node)
		else:
			i = 1
			curr = self.head
			while i < (pos - 1) and curr.get_next() != self.head:
				i += 1
				curr = curr.get_next()

			node.set_next(curr.get_next())
			curr.set_next(node)
	def __str__(self):
		curr = self.head
		while curr.get_next() != self.head:
			print curr.get_data(),
			curr = curr.get_next()

		print

if __name__ == "__main__":
	cl = CircularList()
	for _ in range(5):
		data = random.randint(45, 67)
		print data,
		cl.add_pos(0, data)

	print
	print 'clist'
	print cl