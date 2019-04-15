def get_rhyme_words(w1, w2):
	w1 = w1[::-1]
	w2 = w2[::-1]

	rhyme = ''
	for a, b in zip(w1, w2):
		if a != b:
			break
		else:
			rhyme += a

	return rhyme

def main():

	output_fmt = 'Case #{testcase}: {ans}'

	t = int(raw_input())

	for case in range(t):
		n = int(raw_input())
		words = []
		for _ in range(n):
			words.append(raw_input().strip())

		rhymes = dict()
		while len(words):
			w1, w2, r = None, None, ''
			i = 0
			for i in range(len(words)):
				for j in range(i + 1, len(words)):
					rhm = get_rhyme_words(words[i], words[j])
					if len(rhm) > len(r):
						w1, w2, r = words[i], words[j], rhm

			if w1 and w2:
				rhymes[(w1, w2)] = r
				# print w1, w2
				words.remove(w1)
				words.remove(w2)
			else:
				words.remove(words[i])

		count = 2 * len(set(rhymes.values()))

		print output_fmt.format(testcase=case + 1, ans=count)

main()