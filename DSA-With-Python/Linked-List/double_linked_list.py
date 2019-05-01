from __future__ import print_function
from node import NodeD as Node
import random

class DList:
	def __init__(self):
		self.head = Node()

	def insert(self, pos, data):
		node = Node()
		node.set_data(data)

		if self.head.get_data() is None:
			self.head = node
		else:
			if pos == 0:
				node.set_next(self.head)
				self.head.set_prev(node)
				self.head = node
			else:
				i = 1
				curr = self.head
				while i < (pos - 1) and curr.has_next():
					curr = curr.get_next()
					i += 1

				node.set_next(curr.get_next())
				node.set_prev(curr)
				curr.get_next().set_prev(node)
				curr.set_next(node)

	def delete(self, pos):
		if pos == 0:
			self.head = self.head.get_next()
			self.head.set_prev(None)
		else:
			i = 1
			curr = self.head
			while i < (pos - 1) and curr.get_next().has_next():
				curr = curr.get_next()
				i += 1

			d_node = curr.get_next()
			next_node = d_node.get_next()

			d_node.set_prev(None)
			d_node.set_next(None)
			next_node.set_prev(curr)
			curr.set_next(next_node)

	def traverse(self):
		curr = self.head

		while curr:
			print (curr.data)
			curr = curr.get_next()

if __name__ == '__main__':

	l = DList()
	print ('===== data =====')
	for _ in range(5):
		data = random.randint(45, 100)
		print (data, end=" ")
		l.insert(0, data)
	print ('\n===== data ends here =====')

	l.traverse()
	print('-----')
	l.delete(2)
	print ('-----')

	l.traverse()