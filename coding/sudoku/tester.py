from main import SudokuBoard

testSetup = [[1,2,3],
             [2,3,0],
             [3,1,2],
            ]
testBoard = SudokuBoard(testSetup)

print(testBoard.unsolved)
# for i in range(64):
#     print(i)