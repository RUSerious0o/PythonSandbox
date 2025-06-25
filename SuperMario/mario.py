import pygame


class Mario(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        super(Mario, self).__init__()

        self.screen = screen
        self.image = pygame.image.load('images/mario.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
