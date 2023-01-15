from fifteenSolver import SlideBoard, sign

board = SlideBoard([
	[1,1,2,1,0],
	[1,1,5,1,1],
	[1,1,1,1,1],
	[1,1,1,1,1]
])

def empty_to_pos_new(pos, rel_pos):
	if board.is_at_rel_pos(pos, rel_pos):
		return

	distToPos = [pos[i] - board.emptyPos[i] for i in [0,1]] # dist to pos

	distance = [pos[i] + rel_pos[i] - board.emptyPos[i] for i in [0,1]] # dist to pos+rel_pos

	targetRelPos = [-sign(distToPos[i]) for i in [0, 1]]  # closest point around POS to empty = target

	distToTarget = [distance[i] - rel_pos[i] + targetRelPos[i] for i in [0, 1]]  # dist to this target

	board.multi_swap_new(distToTarget, 1)  # move to target

	difference = [rel_pos[i] - targetRelPos[i] for i in [0, 1]]

	for i in [0,1]:  # if in same row/column
		if difference[i] == 0:
			if difference[1-i] == 0:
				return
			baseCorrection = 'R'
			if i == 1:
				baseCorrection = 'D'
			if pos[i] == board.size[i] -1:
				baseCorrection = SlideBoard.HVInverter(baseCorrection, i)

			correction = ''

			# what exactly is this doing here
			# i would love to know
			if rel_pos[i] == 0:
				board.parse_commands(baseCorrection)
				correction = SlideBoard.HVInverter(baseCorrection, i)
			board.multi_swap_new(difference)
			board.parse_commands(correction)
			return


	if abs(difference[0]) == abs(difference[1]) == 2:
		# if in corner diagonal to rel_pos
		yCorrection = 0
		if pos[1] == board.size[1]-1:
			# go up instead of down if you can't go down
			yCorrection = -2
		board.multi_swap_new([difference[0],1-targetRelPos[1] + yCorrection])
		board.multi_swap_new([0,rel_pos[1] - 1 - yCorrection])
		return

	correction = [0,0]

	for i in [0,1]:
		if pos[i] == board.size[i] - 1:
			# go up instead of down if you can't go down
			correction[i] = -2

	unchanged = 1

	toCorner = [1-targetRelPos[i] + correction[i] for i in [0,1]]

	board.multi_swap_new(toCorner)

	differenceFinal = [pos[i] + rel_pos[i] - board.emptyPos[i] for i in [0, 1]]

	if correction[1] != 0:
		unchanged = 0
	if targetRelPos[1] == 1:
		unchanged = 0


	board.multi_swap_new(differenceFinal, unchanged)

# empty_to_pos_new(board.findNum(5), [-1,0])
board.empty_to_pos(board.findNum(5), [-1,0])

# board.num_to_pos(5, [1,2])
# if board.emptyPos[0] <=
# board.empty_to_pos(board.findNum(5), [0,-1])
board.print_board()