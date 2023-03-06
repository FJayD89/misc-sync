def gcd(a,b):
	if a < b:
		a, b = b, a
	while b > 0:
		a, b = b, a % b
	return a

closest = [0, 1]
for j in range(10 ** 6 - 10, 10 ** 6 + 1):  # denominator
	if j == 7:
		continue
	last = [0, 1]
	for i in range(1, j):  # numerator
		if gcd(i, j) == 1:  # if coprime, really slow
			if i / j > 3 / 7:
				if 3 / 7 - last[0] / last[1] < 3 / 7 - closest[0] / closest[1]:
					closest = list(last)
				break
			last = [i, j]

print(closest)
print(3 / 7 - closest[0] / closest[1])