import pygame
from pygame.locals import *
import os
import Buttons
import math

#création de l'interface graphique avec pygame
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Optics Elements')
background_colour = (200,200,200,0)
screen.fill(background_colour)


class Object:
    "Generic optical element"
    def __init__(self, pos=(0,0), current=0,size=(0,0)):
        self.pos = pos # position of the object
        self.current = current # current through the object
        self.size=size # size of the object
        self.image = [] # image sequence
        

    def position(self):
        "Return the position of the object"
        return self.pos
    
    def define_size(self):
        "Return the size of the object"
        self.size=(self.image[0].get_height(),self.image[0].get_width())
        return self.size

    def load_image(self,path_image):
        "Load an image from a privte file present in a subdirectory"
        path=os.getcwd()+path_image     
        #self.image.append(pygame.image.load(path).convert_alpha())
        self.image.append(pygame.image.load(path))

    def display(self,X,Y):
        "Display the object"
        xrect=self.position()[0]
        yrect=self.position()[1]
        pygame.draw.rect(screen,background_colour,(xrect,yrect,self.size[1],self.size[0]))
        self.pos=(X,Y)
        screen.blit(self.image[0], self.pos)

    def draw(self):
        #self.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
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

optical_elements = []

list_buttons=[Buttons.Button("Laser",(10, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Laser(),object_list=optical_elements),
Buttons.Button("Flat Mirror",(100, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Flat_mirror(),object_list=optical_elements),
Buttons.Button("Beam Splitter",(230, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Beam_splitter(),object_list=optical_elements),
Buttons.Button("Curve Mirror",(400, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Curve_mirror(),object_list=optical_elements)]


def select_object(o_elements,x,y):
    print(optical_elements)
    for e in o_elements:
        print(e.define_size()[0])
        if e.position()[0]<=x<=e.position()[0]+e.define_size()[0] and e.position()[1]<=y<=e.position()[1]+e.define_size()[1]:
            print("Trouvé!!")
            return e


pygame.display.flip()
running = True
selected_object = None

while running:
    for b in list_buttons:
        screen.blit(b.surface, b.position())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for b in list_buttons:
            if event.type == b.click(event):
                pass
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX=pygame.mouse.get_pos()[0]
            mouseY=pygame.mouse.get_pos()[1]
            selected_object = select_object(optical_elements, mouseX, mouseY)
        if event.type == pygame.MOUSEBUTTONUP:
            selected_object = None
    
    

    if selected_object:
        mouseX=pygame.mouse.get_pos()[0]
        mouseY=pygame.mouse.get_pos()[1]
        selected_object.display(mouseX, mouseY)
        

    pygame.display.update()
        