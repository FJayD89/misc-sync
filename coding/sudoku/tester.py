from main import SudokuBoard
from decoder import get_setup, setup

testSetup = setup()

testBoard = SudokuBoard(testSetup, 3)

print(testBoard.unsolved)

# print(testBoard)
# print(testBoard.list_potentials(testBoard.unsolved[0]))

print(testBoard)

print(testBoard.get_subdivision(2))

# testBoard.solve()
# print(testBoard)
# pots = testBoard.list_potentials([5,3])
# print(pots)
