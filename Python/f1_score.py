import math

def snt(n):
	if n == 1 or n == 0: return False
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

cnt = 0
i = 2
while cnt < 10:
	if snt(i):
		print(i, end=" ")
		cnt += 1
	i += 1

