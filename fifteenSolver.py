def sign(x):
	if x == 0:
		return 0
	return abs(x)//x

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

	@staticmethod
	def HVInverter(cmds, verticality):
		inverter = [SlideBoard.invertCmdsHorizontally, SlideBoard.invertCmdsVertically]
		return inverter[verticality](cmds)
	
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

	def multi_swap_new(self, rel_pos, priority = 0):
		# priority = which direction is moved first, in [0,1]
		xMove = rel_pos[0]
		xDir = 0
		if xMove != 0:
			xDir = abs(xMove)//xMove

		yMove = rel_pos[1]
		yDir = 0
		if yMove != 0:
			yDir = abs(yMove)//yMove

		amounts = [abs(xMove), abs(yMove)]
		directions = [[xDir,0], [0,yDir]]

		for order in [priority, 1-priority]:
			for i in range(amounts[order]):
				self.swap_relative(directions[order])

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

	def is_at_rel_pos(self, pos, rel_pos):
		for i in [0,1]:
			if self.emptyPos[i] != pos[i] + rel_pos[i]:
				return False
		return True

	def empty_to_pos(self, pos, rel_pos):
		if self.is_at_rel_pos(pos, rel_pos):
			return

		distToPos = [pos[i] - self.emptyPos[i] for i in [0, 1]]  # dist to pos

		distance = [pos[i] + rel_pos[i] - self.emptyPos[i] for i in [0, 1]]  # dist to pos+rel_pos

		targetRelPos = [-sign(distToPos[i]) for i in [0, 1]]  # closest point around POS to empty = target

		distToTarget = [distance[i] - rel_pos[i] + targetRelPos[i] for i in [0, 1]]  # dist to this target

		self.multi_swap_new(distToTarget, 1)  # move to target

		difference = [rel_pos[i] - targetRelPos[i] for i in [0, 1]]

		for i in [0, 1]:  # if in same row/column
			if difference[i] == 0:
				if difference[1 - i] == 0:
					return
				baseCorrection = 'R'
				if i == 1:
					baseCorrection = 'D'
				if pos[i] == self.size[i] - 1:
					baseCorrection = SlideBoard.HVInverter(baseCorrection, i)

				correction = ''

				# what exactly is this doing here
				# i would love to know
				if rel_pos[i] == 0:
					self.parse_commands(baseCorrection)
					correction = SlideBoard.HVInverter(baseCorrection, i)
				self.multi_swap_new(difference)
				self.parse_commands(correction)
				return

		if abs(difference[0]) == abs(difference[1]) == 2:
			# if diagonal to rel_pos
			yCorrection = 0
			if pos[1] == self.size[1] - 1:
				# go up instead of down if you can't go down
				yCorrection = -2
			self.multi_swap_new([difference[0], 1 - targetRelPos[1] + yCorrection])
			self.multi_swap_new([0, rel_pos[1] - 1 - yCorrection])
			return

		correction = [0, 0]

		for i in [0, 1]:
			if pos[i] == self.size[i] - 1:
				# go up instead of down if you can't go down
				correction[i] = -2

		unchanged = 1

		if correction[1] != 0:
			unchanged = 0

		toCorner = [1 - targetRelPos[i] + correction[i] for i in [0, 1]]

		self.multi_swap_new(toCorner)

		differenceFinal = [pos[i] + rel_pos[i] - self.emptyPos[i] for i in [0, 1]]

		self.multi_swap_new(differenceFinal, unchanged)

	def cycle_vertical(self, cycles):
		direction = abs(cycles)//cycles
		baseCmd = "RUULD"  # UpWARD CYCLE
		if direction == 1: # 1 means Down
			baseCmd = SlideBoard.invertCmdsVertically(baseCmd)
		for cycle in range(abs(cycles)):
			self.parse_commands(baseCmd)
		
	def cycle_right(self, cycle_count):
		# only from the cell directly left of the moved num
		for i in range(cycle_count):
			self.parse_commands("DLLUR")

	def cycle_horizontal(self, cycle_count, direction):
		baseCmd = "DLLUR"  # LeftWARD CYCL
		if direction == 1: # 1 means Right
			baseCmd = SlideBoard.invertCmdsHorizontally(baseCmd)
		for cycle in range(cycle_count):
			self.parse_commands(baseCmd)

	def num_to_pos(self, num, pos):
		if self.findNum(num) == pos:
			return

		if self.findNum(num)[1] == self.size[1]-1:
			self.empty_to_pos(self.findNum(num), [0, -1])
			self.parse_commands("D")

		if self.findNum(num)[0] == self.size[0]-1:
			# reference_pos = [self.findNum(num)[i]-1 for i in [0,1]]
			# self.empty_to_pos(reference_pos, [0, 1])
			self.empty_to_pos(self.findNum(num), [-1, 0])
			self.parse_commands("R")

		yDistToGoal = pos[1] - self.findNum(num)[1]
		#  dir 1 == cycle down
		if yDistToGoal != 0:
			self.empty_to_pos(self.findNum(num), [0, 1])
			self.cycle_vertical(yDistToGoal) # UP

		xDistToGoal = pos[0] - self.findNum(num)[0]
		if xDistToGoal != 0:
			direction = abs(xDistToGoal) // xDistToGoal  # dir 1 == cycle right
			# self.empty_to_pos(self.findNum(num), [-direction, 0])
			# self.cycle_horizontal(abs(xDistToGoal), direction)
			self.empty_to_pos(self.findNum(num), [direction, 0]) # Mucked with this
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

if __name__ == "__main__":
	board = SlideBoard([
			[13,2,3,4],
			[5,6,9,14],
			[0,7,11,15],
			[10,12,8,1]
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
			# board.parse_commands('D')
			if board.get_cell(checkPos) == i-1:
				board.parse_commands("ULDDRULURDDLURULDR")
				continue
			underLast = [board.end_pos(i-1)[0], board.end_pos(i-1)[1]+1]
			board.num_to_pos(i-1, underLast)
			board.parse_commands('RUULD')
			continue

		board.num_to_goal(i)


	# last 2 rows get extra treatment
	# StartIndex is the first index in the last row


	startIndex = (board.size[1]-1)*board.size[0]+1
	endIndex = board.size[0]*board.size[1]
	for i in range(startIndex, endIndex-1):
		board.num_to_pos(i, board.end_pos(i-board.size[0]))
		checkPos = board.end_pos(i)
		# board.parse_commands('D')
		if board.get_cell(checkPos) == i - board.size[0]:
		#   board.parse_commands("ULDDRULURDDLURULDR")
			board.parse_commands("LDRRULDLURRDLULDRU")
			continue
		board.num_to_pos(i-board.size[0], board.end_pos(i-board.size[0]+1))
		board.parse_commands("DLLUR")

	# if we get to a sich like 1243
	#                          xxx0
	# we go
	# URDLDRUULDRDRUULD
	# and we get 1234
	# #          xx0x

	# print('')
	#
	board.print_board()
	#
# print(board.end_pos(5))