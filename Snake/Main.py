# Main.py is currently being used to test that my code works, will eventually be turned into something like Game.py that handles gamestate etc

from GUI import Display
from Board import Board
# Only being used to debug currently
from Square import Square, squareType
import time


# Test to make sure GUI is updating
def testGUI():
    for x in range(board.getWidth()):
        for y in range(board.getHeight()):
            board.setSquare(x, y, squareType.FOOD)
            display.update()
            time.sleep(1)




board = Board(10, 10)
display = Display(board)
display.update()
testGUI()





