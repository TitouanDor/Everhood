import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pv, name, sprite, displayY, displayX) -> None:
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.tupleX = (displayX//2-(displayX//20)*4 - self.rect.width//2,
                       displayX//2-(displayX//20)*2 - self.rect.width//2,
                       displayX//2 - self.rect.width//2,
                       displayX//2+(displayX//20)*2 - self.rect.width//2,
                       displayX//2+(displayX//20)*4 - self.rect.width//2,
                       displayX//2+(displayX//20)*5,
                       )
        self.position = 3
        self.cooPos = [(self.tupleX[0], displayY - self.rect.height), 
                       (self.tupleX[1], displayY - self.rect.height), 
                       (self.tupleX[2], displayY - self.rect.height), 
                       (self.tupleX[3], displayY - self.rect.height), 
                       (self.tupleX[4], displayY - self.rect.height)
                       ]
        self.rect.x = self.cooPos[self.position - 1][0]
        self.rect.y = self.cooPos[self.position - 1][1]
        self.pv = pv
        self.name = name
        

    def degat(self, d):
        self.pv -= d

    def chang_pos(self, new_pos):
        self.position = new_pos
        self.rect.x = self.cooPos[self.position - 1][0]
        self.rect.y = self.cooPos[self.position - 1][1]


        

    
