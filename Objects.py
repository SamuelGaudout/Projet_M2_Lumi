import pygame
from pygame.locals import *
import os


TYPE_LASER=0
TYPE_FLAT_MIRROR=1
TYPE_CURVE_MIRROR=2
TYPE_BEAM_SPLITTER=3
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




class Beam():
    "Create the beam for the different optical elements"
    def __init__(self,scr,object_list=None):
        self.screen=scr
        self.object_list=object_list
        #self.dirs=utils.Stack()
        self.laser_list=[]

    def fill_laser_list(self):
        "Fill the laser list with the laser objects"
        for l in self.object_list:
            if l.type==TYPE_LASER:
                self.laser_list.append(l)

    def beam_lines(self,color):
        "Draw the beam lines"
        if color=='red':
            color=(250,0,0)
        elif color=='erase':
            color=background_colour
        self.fill_laser_list()
        if len(self.laser_list) !=0:
            for l in self.laser_list:
                start_pos=(l.position()[0],l.position()[1]+l.size[0]/2)
                end_pos=(l.position()[0]-1000,l.position()[1]+l.size[0]/2)
                pygame.draw.line(self.screen, color, start_pos, end_pos, 2)





class Laser(Object):
    "Laser object"
    def __init__(self,scr,pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\laser.png"
        self.load_image(self.pathIm)
        self.type=TYPE_LASER
    
class Flat_mirror(Object):
    "Mirror object"
    def __init__(self,scr, pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\lat_mirror.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_FLAT_MIRROR

class Curve_mirror(Object):
    "Mirror object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\curve_mirror.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_CURVE_MIRROR

class Beam_splitter(Object):
    "Beam splitter object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\eam_splitter.png"
        self.load_image(self.pathIm)   
        self.type=TYPE_BEAM_SPLITTER     