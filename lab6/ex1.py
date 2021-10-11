import pygame
from random import randint,choice
import math
from pygame.draw import *
import pygame.freetype

# INITI
pygame.init()
pygame.font.init()
FONT = pygame.freetype.Font("comic.ttf", 24)

# consts
FPS = 30
screen = pygame.display.set_mode((600, 600))
COLORS = [(0, 0 , 0), (0, 255 , 255), (255, 0 , 255), (255, 255 , 0), (0, 0 , 255), (0, 255 , 0), (255, 0 , 0)]
WHITE = (255, 255, 255)
SCORE = 0
rings = 3
balls = 12
ring_max_speed = 10

# SHARI
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

        if not (self.y > self.r + 30 and self.y < borders[1]):
            self.v_y = - self.v_y

    def shot(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
            return 100
        else:
            return 0

# KOLCA
class Ring:

    def __init__(self):

        self.v_x = randint(-100, 100)/10
        self.v_y = randint(-100, 100)/10
        self.r2 = randint(30, 40)
        self.r1 = 2 * self.r2 / 3
        self.x = randint(self.r2, 580 - self.r2)
        self.y = randint(self.r2, 580 - self.r2)
        self.color = (255, 0, 0)

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), self.r2)
        circle(surface, WHITE, (self.x, self.y), self.r1)

    def move(self):
        if (abs(self.v_x) < ring_max_speed):
            self.v_x += randint(-100, 100) / 50
        else:
            self.v_x *= 0.5

        if (abs(self.v_y) < ring_max_speed):
            self.v_y += randint(-100, 100) / 50
        else:
            self.v_y *= 0.5

        self.x += self.v_x
        self.y += self.v_y
        

    def collision(self, borders):
        if not (self.x > self.r2 and self.x < borders[0]):
            self.v_x = - self.v_x

        if not (self.y > self.r2 + 30 and self.y < borders[1]):
            self.v_y = - self.v_y

    def shot(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r2 ** 2 and (x - self.x) ** 2 + \
                (y - self.y) ** 2 >= self.r1 ** 2:
            return 100
        else:
            return 0


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# MASSIVI S KOLAMI I SHARAMI
ball_pool = []
ring_pool = []

for i in range(balls):
    ball_pool.append(Ball())
for i in range(rings):
    ring_pool.append(Ring())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            print('BANG!')

            for ball in ball_pool:
                if (ball.shot(event.pos[0], event.pos[1]) == 100):
                    SCORE += 100
                    print(f"SCORE = {SCORE}")
                    print('NICE SHOT!')

            for ring in ring_pool:
                if (ring.shot(event.pos[0], event.pos[1]) == 100):
                    SCORE += 500
                    print(f"SCORE = {SCORE}")
                    print('AMAZING!')

    for ball in ball_pool:
        ball.draw(screen)
        ball.move()
        ball.collision([580, 580])

    for ring in ring_pool:
        ring.draw(screen)
        ring.move()
        ring.collision([580, 580])

    pygame.display.update()
    screen.fill((255, 255, 255))

    # ETO TEXT
    text_surface, rect = FONT.render(f"SCORE = {SCORE}", (0, 0, 0))
    screen.blit(text_surface, (40, 12))


pygame.quit()