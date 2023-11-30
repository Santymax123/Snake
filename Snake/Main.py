# Main.py is currently being used to test that my code works, will eventually be turned into something like Game.py that handles gamestate etc

from GUI import Display
from Board import Board

import pygame
from Square import Square, squareType

GAME_SPEED = 1 # FPS

# Test to make sure GUI is updating
def runGame():
    for x in range(board.getWidth()):
        for y in range(board.getHeight()):
            board.setSquare(x, y, squareType.FOOD)
            game.update()
            clock.tick(1)
            input = game.get_input
            next_square = board.next_square(input)
            board.get_snake().move_snake(next_square)


        




board = Board(10, 10)
game = Display(board)
clock = pygame.time.Clock()
runGame()





