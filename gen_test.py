import random
import sys

n = random.randint(50, 100)

print(n)

ar = list()

for i in range(n):
	ar.append(random.randint(100, 200))

ar.sort()

for k in ar:
	print(k, end=" ")

print ()

k = random.randint(200, 300)
print(k)

