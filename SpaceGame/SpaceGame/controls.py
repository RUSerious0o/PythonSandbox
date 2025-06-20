import pygame
import sys

from gun import Gun
from bullet import Bullet
from alien import Alien


def create_army(screen: pygame.Surface, aliens: pygame.sprite.Group):
    """создание армии пришельцев"""
    def_alien = Alien(screen)
    alien_width = def_alien.rect.width

    vertical_padding = horizontal_padding = 80
    horizontal_margin = alien_width * 0.3
    aliens_count = int((screen.get_rect().width - 2 * horizontal_padding) // (alien_width + horizontal_margin))
    rows_count = 5

    for j in range(rows_count):
        y = vertical_padding + (alien_width + horizontal_margin) * j

        for i in range(aliens_count):
            alien = Alien(screen)

            alien.x = horizontal_padding + (alien_width + horizontal_margin) * i
            alien.rect.x = alien.x
            alien.y = alien.rect.y = y

            aliens.add(alien)

def events(screen: pygame.Surface, gun: Gun, bullets: pygame.sprite.Group):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            if event.key == pygame.K_a:
                gun.mleft = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False

def update_screen(
        bg_color: tuple,
        screen: pygame.Surface,
        gun: Gun,
        aliens: pygame.sprite.Group,
        bullets: pygame.sprite.Group
):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets: pygame.sprite.Group):
    """обновлять позиции пуль"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_aliens(aliens: pygame.sprite.Group):
    """обновляем позиции пришельцев"""

    aliens.update()

