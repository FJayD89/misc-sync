from math import atan, cos, sin
import matplotlib.pyplot
import matplotlib.pyplot as plt


class System:
	mass_2 = 2
	gravAccel = 9.81
	pos_x = 0
	pos_y = 1
	alpha = 0
	accel_x = 0
	accel_y = 0
	veloc_x = 0
	veloc_y = 0

	def __init__(self, dt = 10**(-3), grav_accel = 9.81):
		self.dt = dt
		self.gravAccel = grav_accel

	def updateAccel(self):
		self.accel_x = self.gravAccel * cos(self.alpha)
		self.accel_y = self.gravAccel * -sin(self.alpha)

	def updateSpeed(self):
		self.veloc_x += self.dt * self.accel_x
		self.veloc_y += self.dt * self.accel_y

	def updatePos(self):
		self.pos_x += self.dt * self.veloc_x
		self.pos_y += self.dt * self.veloc_y
		self.alpha = atan(self.pos_x/self.pos_y)

	def makeState(self):
		posList = [self.pos_x, self.pos_y]
		return posList

	def printState(self):
		posList = [self.pos_x, self.pos_y]
		print(posList)

	def timeStep(self):
		self.updateAccel()
		self.updateSpeed()
		self.updatePos()

testSystem = System(5*10**-4)

states = []

for _ in range(1000):
	states.append(testSystem.makeState())
	testSystem.timeStep()

xPosList = [pos[0] for pos in states]
yPosList = [pos[1] for pos in states]
print(xPosList)
fig, posChart = plt.subplots()
posChart.plot(xPosList, yPosList, 'o', color = 'tab:brown')

circle2 = plt.Circle((0, 0), 1, color='blue')

posChart.add_patch(circle2)

plt.show()