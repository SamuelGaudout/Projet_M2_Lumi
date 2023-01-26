import pygame
from pygame.locals import *
import os
import Buttons

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


    def load_image(self,path_image):
        "Load an image from a privte file present in a subdirectory"
        path=os.getcwd()+path_image     
        self.image.append(pygame.image.load(path).convert_alpha())


    def draw(self):

        self.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        screen.blit(self.image[0], self.pos)
        pass


class Laser(Object):
    "Laser object"
    def __init__(self, pos=(0,0), current=0):
        Object.__init__(self, pos, current)
        self.pathIm="\Photos_Materiel\laser.png"
        self.load_image(self.pathIm)
    


l1=Laser()

button1 = Buttons.Button(
    "Laser",
    (10, 10),
    font=30,
    scrn=screen,
    bg="navy",
    feedback="You clicked me")


pygame.display.flip()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            l1.draw()
        button1.click(event)
    screen.blit(button1.surface, (10,10))
        



    pygame.display.update()
        