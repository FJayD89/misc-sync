# from math import abs

class slideBoard:
	
	def __init__(self, boardSetup):
		self.board = boardSetup
		self.size = [len(self.board[0]), len(self.board)]
		self.emptyPos = self.findNum(0)

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
			self.swap_relative([1, 0])
			self.multi_swap([0, -1], 2)
			self.swap_relative([-1, 0])
			self.swap_relative([0, 1])
		
	def cycle_right(self, cycleCount):
		# only from the cell directly left of the moved num
		for i in range(cycleCount):
			self.swap_relative([0, 1])
			self.multi_swap([-1, 0], 2)
			self.swap_relative([0, -1])
			self.swap_relative([1, 0])
			
	


board = slideBoard([
		[5,2,3],
		[4,0,2],
		[6,4,1]
		] )

# board.print_board()

def numToGoal

goal = board.end_pos(1)

if board.findNum(1)[0] == board.size[0]-1:
	board.empty_to_pos(board.findNum(1), [-1,0])
	board.swap_relative([1,0])

if board.findNum(1)[1] == board.size[1]-1:
	board.empty_to_pos(board.findNum(1), [0,-1])
	board.swap_relative([0,1])

yDistToGoal = board.emptyPos[1] - goal[1] - 1
if yDistToGoal > 0:
	board.empty_to_pos(board.findNum(1), [0,1])
	board.cycle_up(yDistToGoal)

xDistToGoal = board.emptyPos[0]-goal[0]
if xDistToGoal > 0:
	board.empty_to_pos(board.findNum(1), [1,0])
	board.cycle_right(xDistToGoal)


	
# if we get to a sich like 1243
#                          xx0x
# we go
# LURDLDRUULDRDRUULD
# and we get 1234
# #          xx0x

print('')

board.print_board()

print(board.end_pos(5))