class SudokuBoard:
	def __init__(self, setup):
		self.board = setup

		self.size = len(setup)
		
		self.potentials = [[[] for _ in range(self.size)] for _ in range(self.size)]

		self.unsolved = []
		for x in range(self.size):
			for y in range(self.size):
				if self.get_cell([x,y]) == 0:
					self.unsolved.append([x,y])
					
		for cell in self.unsolved:
			self.potentials[cell[1]][cell[0]] = [True for _ in range(self.size)]

	def get_cell(self, pos):
		return self.board[pos[1]][pos[0]]
	
	def get_potential(self, pos):
		return self.potentials[pos[1]] [pos[0]]
	
	def list_potentials(self, pos):
		# converts the T/F list to a list of included nums
		potentialList = []
		potential = self.get_potential(pos)
		for numIndex in range(self.size):
			if potential[numIndex]:
				potentialList.append(numIndex+1)
		return potentialList
	
	def remove_potential(self, pos, potential_num):
		potential_list = self.get_potential(pos)
		if not potential_list:
			return
		self.get_potential(pos)[potential_num-1] = False
		
	def check_row(self, pos):
		row = pos[0]
		definiteNums = []
		for cellIndex in range(self.size):
			cell = self.get_cell([row, cellIndex])
			if cell == 0:
				continue
			definiteNums.append(cell)
		for num in definiteNums:
			self.remove_potential(pos, num)
	
	def check_col(self, pos):
		col = pos[1]
		definiteNums = []
		for cellIndex in range(self.size):
			cell = self.get_cell([cellIndex, col])
			if cell == 0:
				continue
			definiteNums.append(cell)
		for num in definiteNums:
			self.remove_potential(pos, num)
	
	def check_potential(self, pos):
		"""
		Refreshes the list of potentials on a given cell
		"""
		self.check_row(pos)
		self.check_col(pos)
		if self.get_cell(pos) != 0:
			return
		pot_list = self.list_potentials(pos)
		if len(pot_list) == 1:
			self.write_cell(pos, pot_list[0])
			
	def write_cell(self, pos, num):
		self.board[pos[1]][pos[0]] = num
	
	def __str__(self):
		out = str(self.board[0])
		for row in self.board[1:]:
			out += '\n' + str(row)
		return out
	
	def is_potential_unique_in_row(self, row, num):
		finds = []
		for col in range(self.size):
			pos = [col,row]
			potential_truth_list = self.get_potential(pos)
			if potential_truth_list[num-1]:
				finds.append(col)
		if len(finds) == 1:
			foundPos = [finds[0],row]
			self.write_cell(foundPos, num)
			
	def is_potential_unique_in_col(self, col, num):
		finds = []
		for row in range(self.size):
			pos = [col,row]
			potential_truth_list = self.get_potential(pos)
			if potential_truth_list[num-1]:
				finds.append(col)
		if len(finds) == 1:
			foundPos = [col,finds[0]]
			self.write_cell(foundPos, num)
	
	def clear_potentials_in_row(self, row, num):
		for col in range(self.size):
			self.remove_potential([col, row], num)
	
	def clear_potentials_in_col(self, col, num):
		for row in range(self.size):
			self.remove_potential([col, row], num)
	
	def clear_potentials(self, pos):
		cell_num = self.get_cell(pos)
		if cell_num == 0:
			return
		self.clear_potentials_in_row(pos[1], cell_num)
		self.clear_potentials_in_col(pos[0], cell_num)

	
	def is_won(self):
		for x in range(self.size):
			for y in range(self.size):
				cell = self.get_cell([x,y])
				if cell == 0:
					return False
		return True
	
	def check_all_potentials(self):
		old = str(self)
		for x in range(self.size):
			for y in range(self.size):
				self.check_potential([x,y])
				self.clear_potentials([x,y])
				self.is_potential_unique_in_row(y)
			self.is_potential_unique_in_col(x)
		new = str(self)
		if new != old:
			self.check_all_potentials()
		