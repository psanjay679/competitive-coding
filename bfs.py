from __future__ import print_function
from Queue import Queue
import threading

if __name__ == '__main__':


	adj = dict()

	adj[1] = [2, 4]
	adj[4] = [1]
	adj[2] = [1, 3, 5]
	adj[3] = [2, 6]
	adj[6] = [3, 5]
	adj[5] = [2, 6]

	visited = [False] * 7

	q = Queue()

	s = 1
	q.put(s)
	visited[s] = True
	print (s)
	while not q.empty():
		s = q.get()
		for k in adj[s]:

			if visited[k] == True:
				continue
			visited[k] = True
			print (s, '-->', k)
			q.put(k)

