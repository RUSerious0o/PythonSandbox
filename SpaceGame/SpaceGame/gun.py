import pygame
from pygame import Surface
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen: Surface):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование пушки """

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.5

        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 0.5

        self.rect.centerx = self.center

    def create_gun(self):
        """размещаем пушку по центру внизу"""
        self.center = self.screen_rect.centerx