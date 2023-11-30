# GUI.py Provides visualisation for the game
from Square import Square, squareType
import pygame

# Window/Snake/Block size setter
BLOCK_SIZE = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Display to be called after each game logic frame has been finished
class Display:
    def __init__(self, board):
        self.board = board

        # Initiate empty pygame display
        pygame.init()
        self.dis = pygame.display.set_mode((board.width * BLOCK_SIZE, board.height * BLOCK_SIZE))
        pygame.display.set_caption("Snake by SantyMax")

    # Loops over the entire board and renders each square
    # TODO should i instead pass the board object to this function, rather than have the class hold the board?
    def update(self):
        self.dis.fill((0, 0, 0))
        for x in range(self.board.getWidth()):
            for y in range(self.board.getHeight()):
                if self.board.squares[x][y].getType() == squareType.EMPTY:
                    pygame.draw.rect(self.dis, (BLACK), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].getType() == squareType.WALL:
                    pygame.draw.rect(self.dis, (WHITE), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].getType() == squareType.FOOD:
                    pygame.draw.rect(self.dis, (RED), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
                elif self.board.squares[x][y].getType() == squareType.SNAKE:
                    pygame.draw.rect(self.dis, (GREEN), [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
        pygame.display.update()

    # Should return the most recent input (or quit)
    def get_input(self):
        input = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                input = "UP"
            elif event.key == pygame.K_DOWN:
                input = "DOWN"
            elif event.key == pygame.K_LEFT:
                input = "LEFT"
            elif event.key == pygame.K_RIGHT:
                input = "RIGHT"
            else:
                input = "NONE"
        print ("here" + input)
        return