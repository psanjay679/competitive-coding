adj = dict()
adj[1] = [2, 4]
adj[4] = [1]
adj[2] = [1, 3, 5]
adj[3] = [2, 5]
adj[5] = [2, 3]

visited = [False] * 6

def dfs(s):
	if visited[s]: return

	visited[s] = True
	print s
	for node in adj[s]:
		dfs(node)


dfs(1)