import pygame
import sys
from random import randrange as rnd


WIDTH, HEIGHT = 700, 800
fps = 60

platform_w = 200
platform_h = 30
platform_speed = 5

ball_rabius = 20
ball_speed = 5
ball_rect = int(ball_rabius * 2 ** 0.5)
dx, dy = -1, -1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")
clock = pygame.time.Clock()

platform = pygame.Rect(
    WIDTH // 2 - platform_w // 2,
    HEIGHT - platform_h - 10,
    platform_w,
    platform_h
)

ball = pygame.Rect(
    rnd(ball_rect, WIDTH - ball_rect ),
    HEIGHT // 2,
    ball_rect,
    ball_rect
)
block_list = []
for i in range(10):
    for j in range(4):
        block = pygame.Rect(10 + 120 * i, 10 + 70 * j, 110, 60)#1:28:02
        block_list.append(block)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill('black')

    pygame.draw.rect(screen, pygame.Color(180, 187, 193), platform)
    pygame.draw.circle(screen, pygame.Color(225, 225, 225), ball.center, ball_rabius)
    for block in block_list:
        pygame.draw.rect(screen, pygame.Color('pink'), block)


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and platform.left > screen.get_rect().left:
        platform.left -= platform_speed
    if key[pygame.K_RIGHT] and platform.right < screen.get_rect().right:
        platform.right += platform_speed

    if ball.top <= screen.get_rect().top:
        dy = 1

    if ball.right >= screen.get_rect().right:
        dx = -1

    if ball.left <= screen.get_rect().left:
        dx = 1

    if ball.colliderect(platform):
        dy = -1

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy


    pygame.display.flip()
    clock.tick(fps)
