# Main.py is currently being used to test that my code works, will eventually be turned into something like Game.py that handles gamestate etc

from GUI import Display
from Board import Board

import pygame
from Square import Square, squareType

GAME_SPEED = 1 # FPS

# Test to make sure GUI is updating
def runGame():
    # loop to try get some display updates
    snake_dead = False
    while (not snake_dead):
        # Updates display
        game.update()
        # Waits one second
        clock.tick(GAME_SPEED)
        # 
        input = game.get_input()
        next_square = board.next_square(input)
        board.get_snake().move_snake(next_square)
        if board.get_snake().is_dead():
            game.game_over()
            clock.tick(GAME_SPEED / 2)
            snake_dead = True

            

board = Board(10, 10)
game = Display(board)
clock = pygame.time.Clock()
runGame()
pygame.quit()
quit()

