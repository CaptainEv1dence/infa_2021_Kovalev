import pygame
from pygame.draw import *


def draw_house(x, y, w, h):
    '''
    x, y - the base points are the upper left corner of the house
    w - width of the house
    h - height of the house
    '''
    # house
    polygon(screen, (22, 20, 0), ([x, y + h], [x + w, y + h], [x + w, y], [x, y]))

    # windows
    polygon(screen, (139, 0, 0), (
    [x + (w // 8), y + 4 * (h // 6)], [x + 2 * (w // 8), y + 4 * (h // 6)], [x + 2 * (w // 8), y + 5 * (h // 6)],
    [x + (w // 8), y + 5 * (h // 6)]))
    polygon(screen, (139, 0, 0), (
    [x + 3 * (w // 8), y + 4 * (h // 6)], [x + 4 * (w // 8), y + 4 * (h // 6)], [x + 4 * (w // 8), y + 5 * (h // 6)],
    [x + 3 * (w // 8), y + 5 * (h // 6)]))
    polygon(screen, YELLOW, (
    [x + 5 * (w // 8), y + 4 * (h // 6)], [x + 6 * (w // 8), y + 4 * (h // 6)], [x + 6 * (w // 8), y + 5 * (h // 6)],
    [x + 5 * (w // 8), y + 5 * (h // 6)]))
    polygon(screen, (128, 128, 128),
            ([x + (w // 5), y], [x + 2 * (w // 5), y], [x + 2 * (w // 5), y + (h // 2)], [x + (w // 5), y + (h // 2)]))
    polygon(screen, (128, 128, 128), (
    [x + 3 * (w // 5), y], [x + 4 * (w // 5), y], [x + 4 * (w // 5), y + (h // 2)], [x + 3 * (w // 5), y + (h // 2)]))

    # chimney
    polygon(screen, (36, 34, 14),
            ([x + (w // 6), y], [x + 2 * (w // 6), y], [x + 2 * (w // 6), y - h // 4], [x + (w // 6), y - h // 4]))
    polygon(screen, (36, 34, 14), (
    [x + 3 * (w // 6), y], [x + 4 * (w // 6), y], [x + 4 * (w // 6), y - h // 6], [x + 3 * (w // 6), y - h // 6]))

    # roof
    polygon(screen, (0, 30, 0), ([x - (w // 8), y], [x + w + (w // 8), y], [x + w, y - (h // 8)], [x, y - (h // 8)]))

    # balcony
    polygon(screen, (0, 31, 27), (
    [x - (w // 8), y + (h // 2)], [x + w + (w // 8), y + (h // 2)], [x + w + (w // 8), y + (h // 2) + (h // 10)],
    [x - (w // 8), y + (h // 2) + (h // 10)]))

    # fence
    polygon(screen, (0, 31, 27), (
    [x - (w // 8), y + (h // 2)], [x + (w // 25), y + (h // 2)], [x + (w // 25), y + (h // 2) - (h // 10)],
    [x - (w // 8), y + (h // 2) - (h // 10)]))
    polygon(screen, (0, 31, 27), ([x + w + (w // 8) - (h // 10), y + (h // 2)], [x + w + (w // 8), y + (h // 2)],
                                  [x + w + (w // 8), y + (h // 2) - (h // 10)],
                                  [x + w + (w // 8) - (h // 10), y + (h // 2) - (h // 10)]))

    i = 1
    while i < 11:
        polygon(screen, (0, 31, 27), ([x + i * (w // 10), y + (h // 2)], [x + (i + 1) * (w // 10), y + (h // 2)],
                                      [x + (i + 1) * (w // 10), y + (h // 2) - (h // 10)],
                                      [x + i * (w // 10), y + (h // 2) - (h // 10)]))
        i += 2
    polygon(screen, (0, 31, 27), (
    [x - (w // 8), y + (h // 2) - (h // 10)], [x + w + (w // 8), y + (h // 2) - (h // 10)],
    [x + w + (w // 8), y + (h // 2) - (h // 9)], [x - (w // 8), y + (h // 2) - (h // 9)]))


def draw_clouds_1(x, y, h, w):
    ellipse(screen, (40, 40, 40), (x, y, h, w))


def draw_clouds_2(x, y, h, w):
    ellipse(screen, (60, 60, 60), (x, y, h, w))


def draw_clouds_tr(x, y, h, w):  # transparent
    ellipse(cloud_screen, (30, 30, 30), (x, y, h, w))


def draw_ghost(x, y, r, h):
    circle(screen, WHITE, (x, y), r)
    polygon(screen, WHITE, ([x + r, y], [x + r * 1.2, y + h], [x - r * 1.2, y + h], [x - r, y]))
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, WHITE, ((x - r) + R * i, y + h), R)
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, BLACK, ((x - r) + R * i, y + h + R), R)

    # eyes
    ellipse(screen, (0, 191, 255), (x - 0.5 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, (0, 191, 255), (x + 0.25 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, BLACK, (x - 0.50 * r, y - 0.3 * r, r * 0.25, r * 0.25))
    ellipse(screen, BLACK, (x + 0.25 * r, y - 0.3 * r, r * 0.25, r * 0.25))


def draw_ghost_tr(x, y, r, h):  # transparent
    circle(ghost_screen, WHITE, (x, y), r)
    polygon(ghost_screen, WHITE, ([x + r, y], [x + r * 1.2, y + h], [x - r * 1.2, y + h], [x - r, y]))
    for i in range(6):
        R = int(r // (2.5))
        circle(ghost_screen, WHITE, ((x - r) + R * i, y + h), R)
    for i in range(6):
        R = int(r // (2.5))
        circle(ghost_screen, BLACK, ((x - r) + R * i, y + h + R), R)

    # eyes
    ellipse(ghost_screen, (0, 191, 255), (x - 0.5 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(ghost_screen, (0, 191, 255), (x + 0.25 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(ghost_screen, BLACK, (x - 0.50 * r, y - 0.3 * r, r * 0.25, r * 0.25))
    ellipse(ghost_screen, BLACK, (x + 0.25 * r, y - 0.3 * r, r * 0.25, r * 0.25))


pygame.init()

# consts
FPS = 30
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)


# create screens
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)

ghost_screen = pygame.Surface((200, 200))
ghost_screen.set_alpha(180)
ghost_screen.fill(BLACK)
ghost_screen.set_colorkey(BLACK)

cloud_screen = pygame.Surface((400, 400))
cloud_screen.set_alpha(200)
cloud_screen.fill((105, 105, 105))
cloud_screen.set_colorkey((105, 105, 105))

# background
polygon(screen, BLACK, ([0, 150], [400, 150], [400, 400], [0, 400]))
polygon(screen, (105, 105, 105), ([0, 0], [0, 150], [400, 150], [400, 0]))

# moon
circle(screen, WHITE, (350, 50), 20)

draw_house(30, 100, 50, 100)
draw_house(30, 300, 50, 100)
draw_house(100, 200, 100, 150)

draw_clouds_1(200, 20, 250, 30)
draw_clouds_2(150, 50, 140, 40)

draw_house(150, 60, 50, 100)

draw_clouds_2(80, 100, 100, 20)

draw_ghost(300, 150, 30, 20)
draw_ghost(300, 250, 30, 100)

draw_clouds_tr(150, 200, 200, 30)
draw_clouds_tr(50, 150, 100, 30)

screen.blit(cloud_screen, (0, 0))

draw_ghost_tr(40, 40, 30, 30)
screen.blit(ghost_screen, (130, 300))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()