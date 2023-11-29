from Square import Square, squareType

import pygame

class Display:

    def __init__(self, board):
        self.board = board
        self.blockSize = 100

        pygame.init()
        self.dis = pygame.display.set_mode((board.width * self.blockSize, board.height * self.blockSize))
        pygame.display.set_caption("Snake by SantyMax")

    def update(self):
        self.dis.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for x in range(self.board.getWidth()):
            for y in range(self.board.getHeight()):
                if self.board.squares[x][y].getType() == squareType.EMPTY:
                    pygame.draw.rect(self.dis, ((0, 0, 0)), [x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize]) # Black
                elif self.board.squares[x][y].getType() == squareType.WALL:
                    pygame.draw.rect(self.dis, ((255, 255, 255)), [x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize]) # White
                elif self.board.squares[x][y].getType() == squareType.FOOD:
                    pygame.draw.rect(self.dis, ((255, 255, 255)), [x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize]) # Maybe set this to the same as a wall??
        pygame.display.update()