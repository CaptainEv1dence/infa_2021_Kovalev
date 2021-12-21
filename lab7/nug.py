import math
from random import choice, randint

import pygame
from pygame.draw import *

FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
G = 10

gunx = 20
guny = 450


class Ball:
    def __init__(self, power, angle, screen: pygame.Surface, x=gunx, y=guny):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0.9 * power * math.cos(angle)
        self.vy = power * math.sin(angle)
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx * 0.1
        self.y += self.vy * 0.1
        self.vy += G * 0.1
        if self.x <= self.r or WIDTH <= self.x + self.r:
            self.vx *= -1
        if self.y <= self.r:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hit_test(self, target):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            target: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (target.x - self.x) ** 2 + (target.y - self.y) ** 2 <= (target.r + self.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.surface = pygame.Surface((120, 10))
        self.f2_power = 0
        self.f2_on = 0
        self.angle = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.f2_power, self.angle, screen)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 0

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and not event.pos[0] == 20:
            self.angle = math.atan2((event.pos[1] - guny), (event.pos[0] - gunx))

    def draw(self):
        self.surface.fill(WHITE)
        new_surface = self.surface
        if self.angle > 0:
            rect(new_surface, self.color, (2, 2, 20 + self.f2_power // 2, 10))
            new_surface = pygame.transform.rotate(new_surface, -self.angle * 180 / math.pi)
            screen.blit(new_surface, (gunx, guny))
        else:
            rect(new_surface, self.color, (2, 2, 20 + self.f2_power // 2, 10))
            new_surface = pygame.transform.rotate(new_surface, -self.angle * 180 / math.pi)
            screen.blit(new_surface, (gunx,
                                      int(guny + 120 * math.sin(self.angle)) + 5 * math.cos(self.angle)))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 75:
                self.f2_power += 3
                self.color = BLACK
            elif 75 <= self.f2_power < 150:
                self.f2_power += 2
                self.color = BLACK
            else:
                self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = randint(300, 780)
        self.y = randint(150, 450)
        self.r = randint(2, 50)
        self.color = RED

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun()
target = Target()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
        b.hit_test(target)
    pygame.display.update()

    for b in balls:
        b.move()
        if b.hit_test(target) and target.live:
            target.live = 0
            target = Target()
    gun.power_up()

pygame.quit()
