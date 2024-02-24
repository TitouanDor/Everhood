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
displayY -= 70

loop = True
muse = False
toucheGauche = False
toucheDroite = False

color = {
    "black" : (0, 0, 0),
    "white" : (255, 255, 255),
    "red" : (255, 0, 0),
}

sprit = pygame.image.load(os.path.dirname(os.path.abspath(__file__)) + "\\Sprite\\placeholder.png")

player = Player.Player(100, "test", sprit, displayY, displayX)

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

win = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Game")

#endregion

#region musique
if muse:
    pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__)) + "\\SoundTrack\\MEGALOVANIA.mp3")
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play()
#endreion

while loop:


    keys = pygame.key.get_pressed()
    #region mouvement
    if keys[pygame.K_LEFT] and (player.position > 1) and (toucheGauche == False): 
        player.chang_pos(player.position - 1)
        toucheGauche = True

    elif not(keys[pygame.K_LEFT]): 
        toucheGauche = False
        
    if keys[pygame.K_RIGHT] and (player.position < 5) and (toucheDroite == False): 
        toucheDroite = True
        player.chang_pos(player.position + 1)

    elif not(keys[pygame.K_RIGHT]): 
        toucheDroite = False
    #endregion

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: loop = False
    
    draw()


pygame.quit()