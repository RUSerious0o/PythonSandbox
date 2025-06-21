import pygame
import sys
import time

from gun import Gun
from bullet import Bullet
from alien import Alien
from stats import Stats
from scores import Scores

def aliens_check(stats, screen, gun, aliens, bullets):
    """проверка, добралась ли армия до края"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break



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
        stats: Stats, scores: Scores, gun: Gun,
        aliens: pygame.sprite.Group,
        bullets: pygame.sprite.Group
):
    """обновление экрана"""
    screen.fill(bg_color)
    scores.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(screen: pygame.Surface, stats: Stats, scores: Scores, aliens: pygame.sprite.Group, bullets: pygame.sprite.Group):
    """обновлять позиции пуль"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        scores.image_score()
        check_high_score(stats,scores)
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def gun_kill(stats, screen, gun, aliens, bullets):
    """столкновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        time.sleep(1)
        gun.create_gun()
    else:
        stats.run_game = False
        sys.exit()

def update_aliens(stats: Stats, screen: pygame.Surface, bullets: pygame.sprite.Group, gun: Gun, aliens: pygame.sprite.Group):
    """обновляем позиции пришельцев"""

    aliens.update()
    # if pygame.sprite.collideany(gun, aliens):
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)
    aliens_check(stats, screen, gun, aliens, bullets)

def check_high_score(stats, scores):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scores.image_high_score()
