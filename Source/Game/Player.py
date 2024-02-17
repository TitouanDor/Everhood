import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pv, name, sprite) -> None:
        super().__init__()
        self.position = 3
        self.pv = pv
        self.name = name
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

        def getName(self): 
            return self.name

        def degat(self, d):
            self.pv -= d


        

    
