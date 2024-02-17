import pygame
from PyQt5.QtWidgets  import* 
import sys
import os

#####fonction#####


def draw():
    win.fill(color["black"])

    for e in coo_ligne_blanche:
        pygame.draw.line(win,color["white"], (displayX//2,displayY//3), e)
    
    
    pygame.display.update()


#####porgramme#####
    
os.system("cls")

#region definition variable
"""app = QApplication(sys.argv)
screen = QApplication.screens()[0]

displayX = screen.size().width()
displayY = screen.size().height()-65"""

loop = True




color = {
    "black" : (0, 0, 0),
    "white" : (255, 255, 255)

}


pygame.init()
displayX, displayY = pygame.display.get_desktop_sizes()[0]

coo_ligne_blanche = [
        (displayX//2-(displayX//20)*5, displayY), 
        (displayX//2-(displayX//20)*3, displayY), 
        (displayX//2-(displayX//20), displayY), 
        (displayX//2+(displayX//20), displayY), 
        (displayX//2+(displayX//20)*3, displayY), 
        (displayX//2+(displayX//20)*5, displayY)
        ]

win = pygame.display.set_mode((displayX, displayY-65))
pygame.display.set_caption("Game")

#endregion

while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: loop = False
    
    draw()


pygame.quit()