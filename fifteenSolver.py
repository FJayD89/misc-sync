# from math import abs



class SlideBoard:
	cmdDict = {
		"U": [0, -1],
		"D": [0, 1],
		"R": [1, 0],
		"L": [-1, 0]
	}
	horizInverter = {
		"U": 'U',
		"D": 'D',
		"R": 'L',
		"L": 'R'
	}
	verticInverter = {
		"U": 'D',
		"D": 'U',
		"R": 'R',
		"L": 'L'
	}


	@staticmethod
	def invertCmdsHorizontally(cmds):
		newCommand = ''
		for cmd in cmds:
			newCommand += SlideBoard.horizInverter[cmd]
		return newCommand

	@staticmethod
	def invertCmdsVertically(cmds):
		newCommand = ''
		for cmd in cmds:
			newCommand += SlideBoard.verticInverter[cmd]
		return newCommand
	
	def __init__(self, board_setup):
		self.board = board_setup
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
		
	def cycle_right(self, cycle_count):
		# only from the cell directly left of the moved num
		for i in range(cycle_count):
			self.parse_commands("DLLUR")

	def cycle_horizontal(self, cycle_count, direction):
		baseCmd = "DLLUR"  # LeftWARD CYCL
		if direction == 1:
			baseCmd = SlideBoard.invertCmdsHorizontally(baseCmd)
		for cycle in range(cycle_count):
			self.parse_commands(baseCmd)

	def num_to_pos(self, num, pos):
		if self.findNum(num) == pos:
			return

		if self.findNum(num)[0] == self.size[0]-1:
			self.empty_to_pos(self.findNum(num), [-1, 0])
			self.parse_commands("R")

		if self.findNum(num)[1] == self.size[1]-1:
			self.empty_to_pos(self.findNum(num), [0, -1])
			self.parse_commands("D")

		yDistToGoal = pos[1] - self.findNum(num)[1]
		#  dir 1 == cycle do
		if yDistToGoal > 0:
			self.empty_to_pos(self.findNum(num), [0, 1])
			self.cycle_up(yDistToGoal)

		xDistToGoal = pos[0] - self.findNum(num)[0]
		if xDistToGoal != 0:
			direction = abs(xDistToGoal) // xDistToGoal  # dir 1 == cycle right
			# self.empty_to_pos(self.findNum(num), [-direction, 0])
			# self.cycle_horizontal(abs(xDistToGoal), direction)
			self.empty_to_pos(self.findNum(num), [direction,0])
			baseCmd = 'R'  # for dierction = 1
			if direction == 1:
				# baseCmd = SlideBoard.invertCmdsHorizontally(baseCmd)
				baseCmd = 'L'
			self.parse_commands(baseCmd)
			self.cycle_horizontal(abs(xDistToGoal)-1, direction)

			
	def parse_commands(self, cmds):
		for cmd in cmds:
			self.swap_relative(SlideBoard.cmdDict[cmd])

	def index_to_coords(self, index):
		# 1-indexed!!!
		x = index % self.size[0]
		y = index // self.size[0]
		return [x,y]


	def num_to_goal(self, num):
		goal = self.end_pos(num)
		self.num_to_pos(num, goal)


board = SlideBoard([
		[1,2,3,4],
		[5,6,9,14],
		[0,7,11,15],
		[10,12,8,13]
		] )

# board2 = SlideBoard([
# 	[2,1],
# 	[3,0],
# 	[4,5]
# ])

# board2.parse_commands("ULDDRULURDDLURULDR")
# board2.print_board()

# for i in range(1, board.size[0]*board.size[1]):
for i in range(1,(board.size[1]-2)*board.size[0]+1):
	pass
	if board.findNum(i) == board.end_pos(i):
		# skip if already in correct position
		continue
	if (i+1) % board.size[0] == 0:
		# those that will end up in the next to rightmost column get special treatment afterwards
		continue
	if i % board.size[0] == 0:
		board.num_to_pos(i, board.end_pos(i-1))
		checkPos = board.end_pos(i)
		board.parse_commands('D')
		if board.get_cell(checkPos) == i-1:
			board.parse_commands("ULDDRULURDDLURULDR")
			continue
		underLast = [board.end_pos(i-1)[0], board.end_pos(i-1)[1]+1]
		board.num_to_pos(i-1, underLast)
		board.parse_commands('DRRUULD')
		continue

	board.num_to_goal(i)
# last 2 rows get extra treatment
# StartIndex is the first index in the last row
startIndex = (board.size[1]-1)*board.size[0]+1
endIndex = board.size[0]*board.size[1]
for i in range(startIndex, endIndex-1):
	board.num_to_pos(i, board.end_pos(i-board.size[0]))
	checkPos = board.end_pos(i)
	board.parse_commands('D')
	if board.get_cell(checkPos) == i - 1:
	#   board.parse_commands("ULDDRULURDDLURULDR")
		board.parse_commands("LDRRULDLURRDLULDRU")
		continue
	board.num_to_pos(i-1, board.end_pos(i-board.size[0]-1))
	board.parse_commands("DLLUR")

# if we get to a sich like 1243
#                          xxx0
# we go
# URDLDRUULDRDRUULD
# and we get 1234
# #          xx0x

print('')

board.print_board()

print(board.end_pos(5))