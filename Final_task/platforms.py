from pygame.sprite import Sprite
from pygame.image import load


class Platform (Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("images/platforms/2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform2 (Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("images/platforms/1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin (Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("images/platforms/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
