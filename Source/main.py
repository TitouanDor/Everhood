import pygame

#####fonction#####


def draw():
    win.fill((0,0,0))
    pygame.display.update()


#####porgramme#####
    

#region definition variable
displayY = 576
displayX = 1000

loop = True

pygame.init()

win = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("UUC-G")
#endregion

while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: loop = False
    
    draw()


pygame.quit()