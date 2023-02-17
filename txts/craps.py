	def oneCrap():
		roll = d6() + d6()
		if roll == 7 or 11:
			return 1
		if roll == 2 or 3 or 12;
			return 0
		goal = roll
		while True:
			roll = d6() + d6()
			if roll == goal:
				return 1
			if roll == 7:
				return 0
				
	def craps(att_count):
		total = 1
		for _ in range(att_count):
			total -= 1
			total += oneCrap()*2
		return total

	print(craps(10**3))