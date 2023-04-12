from main import SudokuBoard
from decoder import get_setup

testSetup = get_setup()

testBoard = SudokuBoard(testSetup)

print(testBoard.unsolved)

# print(testBoard)
# print(testBoard.list_potentials(testBoard.unsolved[0]))

print(testBoard)

testBoard.clear_potentials()
print()
print(testBoard)
