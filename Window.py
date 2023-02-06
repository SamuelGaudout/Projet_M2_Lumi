import pygame
import sys, os
import Buttons
from pygame.locals import *

pygame.init()



# icon_32x32 = pygame.image.load("C:\\Users\\not-a\\Desktop\\Interface\\IMage.png")
icon_32x32 = pygame.image.load(os.getcwd()+"\Photos_Materiel\laser.png")

#Taille fenetre
windowSurface = pygame.display.set_mode((1080, 720), 0, 32)


#création de la fenetre
pygame.display.set_caption('Window')
pygame.display.set_icon(icon_32x32)
pygame.display.set_caption('Application')

#fond de la fenetre
#background = pygame.image.load("C:\\Users\\not-a\\Desktop\\Interface\\IMage.png")
background = pygame.image.load(os.getcwd()+"\Photos_Materiel\laser.png")
background = pygame.transform.scale(background, (1233, 925))
#texte
font = pygame.font.SysFont("Verdana", 72)
font_1= pygame.font.SysFont("Verdana", 48)
font_2= pygame.font.SysFont("Verdana", 32)
text = font.render("Bienvenue sur l'application", True, (255, 255, 255))
text_1= font_1.render("Projet LuMI 22-23", True, (255, 255, 255))
text_2= font_2.render("Gaudout et Hamdad", True, (255, 255, 255))
textRect = text.get_rect()
textRect_1 = text_1.get_rect()
textRect_2 = text_2.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery - 100
textRect_1.centerx = windowSurface.get_rect().centerx
textRect_1.centery = windowSurface.get_rect().centery - 300
textRect_2.centerx = windowSurface.get_rect().centerx
textRect_2.centery = windowSurface.get_rect().centery + 100

pos=(windowSurface.get_rect().centerx - 100,windowSurface.get_rect().centery + 200)

B1=Buttons.Button_Launch("Lancer l'application",pos,font=30,scrn=windowSurface,bg="blue",feedback="Lancement en Cours")


windowSurface.blit(background,(0,-200))
windowSurface.blit(text, textRect)
windowSurface.blit(text_1, textRect_1)
windowSurface.blit(text_2, textRect_2)
windowSurface.blit(B1.surface, (B1.x, B1.y))
pygame.display.flip()


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            windowSurface.blit(B1.surface, (B1.x, B1.y))
        B1.click(event)
    
    pygame.display.update()
