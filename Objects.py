import pygame
from pygame.locals import *
import os
import Buttons
import math

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
        self.size=(0,0)

    def position(self):
        "Return the position of the object"
        return self.pos
    
    def size(self):
        "Return the size of the object"
        self.size=(self.image[0].get_height(),self.image[0].get_width())

    def load_image(self,path_image):
        "Load an image from a privte file present in a subdirectory"
        path=os.getcwd()+path_image     
        self.image.append(pygame.image.load(path).convert_alpha())

    def move(self):
        "Move the object"
        self.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        #screen.blit(self.image[0], self.pos)

    def draw(self):
        self.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        screen.blit(self.image[0], self.pos)


class Laser(Object):
    "Laser object"
    def __init__(self, pos=(0,0), current=0):
        Object.__init__(self, pos, current)
        self.pathIm="\Photos_Materiel\laser.png"
        self.load_image(self.pathIm)
    
class Flat_mirror(Object):
    "Mirror object"
    def __init__(self, pos=(0,0), current=0):
        Object.__init__(self, pos, current)
        self.pathIm="\Photos_Materiel\lat_mirror.jpg"
        self.load_image(self.pathIm)

class Curve_mirror(Object):
    "Mirror object"
    def __init__(self, pos=(0,0), current=0):
        Object.__init__(self, pos, current)
        self.pathIm="\Photos_Materiel\curve_mirror.jpg"
        self.load_image(self.pathIm)

class Beam_splitter(Object):
    "Beam splitter object"
    def __init__(self, pos=(0,0), current=0):
        Object.__init__(self, pos, current)
        self.pathIm="\Photos_Materiel\eam_splitter.png"
        self.load_image(self.pathIm)

list_buttons=[Buttons.Button("Laser",(10, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Laser()),
Buttons.Button("Flat Mirror",(100, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Flat_mirror()),
Buttons.Button("Beam Splitter",(230, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Beam_splitter()),
Buttons.Button("Curve Mirror",(400, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Curve_mirror())]


def select_object(o_elements,x,y):
    for e in o_elements:
        if e.position()[0]<=x<=e.position()[0]+e.size[0] and e.position()[1]<=y<=e.position()[1]+e.size[1]:
            print("Trouvé!!")
            return e


pygame.display.flip()
running = True
selected_object = None
optical_elements = []
while running:
    for b in list_buttons:
        screen.blit(b.surface, b.position())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for b in list_buttons:
            if event.type == b.click(event):
                print(b.optical_element())
                optical_elements.append(b.optical_element())
                print(optical_elements)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX,mouseY)=pygame.mouse.get_pos()
            selected_object = select_object(optical_elements, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_object = None
    
    if selected_object:
        selected_object.move()

    pygame.display.update()
        