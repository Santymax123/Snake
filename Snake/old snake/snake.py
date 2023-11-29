import pygame
from time import sleep
import random

# Game variables that chan be changed for larger board or faster gamespeed
WINDOW_HEIGHT = 400
WINDOW_LENGTH = 400
BLOCK_SIZE = 20
GAME_SPEED = 5

# Colour variables to easy call
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Initialises display then loops till game is over
def main():
    pygame.init()
    dis = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_LENGTH))
    pygame.display.set_caption('Snake project')

    gameLoop(dis)
    gameLose(dis)
    


# Handles all game logic
def gameLoop(dis):
    
    x = WINDOW_LENGTH / 2
    y = WINDOW_HEIGHT / 2

    xChange = 0
    yChange = 0

    foodX = random.randrange(0, WINDOW_LENGTH, BLOCK_SIZE)
    foodY = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)

    # Clock regulates game speed
    clock = pygame.time.Clock()

    # Loop will continue till game is over
    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -BLOCK_SIZE
                    yChange = 0
                elif event.key == pygame.K_RIGHT:
                    xChange = BLOCK_SIZE
                    yChange = 0
                elif event.key == pygame.K_UP:
                    xChange = 0
                    yChange = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    xChange = 0
                    yChange = BLOCK_SIZE
        
        x += xChange
        y += yChange

        if x == WINDOW_LENGTH or x == 0 or y == WINDOW_HEIGHT or y == 0:
            gameOver = True

        dis.fill(WHITE)
        pygame.draw.rect(dis, BLUE, [x, y, BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(dis, RED, [foodX, foodY, BLOCK_SIZE, BLOCK_SIZE])
        drawGrid(dis)
        pygame.display.update()

        if x == foodX and y == foodY:
            #snakeList.append
            print("yummy")

        clock.tick(GAME_SPEED)

# Displays lose message on game end
def gameLose(dis):
    message("You Lost", dis)
    pygame.display.update()
    sleep(2)
    pygame.quit()
    quit()

# Draws the grid we play on
def drawGrid(dis):
    for x in range(0, WINDOW_LENGTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            block = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(dis, BLACK, block, 1)

# Wipes screen and writes text to screen
def message(msg, dis):
    dis.fill(WHITE)
    msg = pygame.font.SysFont(None, BLOCK_SIZE).render(msg, True, RED)
    dis.blit(msg, [WINDOW_LENGTH/2, WINDOW_HEIGHT/2])



main()


#https://www.youtube.com/watch?v=tjQIO1rqTBE
#https://johnflux.com/2015/05/02/nokia-6110-part-3-algorithms/