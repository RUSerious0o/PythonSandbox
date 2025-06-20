import pygame
import sys

from gun import Gun
from controls import events

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        events(gun)

        screen.fill(bg_color)
        gun.update_gun()
        gun.output()
        pygame.display.flip()


if __name__ == '__main__':
    run()