import pygame
from pygame import Surface

class Gun():

    def __init__(self, screen: Surface):
        self.screen = screen
        self.image = pygame.image.load('images/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """рисование пушки """

        self.screen.blit(self.image, self.rect)
