import pygame
from pygame.locals import *
import os


background_colour = (200,200,200,0)

class Object:
    "Generic optical element"
    def __init__(self,scr, pos=(0,0), current=0,size=(0,0)):
        self.screen=scr
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
        pygame.draw.rect(self.screen,background_colour,(xrect,yrect,self.size[1],self.size[0]))
        self.pos=(X,Y)
        self.screen.blit(self.image[0], self.pos)

    def draw(self):
        self.screen.blit(self.image[0], self.pos)


class Laser(Object):
    "Laser object"
    def __init__(self,scr,pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\laser.png"
        self.load_image(self.pathIm)
    
class Flat_mirror(Object):
    "Mirror object"
    def __init__(self,scr, pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\lat_mirror.jpg"
        self.load_image(self.pathIm)

class Curve_mirror(Object):
    "Mirror object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\curve_mirror.jpg"
        self.load_image(self.pathIm)

class Beam_splitter(Object):
    "Beam splitter object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\eam_splitter.png"
        self.load_image(self.pathIm)        