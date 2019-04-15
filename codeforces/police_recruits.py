n = int(raw_input())

ar = map(int, raw_input().split())

crimes = 0
police = 0

for el in ar:
	if el > 0:
		police += el
	else:
		if police > 0:
			police -= 1
		else:
			crimes += 1

print crimes