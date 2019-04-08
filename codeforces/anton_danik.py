n = int(raw_input())
s = raw_input()

a = 0
d = 0

for w in s:
	if w == 'A': a += 1
	else: d += 1

if a > d:
	print('Anton')
elif d > a:
	print ('Danik')
else:
	print ('Friendship')