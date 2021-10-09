import pygame
from pygame.draw import *
from math import pi as pi


pygame.init()
FPS = 30


#LIST OF COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHTGRAY = (200, 200, 200)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (250, 150, 150)
RED = (255, 0, 0)
BROWN1 = (100, 60, 0)
BROWN2 = (150, 120, 20)
ORANGE = (210, 110, 0)
LIGHTBLUE = (160, 180 , 255)
LLBLUE = (210, 230, 255)
LIGHTGREEN = (160, 250, 100)
COFFEE = (150, 110, 110)


#SCREEN
x1 = 450
y1 = 600
k = 2.3
screen = pygame.display.set_mode((x1, y1))
screen.fill(BROWN1)
rect(screen, BROWN2,(0, y1/k, x1, y1 - (y1/k)))


def window (surface, x, y, width, height):

    '''
    This function draws a window
    :param x: the base point of the upper left corner of the window
    :param y: the base point of the upper left corner of the window
    :param width: width of the window
    :param height: height of the window
    :return: drawn window
    '''

    #main frame
    rect(surface, LLBLUE, (x, y, width, height))

    #glass panels
    rect(surface, LIGHTBLUE, (x + 5, y + 5, (width/2) - 10, (height/3)))
    rect(surface, LIGHTBLUE, (x + width - 5 + 10 - (width/2), y + 5, (width/2) - 10, (height/3)))
    rect(surface, LIGHTBLUE, (x + 5, y + 10 + (height/3), (width/2) - 10, (2*height/3) - 15))
    rect(surface, LIGHTBLUE, (x + width - 5 + 10 - (width/2), y + 10 + (height/3), (width/2) - 10, (2*height/3) - 15))


def ball(surface, x, y, r, color):

    '''
    This function draws a ball of yarn
    :param x: the base point of the center of a ball
    :param y: the base point of the center of a ball
    :param r: the radius of a ball
    :param color: the color of the ball's yarn tail
    :return: drawn ball of yarn
    '''

    #yarn tail
    arc(surface, color, (x, y, 2*r, r/4), 0, pi)
    arc(surface, color, (x + 2*r, y, r, r/4), pi, 2*pi)
    arc(surface, color, (x + 2*r + r, y, 1.5*r, r/4), 0, pi)

    #main body
    circle(surface, GRAY, (x, y), r)
    circle(surface, BLACK, (x, y), r, 1)

    #yarn threads
    arc(surface, BLACK, (x - r/2, y - r/2, r, r/4,), 0, pi)
    arc(surface, BLACK, (x - r/2, y - r/4, r, r/4,), 0, pi)
    arc(surface, BLACK, (x - r/2, y , r, r/4,), 0, pi)
    arc(surface, BLACK, (x - r/2, y - r/2, r/4, r,), 0.5*pi, 1.5*pi)
    arc(surface, BLACK, (x , y - r/2, r/4, r,), 0.5*pi, 1.5*pi)
    arc(surface, BLACK, (x - r/4, y - r/2, r/4, r,), 0.5*pi, 1.5*pi)


def cat (surface, x, y, a, b, color, eyecolor, earcolor):
    #POMOGITE, VITALIY ZAVADSKIY DERZHIT MENIA V ZALOZHNIKAH! YA NE HOCHU PARSIT CHUZHOI KOD V 2 CHASA NOCHI!

    '''
    This function draws a cat
    :param x: x coordinate of the head's center
    :param y: y coordinate of the head's center
    :param a: semi-major axis of a cat
    :param b: semi-minor axis of a cat
    :param color: the color of a cat
    :param eyecolor: the color of a cat's eyes
    :param earcolor: the color of a cat's ears
    :return: drawn cat
    '''

    #leg under the head
    ellipse(surface, color, (x - (a/17), y - (b/18), a/8, b/1.95))
    ellipse(surface, BLACK, (x - (a/17), y - (b/18), a/8, b/1.95), 1)

    #tail
    ellipse(surface, color, (x + a - (a/12.5), y - (b/5), a/2, b/2.5))
    ellipse(surface, BLACK, (x + a - (a/12.5), y - (b/5), a/2, b/2.5), 1)

    #body
    ellipse(surface, color, (x, y - (b/2),  a, b))
    ellipse(surface, BLACK, (x, y - (b/2),  a, b), 1)

    #head
    circle(surface, color, (x, y - (b/26)), b/2.5)
    circle(surface, BLACK, (x, y - (b/26)), b/2.5, 1)

    #legs
    ellipse(surface, color, (x + (a/10), y + (b/4), a/4.2, b/3.8))
    ellipse(surface, BLACK, (x + (a/10), y + (b/4), a/4.2, b/3.8), 1)
    circle(surface, color, (x + a - (a/6.7), y + (a/6.7)), a/6.7)
    circle(surface, BLACK, (x + a - (a/6.7), y + (a/6.7)), a/6.7, 1)
    ellipse(surface, color, (x + a - (a/16), y + (a/6), a/8, b/1.95))
    ellipse(surface, BLACK, (x + a - (a/16), y + (a/6), a/8, b/1.95), 1)

    #eyes
    ellipse(surface, eyecolor, (x - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(surface, BLACK, (x - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5), 1)
    ellipse(surface, eyecolor, (x + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(surface, BLACK, (x + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5),1)
    ellipse(surface, BLACK, (x - b/3.8 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(surface, BLACK, (x + b/3.8 - b/5 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(surface, WHITE, (x - b/3.8 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))
    ellipse(surface, WHITE, (x + b/3.8 - b/5 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))

    #ears
    polygon(surface, PINK,
            [(x - 0.9 * b / 2.5, y - (b / 26) - 0.8 * b / 2.5),
             (x - 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5),
             (x - 0.55 * b / 2.5, y - (b / 26) - 0.7 * b / 2.5)])
    polygon(surface, BLACK,
            [(x - 0.9 * b / 2.5, y - (b / 26) - 0.8 * b / 2.5),
             (x - 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5),
             (x - 0.55 * b / 2.5, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, earcolor, [(x - 0.9 * b / 2.5 - 1, y - (b / 26) - 0.8 * b / 2.5 + 1),
                               (x - 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5 - 1),
                               (x - 0.55 * b / 2.5 + 1, y - (b / 26) - 0.7 * b / 2.5)], 2)
    polygon(surface, PINK,
            [(x + 0.9 * b / 2.5, y - (b / 26) - 0.8 * b / 2.5),
             (x + 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5),
             (x + 0.55 * b / 2.5, y - (b / 26) - 0.7 * b / 2.5)])
    polygon(surface, BLACK,
            [(x + 0.9 * b / 2.5, y - (b / 26) - 0.8 * b / 2.5),
             (x + 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5),
             (x + 0.55 * b / 2.5, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, earcolor, [(x + 0.9 * b / 2.5 - 1, y - (b / 26) - 0.8 * b / 2.5 + 1),
                               (x + 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5 - 1),
                               (x + 0.55 * b / 2.5 + 1, y - (b / 26) - 0.7 * b / 2.5)], 2)

    #nose and mouth
    polygon(surface, BLACK, [(x + 0.9 * b / 2.5 - 1, y - (b / 26) - 0.8 * b / 2.5 + 1),
                            (x + 0.9 * b / 2.5, y - (b / 26) - 0.25 * b / 2.5 - 1),
                            (x + 0.55 * b / 2.5 + 1, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, PINK, [(x, y - b / 26 + 0.4 * b / 2.5), (x - b / 25, y - b / 26 + 0.3 * b / 2.5),
                           (x + b / 25, y - b / 26 + 0.3 * b / 2.5)])
    polygon(surface, BLACK, [(x, y - b / 26 + 0.4 * b / 2.5), (x - b / 25, y - b / 26 + 0.3 * b / 2.5),
                            (x + b / 25, y - b / 26 + 0.3 * b / 2.5)], 1)
    aalines(surface, BLACK, True, [[x, y - b / 26 + 0.4 * b / 2.5], [x, y - b / 26 + 0.55 * b / 2.5]], 1)
    arc(surface, BLACK, (x, y - b / 26 + 0.45 * b / 2.5, 0.2 * b / 2.5, 0.2 * b / 2.5), pi, 2 * pi, 1)
    arc(surface, BLACK, (x - 0.2 * b / 2.5, y - b / 26 + 0.45 * b / 2.5, 0.2 * b / 2.5, 0.2 * b / 2.5), pi, 2 * pi, 1)

    #cat whiskers
    arc(surface, BLACK, (x + 0.25 * b / 2.5, y - b / 26 + 0.4 * b / 2.5, 0.9 * b / 2.5, 0.2 * b / 2.5), pi / 10, pi, 1)
    arc(surface, BLACK, (x + 0.25*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, 6*pi/7, 1)
    arc(surface, BLACK, (x + 0.25*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)
    arc(surface, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.4*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)
    arc(surface, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, 6*pi/7, 1)
    arc(surface, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)


def reverse_cat (surface, x, y, a, b, color, eyecolor, earcolor): # CHERT, ESHE i reverse. AAAAAAAAAAAAAAAA

    '''
    This function draws a reversed cat
    :param x: x coordinate of the head's center
    :param y: y coordinate of the head's center
    :param a: semi-major axis of a cat
    :param b: semi-minor axis of a cat
    :param color: the color of a cat
    :param eyecolor: the color of a cat's eyes
    :param earcolor: the color of a cat's ears
    :return: drawn reversed cat
    '''

    #tail
    ellipse(surface, color, (x - (a/2.5), y - (b/5), a/2, b/2.5))
    ellipse(surface, BLACK, (x - (a/2.5), y - (b/5), a/2, b/2.5), 1)

    #body
    ellipse(surface, color, (x, y - (b/2),  a, b))
    ellipse(surface, BLACK, (x, y - (b/2),  a, b), 1)

    #leg under the head
    ellipse(surface, color, (x + a -(a/17), y - (b/18), a/8, b/1.95))
    ellipse(surface, BLACK, (x + a - (a/17), y - (b/18), a/8, b/1.95), 1)

    #head
    circle(surface, color, (x + a, y - (b/26)), b/2.5)
    circle(surface, BLACK, (x + a, y - (b/26)), b/2.5, 1)

    #legs
    ellipse(surface, color, (x + a/2 + (a/10), y + (b/4), a/4.2, b/3.8))
    ellipse(surface, BLACK, (x + a/2 + (a/10), y + (b/4), a/4.2, b/3.8), 1)
    circle(surface, color, (x + (a/6.7), y + (a/6.7)), a/6.7)
    circle(surface, BLACK, (x + (a/6.7), y + (a/6.7)), a/6.7, 1)
    ellipse(surface, color, (x, y + (a/6), a/8, b/1.95))
    ellipse(surface, BLACK, (x, y + (a/6), a/8, b/1.95), 1)

    #eyes
    ellipse(surface, eyecolor, (x + a - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(surface, BLACK, (x + a - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5), 1)
    ellipse(surface, eyecolor, (x + a + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(surface, BLACK, (x + a + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5),1)
    ellipse(surface, BLACK, (x + a - b/3.8 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(surface, BLACK, (x + a + b/3.8 - b/5 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(surface, WHITE, (x + a - b/3.8 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))
    ellipse(surface, WHITE, (x + a + b/3.8 - b/5 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))

    #ears
    polygon(surface, PINK, [(x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.8 * b / 2.5),
                           (x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5),
                           (x - 0.55 * b / 2.5 + a, y - (b / 26) - 0.7 * b / 2.5)])
    polygon(surface, BLACK, [(x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.8 * b / 2.5),
                            (x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5),
                            (x - 0.55 * b / 2.5 + a, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, earcolor, [(x - 0.9 * b / 2.5 - 1 + a, y - (b / 26) - 0.8 * b / 2.5 + 1),
                               (x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5 - 1),
                               (x - 0.55 * b / 2.5 + 1 + a, y - (b / 26) - 0.7 * b / 2.5)], 2)
    polygon(surface, BLACK, [(x - 0.9 * b / 2.5 - 1 + a, y - (b / 26) - 0.8 * b / 2.5 + 1),
                            (x - 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5 - 1),
                            (x - 0.55 * b / 2.5 + 1 + a, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, PINK, [(x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.8 * b / 2.5),
                           (x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5),
                           (x + 0.55 * b / 2.5 + a, y - (b / 26) - 0.7 * b / 2.5)])
    polygon(surface, BLACK, [(x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.8 * b / 2.5),
                            (x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5),
                            (x + 0.55 * b / 2.5 + a, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, earcolor, [(x + 0.9 * b / 2.5 - 1 + a, y - (b / 26) - 0.8 * b / 2.5 + 1),
                               (x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5 - 1),
                               (x + 0.55 * b / 2.5 + 1 + a, y - (b / 26) - 0.7 * b / 2.5)], 2)

    #nose and mouth
    polygon(surface, BLACK, [(x + 0.9 * b / 2.5 - 1 + a, y - (b / 26) - 0.8 * b / 2.5 + 1),
                            (x + 0.9 * b / 2.5 + a, y - (b / 26) - 0.25 * b / 2.5 - 1),
                            (x + 0.55 * b / 2.5 + 1 + a, y - (b / 26) - 0.7 * b / 2.5)], 1)
    polygon(surface, PINK, [(x + a, y - b / 26 + 0.4 * b / 2.5), (x - b / 25 + a, y - b / 26 + 0.3 * b / 2.5),
                           (x + b / 25 + a, y - b / 26 + 0.3 * b / 2.5)])
    polygon(surface, BLACK, [(x + a, y - b / 26 + 0.4 * b / 2.5), (x - b / 25 + a, y - b / 26 + 0.3 * b / 2.5),
                            (x + b / 25 + a, y - b / 26 + 0.3 * b / 2.5)], 1)
    aalines(surface, BLACK, True, [[x + a, y - b / 26 + 0.4 * b / 2.5], [x + a, y - b / 26 + 0.55 * b / 2.5]], 1)
    arc(surface, BLACK, (x + a, y - b / 26 + 0.45 * b / 2.5, 0.2 * b / 2.5, 0.2 * b / 2.5), pi, 2 * pi, 1)
    arc(surface, BLACK, (x + a - 0.2 * b / 2.5, y - b / 26 + 0.45 * b / 2.5, 0.2 * b / 2.5, 0.2 * b / 2.5), pi, 2 * pi, 1)

    #cat whiskers
    arc(surface, BLACK, (x + a + 0.25*b/2.5, y - b/26 + 0.4*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)
    arc(surface, BLACK, (x + a + 0.25*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, 6*pi/7, 1)
    arc(surface, BLACK, (x + a + 0.25*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)
    arc(surface, BLACK, (x + a - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.4*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)
    arc(surface, BLACK, (x + a - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, 6*pi/7, 1)
    arc(surface, BLACK, (x + a - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), pi/10, pi, 1)


#окна
window(screen, 270, 30, 100, 150)
window(screen, 120, 30, 100, 150)
window(screen, -30, 30, 100, 150)

#шары
ball(screen, 150, y1/k + 40, 20, BROWN2)
ball(screen, 200, 550, 40, LIGHTGRAY)
ball(screen, 100, 500, 20, BROWN2)
ball(screen, 300, 570, 20, BROWN2)
ball(screen, 350, y1/k + 55 + 90, 20, BLACK)
ball(screen, 390, 500, 30, LIGHTGRAY)
ball(screen, 280, y1/k + 180, 30, LIGHTGRAY)

#обратные кошки
reverse_cat(screen, 70, y1/k + 150, 140, 70, COFFEE, LIGHT_BLUE, BROWN1)
reverse_cat(screen, 50, 560, 50, 25, COFFEE, LIGHT_BLUE, BROWN1)
reverse_cat(screen, 370, y1/k + 180, 50, 25, ORANGE, GREEN, BROWN1)
reverse_cat(screen, 50, y1/k + 40, 50, 25, ORANGE, GREEN, BROWN1)

#кошки
cat(screen, 230, y1/k + 60, 140, 70, ORANGE, GREEN, BROWN1)
cat(screen, 270, 500, 50, 25, ORANGE, GREEN, BROWN1)
cat(screen, 350, 550, 50, 25, COFFEE, LIGHT_BLUE, BROWN1)


pygame.display.update()
clock = pygame.time.Clock() #Cock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()