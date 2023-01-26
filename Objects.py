import pygame
from pygame.locals import *
import sys
import os

#création de l'interface graphique avec pygame
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Optics Elements')
background_colour = (200,200,200)
screen.fill(background_colour)



class Object:
    "Generic optical element"
    def __init__(self, pos=(0,0), current=0):
        self.pos = pos # position of the object
        self.current = current # current through the object
        self.image = [] # image sequence


    def load_image(self):
        "Load an image from a privte file present in a subdirectory"        
        self.image.append(pygame.image.load(os.getcwd()+"\Photos_Materiel\laser.png").convert_alpha())


    def draw(self):

        self.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        screen.blit(self.image[0], self.pos)
        pass

l1=Object()


pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            l1.load_image()
            l1.draw()



    pygame.display.update()
        