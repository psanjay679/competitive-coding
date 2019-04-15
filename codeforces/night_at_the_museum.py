import string

dt = dict()

for i, c in enumerate(string.ascii_lowercase):
	dt[c] = i

s = raw_input().strip()

rots = 0
last_char = 'a'
for c in s:
	rot = min(abs(ord(last_char) - ord(c)), 26 - abs(ord(c) - ord(last_char)))
	rots += rot
	last_char = c

print rots