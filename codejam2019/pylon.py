t = int(raw_input())

for testcase in range(t):
	r, c = map(int, raw_input().split())

	dt = dict()
	dt[False] = []
	dt[True] = []
	for i in range(1, r + 1):
		for j in range(1, c + 1):
			dt[False].append((i, j))

	s_poses = dt[False]
	ans = 'POSSIBLE'
	for sr, sc in s_poses:
		# sr, sc = dt[False][0]
		ans = 'POSSIBLE'
		temp_dict = dt.copy()
		nr, nc = sr, sc
		while temp_dict[False]:
			# nr, nc = None, None
			# temp_dict[False].reverse()
			for _r, _c in temp_dict[False]:
				if nr != _r and nc != _c and nr - nc != _r - _c and nr + nc != _r + _c:
					nr, nc = _r, _c
					break

			if (nr, nc) not in temp_dict[False]:
				ans = 'IMPOSSIBLE'
				break
			else:
				temp_dict[False].remove((nr, nc))
				temp_dict[True].append((nr, nc))
		if ans == 'POSSIBLE': break

	print 'Case #{}: {}'.format(testcase + 1, ans)
	if ans == 'IMPOSSIBLE':
		pass
	else:
		for _r, _c in dt[True]:
			print _r, _c
