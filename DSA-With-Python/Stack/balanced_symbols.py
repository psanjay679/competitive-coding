closing = ( ')', '}', ']')
opening = ('(', '{', '[')
brackets = opening + closing

eq = {
	'(': ')',
	'[': ']',
	'{': '}'
}

def balanced_symbols(line):
	stack = list()
	is_balanced = True
	for c in line:
		if c not in brackets: continue
		elif c in opening: stack.append(c)
		elif c in closing:
			paren = stack.pop()
			# print 'paren', paren
			if c != eq[paren]:
				is_balanced = False
				break
	is_balanced = is_balanced and not len(stack)
	return is_balanced

symbols = [
	'(A+B)+(C-D)',
	'((A+B)+(C-D)',
	'((A+B)+[C-D])',
	'((A+B)+[C-D]}'
]

for symbol in symbols:
	print symbol, balanced_symbols(symbol)