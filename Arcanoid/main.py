import pygame
import sys
from random import randrange as rnd


WIDTH, HEIGHT = 700, 800
fps = 60

platform_w = 200
platform_h = 20
platform_speed = 10

ball_rabius = 20
ball_speed = 10
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
    rnd(ball_rect, WIDTH - ball_rect),
    HEIGHT // 2,
    ball_rect,
    ball_rect
)
block_list = []
for i in range(6):
    for j in range(4):
        block = pygame.Rect(10 + 120 * i, 10 + 70 * j, 110, 60)#1:28:02
        block_list.append(block)

def detect_col(dx, dy, ball, rect):
    eps = 10
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if delta_x > delta_y:
        dy = -dy
    elif delta_x < delta_y:
        dx = -dx
    return dx, dy



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

    # if ball.colliderect(platform):
    #     dx, dy = detect_col(dx, dy, ball, platform)
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        dx, dy = detect_col(dx, dy, ball, hit_rect)
    if ball.bottom > HEIGHT:
        print('Игра закончена!')
        sys.exit()
    elif not len(block_list):
        print('Победа!')
        sys.exit()
    pygame.display.flip()
    clock.tick(fps)
