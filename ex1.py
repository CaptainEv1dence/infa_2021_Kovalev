import pygame
from pygame.draw import *

pygame.init()

FPS = 30
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)

circle (screen, YELLOW, ( 200, 200), 100)
circle (screen, RED, ( 150, 170), 20) #eyes
circle (screen, RED, ( 250, 170), 30)
circle (screen, BLACK, ( 150, 170), 5)
circle (screen, BLACK, ( 250, 170), 10)
polygon(screen, BLACK, ([125,140] , [200,150 ], [200, 140], [125, 130])) #eyebrows
polygon(screen, BLACK, ([225,140] , [300,130 ], [300, 145], [225, 155]))
polygon(screen, BLACK, ([150,250] , [250 ,250 ], [250, 270 ], [150, 270])) #rot)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()