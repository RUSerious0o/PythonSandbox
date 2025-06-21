import pygame
import sys
from pygame.sprite import Group

from gun import Gun
from controls import events, update_screen, update_bullets, create_army, update_aliens
from alien import Alien
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    aliens = Group()
    create_army(screen, aliens)
    stats = Stats()
    scores = Scores(screen, stats)

    while True:
        events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            update_bullets(screen, stats, scores, aliens, bullets)
            update_aliens(stats, screen, bullets, gun, aliens)
            update_screen(bg_color, screen, stats, scores, gun, aliens, bullets)


if __name__ == '__main__':
    run()
