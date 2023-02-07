import pygame
from pygame.locals import *
import os


TYPE_LASER=0
TYPE_FLAT_MIRROR=1
TYPE_CURVE_MIRROR=2
TYPE_BEAM_SPLITTER=3
TYPE_FIBRE=4
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
    
    def beam_line_objects(self,laser,object,color=(250,0,0)):
        end_pos=(object.position()[0]+laser.size[1]/2,laser.position()[1]+laser.size[0]/2)
        pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
        start_pos=end_pos
        object.action_beam(end_pos[0],end_pos[1])


    def beam_lines_laser(self,color):
        "Draw the beam lines"
        if color=='red':
            color=(250,0,0)
        elif color=='erase':
            color=background_colour
        self.fill_laser_list()
        if len(self.laser_list) !=0:
            for l in self.laser_list:
                start_pos=(l.position()[0],l.position()[1]+l.size[0]/2)
                for i in range(len(self.object_list)):
                    if self.object_list[i].type!=TYPE_LASER:
                        if self.object_list[i].position()[1]<l.position()[1]+l.size[0]/2<self.object_list[i].position()[1]+self.object_list[i].size[0] and self.object_list[i].type!=TYPE_LASER:
                            end_pos=(self.object_list[i].position()[0]+self.object_list[i].define_size()[1],l.position()[1]+l.size[0]/2)
                            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
                            self.object_list[i].action_beam(beamxIn=end_pos[0],beamyIn=end_pos[1],color=color)
                            start_pos=end_pos
                            for j in range(i+1,len(self.object_list)):
                                if self.object_list[i].type!=TYPE_LASER:
                                    pass
                            
                        else :
                            end_pos=(l.position()[0]-1000,l.position()[1]+l.size[0]/2)
                            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
                            start_pos=end_pos

    




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
        self.pathIm="\Photos_Materiel\lat_mirror7.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_FLAT_MIRROR
    
    def action_beam(self,beamxIn,beamyIn,BeamRend=800,color=(250,0,0)):
        "reflect the beam"
        start_pos1=(beamxIn,beamyIn) #star of the beam (to the mirror inside the image)
        start_pos2=(beamxIn-(beamyIn-self.position()[1]),beamyIn) #start position of the reflected beam
        end_pos1=(beamxIn-(beamyIn-self.position()[1]),beamyIn) #end position of the beam (to the mirror inside the image)
        end_pos2=(beamxIn-(beamyIn-self.position()[1]),BeamRend) #end position of the reflected beam
        pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
        pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)



        pass

class Curve_mirror(Object):
    "Mirror object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\curve_mirror.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_CURVE_MIRROR
    def action_beam(self,beamxIn,beamyIn,color=(250,0,0)):
        pass

class Beam_splitter(Object):
    "Beam splitter object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\eam_splitter.png"
        self.load_image(self.pathIm)   
        self.type=TYPE_BEAM_SPLITTER

    def action_beam(self,beamxIn,beamyIn,BeamTRend=0,BeamRend=0, color=(250,0,0)):
        "Split the beam in two"
        start_pos1=(beamxIn,beamyIn) #start position of the transmitted beam
        start_pos2=(beamxIn+(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]-self.define_size()[0]),beamyIn) #start position of the reflected beam
        end_pos1=(BeamTRend,beamyIn) #end position of the transmitted beam
        end_pos2=(beamxIn+(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]-self.define_size()[0]),BeamRend) #end position of the reflected beam
        pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
        pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)

class Fiber(Object):
    "Fibre object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\ibre1.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_FIBRE

    def action_beam(self,beamxIn,beamyIn,BeamRend=0,color=(250,0,0)):
        "Stop the beam"
        pass
        
