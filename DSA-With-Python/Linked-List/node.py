class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next

	def has_next(self):
		return self.next != None

class NodeD:
	def __init__(self):
		self.data = None
		self.next = None
		self.prev =  None

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next

	def set_prev(self, prev):
		self.prev = prev

	def get_prev(self):
		return self.prev

	def has_next(self):
		return self.next is not None

	def has_prev(self):
		return self.prev is not None
