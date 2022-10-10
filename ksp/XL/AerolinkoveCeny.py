def main(setup, flightsRaw):
	setup = setup.split(' ')
	flights = []
	flightCount = int(setup[1])
	airportCount = int(setup[0])
	flightsComp = ''
	for i in range(flightCount):
		flight = flightsRaw[i].split(' ')
		flights.append(flight)
		flightsComp += flight[0] + flight[1]

	counts = [0 for num in range(airportCount)]  # counts[portIndex] = portMentions

	for num in flightsComp:
		counts[int(num)] += 1

	largestCount = 0
	orderedPorts = []
	for airportMentions in range(airportCount):
		if len(orderedPorts) == airportCount:
			break
		for airportIndex in range(airportCount):
			if airportMentions == counts[airportIndex]:
				orderedPorts.append(airportIndex)

	profit = 0
	for cost in range(1, airportCount + 1):
		profit += cost * (counts[orderedPorts[cost - 1]])

	# print(flights)
	# print(flightsComp)
	# print(counts)
	return profit


if __name__ == '__main__':
	mSetup = input()
	raw = []
	for i in range(int(mSetup[2])):
		raw.append(input())
	print(main(mSetup, raw))
