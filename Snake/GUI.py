# GUI.py Provides visualisation for the game

import pygame

from Square import Square, square_type
from Direction import Direction

# Window/Snake/Block size setter
BLOCK_SIZE = 50


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Display:
    def __init__(self, board):
        self.board = board
        self.display_width = board.width * BLOCK_SIZE
        self.display_height = board.height * BLOCK_SIZE

        # Initiate empty pygame display
        pygame.init()
        self.dis = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Snake by SantyMax")



    # Loops over the entire board and renders each square
    # Should be called once each frame
    def update(self):
        self.dis.fill((0, 0, 0))
        for x in range(self.board.get_width()):
            for y in range(self.board.get_height()):
                if self.board.squares[x][y].get_type() == square_type.EMPTY:
                    pygame.draw.rect(self.dis, (BLACK), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].get_type() == square_type.WALL:
                    pygame.draw.rect(self.dis, (WHITE), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].get_type() == square_type.FOOD:
                    pygame.draw.rect(self.dis, (RED), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].get_type() == square_type.SNAKE:
                    pygame.draw.rect(self.dis, (GREEN), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
        pygame.display.update()



    # Should return the most recent input (or quit)
    def get_input(self):
        input = Direction.NONE
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    input = Direction.UP
                elif event.key == pygame.K_DOWN:
                    input = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    input = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    input = Direction.RIGHT
        return input

        

    def game_over(self):
        self.dis.fill(WHITE)
        message = pygame.font.SysFont(None, 30).render("You Lost!", True, RED)
        self.dis.blit(message, [self.display_width / 3, self.display_height / 2])
        pygame.display.update()
        
