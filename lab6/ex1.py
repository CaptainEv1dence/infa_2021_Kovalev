import pygame
from random import randint,choice
import math
from pygame.draw import *
from pygame import event

pygame.init()

#consts
FPS = 30
screen = pygame.display.set_mode((600, 600))
COLORS = [(0, 0 , 0), (0, 255 , 255), (255, 0 , 255), (255, 255 , 0), (0, 0 , 255), (0, 255 , 0), (255, 0 , 0)]
SCORE = 0

class Ball:

    def __init__(self):

        self.v_x = randint(-100, 100)/20
        self.v_y = randint(-100, 100)/20
        self.r = randint(20, 40)
        self.x = randint(self.r, 580 - self.r)
        self.y = randint(self.r, 580 - self.r)
        self.color = choice(COLORS)

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def collision(self, borders):
        if not (self.x > self.r and self.x < borders[0]):
            self.v_x = - self.v_x

        if not (self.y > self.r and self.y < borders[1]):
            self.v_y = - self.v_y

    def shot(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
            return 100
        else:
            return 0


pygame.display.update()
clock = pygame.time.Clock()
finished = False


pool = [Ball()]
for i in range(14):
    pool.append(Ball())


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('BANG!')
            for ball in pool:
                if (ball.shot(event.pos[0], event.pos[1]) == 100):
                    SCORE += 100
                    print(f"SCORE = {SCORE}")
                    print('NICE SHOT!')

    for ball in pool:
        ball.draw(screen)
        ball.move()
        ball.collision([580, 580])

    pygame.display.update()
    screen.fill((255, 255, 255))


pygame.quit()