from GUI import Display
from Board import Board
# Only being used to debug currently
from Square import Square, squareType
import time

board = Board(10, 10)
display = Display(board)
display.update()


# Test to make sure GUI is updating
for x in range(board.getWidth()):
    for y in range(board.getHeight()):
        board.setSquare(x, y, squareType.FOOD)
        display.update()
        print("deez")
        time.sleep(1)