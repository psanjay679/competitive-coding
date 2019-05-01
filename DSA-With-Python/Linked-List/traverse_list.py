from __future__ import print_function
from node import Node
import random

class List:
	def __init__(self):
		self.head = Node()

	def add_pos(self, pos, data):
		if pos == 0:
			node = Node()
			node.set_data(data)
			if self.head.get_data() == None:
				self.head = node
			else:
				node.set_next(self.head)
				self.head = node
		else:
			i = 1
			curr = self.head
			while (i < pos - 1) and curr.has_next():
				curr = curr.get_next()
				i += 1

			node = Node()
			node.set_data(data)
			node.set_next(curr.get_next())
			curr.set_next(node)

	def add_start(self, data):
		self.add_pos(0, data)

	def delete_pos(self, pos):
		if pos == 0:
			# delete starting node
			self.head = self.head.get_next()
		else:
			curr = self.head
			i = 1
			while (i < pos - 1) and curr.get_next().has_next():
				curr = curr.get_next()
				i += 1
			node = curr.get_next()
			curr.set_next(curr.get_next().get_next())
			node.set_next(None)

	def delete_start(self):
		self.delete_pos(0)


	def traverse_list(self):
		curr = self.head
		while curr:
			print (curr.get_data())
			curr = curr.get_next()


if __name__ == '__main__':
	l = List()
	print ('===== data =====')
	for _ in range(5):
		data = random.randint(45, 100)
		print (data, end=" ")
		l.add_start(data)
	print ('\n===== data ends here =====')

	l.traverse_list()

	l.delete_pos(2)

	print ('*' * 45)

	l.traverse_list()
