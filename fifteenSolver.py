# from math import abs

class slideBoard:
	cmdDict = {
		"U": [0, -1],
		"D": [0, 1],
		"R": [1, 0],
		"L": [-1, 0]
	}
	
	def __init__(self, boardSetup):
		self.board = boardSetup
		self.size = [len(self.board[0]), len(self.board)]
		self.emptyPos = self.findNum(0)
		self.nums = self.size[0] * self.size[1] - 1

	def findNum(self, searched_num):
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				if self.board[y][x] == searched_num:
					return [x,y]
		
	def set_cell(self, pos, num):
		self.board[pos[1]][pos[0]] = num
		
	def get_cell(self, pos):
		return self.board[pos[1]] [pos[0]]
	
	def swap_empty(self, pos):
		self.set_cell(self.emptyPos, self.get_cell(pos))
		self.set_cell(pos, 0)
		self.emptyPos = pos
	
	def multi_swap(self, direction, amount):
		for i in range(amount):
			self.swap_relative(direction)
	def swap_relative(self, relative_pos):
		abs_pos = [relative_pos[i]+self.emptyPos[i] for i in [0,1]]
		self.swap_empty(abs_pos)
	def print_board(self):
		for row in self.board:
			print(row)
			
	def end_pos(self,num):
		num -= 1
		y = num // self.size[0]
		x = num % self.size[0]
		return [x,y]
	
	def empty_to_pos(self,pos, rel_pos):
		if self.emptyPos == [pos[i]+rel_pos[i] for i in [0,1]]:
			return
		# pos = pos of num we are going to be moving
		# rel_pos = where we want to get to relative to pos = the direction we'll be moving the num @ pos in
		if self.emptyPos[1] == pos[1]+rel_pos[1]:
			xDif = pos[0]+rel_pos[0] - self.emptyPos[0]
			direction = [xDif//abs(xDif),0]
			if direction[0] == rel_pos[0]:
				self.swap_relative([0, 1])
				self.multi_swap(direction, abs(xDif))
				self.swap_relative([0, -1])
				return
			else:
				self.multi_swap(direction, abs(xDif))
				return
				
		if self.emptyPos[0] == pos[0]+rel_pos[0]:
			if self.emptyPos[0] == self.size[0]-1:
				self.swap_relative([-1,0])
				self.empty_to_pos(pos, rel_pos)
				return
				
			yDif = pos[1]+rel_pos[1] - self.emptyPos[1]
			direction = [0,yDif//abs(yDif)]
			if direction[1] == rel_pos[1]:
				self.swap_relative([1, 0])
				self.multi_swap(direction, abs(yDif))
				self.swap_relative([-1, 0])
				return
			else:
				self.multi_swap(direction, abs(yDif))
				return
		
		yDif = pos[1] + rel_pos[1] - self.emptyPos[1]
		direction = [0,yDif // abs(yDif)]
		self.multi_swap(direction, abs(yDif))
		self.empty_to_pos(pos, rel_pos)
		
	def cycle_up(self, cycle_count):
		# only from the cell directly underneath the moved num
		for i in range(cycle_count):
			self.parse_commands('RUULD')
		
	def cycle_right(self, cycleCount):
		# only from the cell directly left of the moved num
		for i in range(cycleCount):
			self.parse_commands("DLLUR")

	def numToGoal(self, num):
		goal = self.end_pos(num)

		if self.findNum(num)[0] == self.size[0]-1:
			self.empty_to_pos(self.findNum(num), [-1, 0])
			self.parse_commands("R")

		if self.findNum(num)[1] == self.size[1]-1:
			self.empty_to_pos(self.findNum(num), [0, -1])
			self.parse_commands("D")

		yDistToGoal = self.emptyPos[1] - goal[1] - 1
		if yDistToGoal > 0:
			self.empty_to_pos(self.findNum(num), [0, 1])
			self.cycle_up(yDistToGoal)

		xDistToGoal = self.emptyPos[0] - goal[0]
		if xDistToGoal > 0:
			self.empty_to_pos(self.findNum(num), [1, 0])
			self.cycle_right(xDistToGoal)
			
	def parse_commands(self, cmds):
		for cmd in cmds:
			self.swap_relative(slideBoard.cmdDict[cmd])
			
	


board = slideBoard([
		[5,7,3],
		[8,0,2],
		[6,4,1]
		] ) 

board.numToGoal(1)
board.numToGoal(2)
board.numToGoal(4)
for i in range(1, board.size[0]*board.size[1]):
	if i % board.size[0] == board.size[0] - 2:
		continue
	if i % board.size[0] == board.size[0]-1:
		board.numToGoal(i)
		if i %

	board.numToGoal(i)

# if we get to a sich like 1243
#                          xx0x
# we go
# LURDLDRUULDRDRUULD
# and we get 1234
# #          xx0x

print('')

board.print_board()

print(board.end_pos(5))