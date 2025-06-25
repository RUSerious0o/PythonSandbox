import pygame
import sys
import prefs

from mario import Mario


def run():
    pygame.init()
    screen = pygame.display.set_mode(prefs.RESOLUTION)
    pygame.display.set_caption(prefs.GAME_CAPTION)

    mario = Mario(screen)

    loop(screen, mario)


def loop(screen: pygame.Surface, mario: Mario):
    while True:
        events()

        screen.fill(prefs.BG_COLOR)
        mario.draw()

        pygame.display.flip()



def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




if __name__ == '__main__':
    run()