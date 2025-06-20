import pygame
import sys
from pygame.sprite import Group

from gun import Gun
from controls import events, update_screen, update_bullets, create_army, update_aliens
from alien import Alien

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    aliens = Group()
    create_army(screen, aliens)

    while True:
        events(screen, gun, bullets)
        gun.update_gun()
        update_bullets(bullets)
        update_aliens(aliens)
        update_screen(bg_color, screen, gun, aliens, bullets)


if __name__ == '__main__':
    run()