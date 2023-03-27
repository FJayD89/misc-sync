class SudokuBoard:
	def __init__(self, setup):
		self.board = setup

		self.size = [0,0]
		self.size[0] = len(setup[0])
		self.size[1] = len(setup)

		self.unsolved = []
		for x in range(self.size[0]):
			for y in range(self.size[1]):
				if self.get_cell([x,y]) == 0:
					self.unsolved.append([x,y])

	def get_cell(self, pos):
		return self.board[pos[1]][pos[0]]

	def get_cell_potentials(self, pos):
		
