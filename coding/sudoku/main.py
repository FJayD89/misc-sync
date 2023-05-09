class SudokuBoard:
	def __init__(self, setup, subdiv_size):
		self.board = setup
		self.size = len(setup)

		if self.size % subdiv_size != 0:
			raise ValueError("Section size doesn't divide size!")
		if subdiv_size >= self.size:
			raise ValueError("Section size is too large!")

		self.subdiv_size = [subdiv_size, int(self.size/subdiv_size)]
		# in the x direction
		
		self.potentials = [[[True]*self.size for _ in range(self.size)] for _ in range(self.size)]

		self.unsolved = []
		for x in range(self.size):
			for y in range(self.size):
				if self.get_cell([x,y]) == 0:
					self.unsolved.append([x,y])
					
		for cell in self.unsolved:
			self.potentials[cell[1]][cell[0]] = [True for _ in range(self.size)]

	def get_cell(self, pos):
		return self.board[pos[1]][pos[0]]
	
	def get_potentials(self, pos):
		return self.potentials[pos[1]] [pos[0]]
	
	def list_potentials(self, pos):
		"""
		Converts the T/F list to a list of included nums
		:type pos: list[int]
		"""
		potentialList = []
		potential = self.get_potentials(pos)
		for numIndex in range(self.size):
			if potential[numIndex]:
				potentialList.append(numIndex+1)
		return potentialList
	
	def remove_potential(self, pos, potential_num):
		if self.get_cell(pos) != 0:
			return  # cell already filled
		self.get_potentials(pos)[potential_num - 1] = False
		
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
	
	def refresh_potential(self, pos):
		"""
		Refreshes the list of potentials on a given cell
		"""
		if self.get_cell(pos) != 0:
			return  # already solved
		self.check_row(pos)
		self.check_col(pos)
		if self.get_cell(pos) != 0:
			return
		pot_list = self.list_potentials(pos)
		if len(pot_list) == 1:
			self.write_cell(pos, pot_list[0])
	
	def refresh_all_potentials(self):
		for row in range(self.size):
			for col in range(self.size):
				pos = [row, col]
				self.refresh_potential(pos)
	
	def write_cell(self, pos, num):
		if self.get_cell(pos) != 0:
			return
		self.board[pos[1]][pos[0]] = num
		for potential in range(1, self.size):
			self.remove_potential(pos, potential)
		
	def __str__(self):
		out = str(self.board[0])
		for row in self.board[1:]:
			out += '\n' + str(row)
		return out
	
	def is_potential_unique_in_line(self, statIndex, potential, XorY):
		"""
		If a given potential is only found once in a line, make it the value of the cell it was found in
		"""
		foundIndex = -1  # some original value that can't be attained
		pos = [statIndex, statIndex]
		for dynIndex in range(self.size):
			pos[XorY] = dynIndex
			if self.get_cell(pos) != 0:
				if self.get_cell(pos) == potential:
					return False  # there's already a cell with the searched-for potential, abort
					# todo: rewrite this better so there's less risk of it failing
				continue  # cell already filled, thus has no potentials
			potential_truth_list = self.get_potentials(pos)
			if potential_truth_list[potential-1]:
				if foundIndex != -1:  # we found another one
					return False
				foundIndex = dynIndex
		foundPos = pos
		foundPos[XorY] = foundIndex
		self.write_cell(foundPos, potential)
		return True
		
	def check_potentials_in_line(self, statIndex, XorY):
		for potential in range(1,self.size):
			self.is_potential_unique_in_line(statIndex, potential, XorY)
	
	def clear_potential_in_line(self, statIndex, XorY, num):
		pos = [statIndex, statIndex]
		for dynIndex in range(self.size):
			pos[XorY] = dynIndex
			self.remove_potential(pos, num)
	
	def collect_filled_cells_in_line(self, stat_index, XorY):
		"""
		Returns a list of filled cells in this row
		"""
		collected = []
		pos = [stat_index]*2
		for dyn_index in range(self.size):
			pos[XorY] = dyn_index
			cell = self.get_cell(pos)
			if cell != 0:
				collected.append(cell)
		return collected
	
	def clear_all_potentials(self):
		"""
		Clear potentials across the entire board based on already filled cells in lines
		"""
		for XorY in [0, 1]:
			for stat_index in range(self.size):
				to_clear = self.collect_filled_cells_in_line(stat_index, XorY)
				for potential in to_clear:
					self.clear_potential_in_line(stat_index, XorY, potential)
	
	def is_won(self):
		for x in range(self.size):
			for y in range(self.size):
				cell = self.get_cell([x,y])
				if cell == 0:
					return False
		return True
		
	def check_all_potentials(self):
		for XorY in [0,1]:
			for index in range(self.size):
				self.check_potentials_in_line(index, XorY)
				
	def get_subdivision(self, index):
		"""
		Return a list of all the positions in a given subdivision
		"""
		subdivision = []
		topRight = [index % self.subdiv_size[XorY] for XorY in [0,1]]
		for x_index in range(self.subdiv_size[0]):
			for y_index in range(self.subdiv_size[1]):
				subdivision.append([topRight[0] + x_index, topRight[1] + y_index])
		return subdivision
	
	def solve_cycle(self):
		self.refresh_all_potentials()
		self.check_all_potentials()
		self.clear_all_potentials()
	
	def solve(self):
		oldState = ''  # ew but cba
		while not self.is_won():
			if oldState == str(self):
				print('unsuccessful')
				return
			oldState = str(self)
			self.solve_cycle()
		print("Done")
		return
	
