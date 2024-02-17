import pygame
import os
import Player

pygame.init()

#####fonction#####


def draw():
    win.fill(color["black"])

    for e in coo_ligne_blanche:
        pygame.draw.line(win,color["white"], (displayX//2,displayY//3), e)
    sprites.draw(win)
    sprites.update()
    pygame.display.update()


#####porgramme#####
    
os.system("cls")

#region definition variable
displayX, displayY = pygame.display.get_desktop_sizes()[0]

loop = True

color = {
    "black" : (0, 0, 0),
    "white" : (255, 255, 255),
    "red" : (255, 0, 0),
}

sp = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "\\Sprite\\placeholder.png")

player = Player.Player(100, "test", sp)

sprites = pygame.sprite.Group()
sprites.add(player)

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

#region musique
pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__)) + "\\SoundTrack\\MEGALOVANIA.mp3")
pygame.mixer.music.set_volume(2)
pygame.mixer.music.play()
#endreion

while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: loop = False
    
    draw()


pygame.quit()