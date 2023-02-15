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
        self.direction=0 # direction of the beam   

    def position(self):
        "Return the position of the object"
        return self.pos

    def dir(self):
        "Return the direction of the object"
        return self.direction
    
    def define_size(self):
        "Return the size of the object"
        self.size=(self.image[0].get_height(),self.image[0].get_width())
        return self.size

    def load_image(self,path_image):
        "Load an image from a privte file present in a subdirectory"
        path=os.getcwd()+path_image     
        self.image.append(pygame.image.load(path))
    
    def rotate_object(self,angle=0):
        "Rotate the object"
        self.image[0]=pygame.transform.rotate(self.image[0],angle)
        self.direction+=1

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
        self.laser_list=[]

    def fill_laser_list(self):
        "Fill the laser list with the laser objects"
        for l in self.object_list:
            if l.type==TYPE_LASER:
                self.laser_list.append(l)
    
    def beam_line_objects(self,start_pos,object,dir="left",color=(250,0,0)):
        if dir=="left":
            end_pos=(object.position()[0]+object.define_size()[1],start_pos[1])
        elif dir=="right":
            end_pos=(object.position()[0],start_pos[1])
        elif dir=="up":
            end_pos=(start_pos[0],object.position()[1]+object.define_size()[0])
        elif dir=="down":
            end_pos=(start_pos[0],object.position()[1])
        object.action_beam(end_pos[0],end_pos[1],color=color)

    def check_beam_line(self,laser):
        'Check if the beam line is in an object, meaning that the beam is incountering an object'
        o=0
        object_intercepted=[]
        for i in range(len(self.object_list)):
            if self.object_list[i].type!=TYPE_LASER:
                if self.object_list[i].position()[1]<laser.position()[1]+laser.size[0]/2<self.object_list[i].position()[1]+self.object_list[i].size[0]:
                    o=+1
                    object_intercepted.append(self.object_list[i])
        if o>0:       
            return True,object_intercepted
        else:
            return False,None

    def object_order_beam(self,laser):
        'Order of the objects in the beam line coming from the laser'
        #reste à coder pour mettre les objets dans le bon ordre pour ensuite définir la nouvelle poisiton init
        #de  manière à faire intéragir les objets entre eux
        #Changer beam line object pour qu'il ne dépende plus du laser mais d'une position init pouvant etre issue d'un objet
        #définir la direction du faisceau et implémenter aux objects en fonction de ou arrove le faisceau


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
                if self.check_beam_line(l)[0]==True:
                    end_pos=self.check_beam_line(l)[1][0].position()
                    beam_laser=l.action_beam(beamxend=((-1)**(l.dir()+1))*(end_pos[0]+self.check_beam_line(l)[1][0].define_size()[1]),color=color)
                    for i in range(len(self.check_beam_line(l)[1])):
                        end_pos=self.check_beam_line(l)[1][i].position()    
                        self.beam_line_objects(start_pos=start_pos,object=self.check_beam_line(l)[1][i],dir=beam_laser,color=color)
                else :
                    l.action_beam(color=color)

                    

class Laser(Object):
    "Laser object"
    def __init__(self,scr,pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\laser.png"
        self.load_image(self.pathIm)
        self.type=TYPE_LASER

    def TYPE(self):
        return self.type

    def action_beam(self,beamxend=1000,beamyend=1000,color=(250,0,0)):
        "Draw the beam"
        if self.direction in range(0,10000,4):
            start_pos=(self.position()[0],self.position()[1]+self.size[0]/2)
            end_pos=(-beamxend,self.position()[1]+self.size[0]/2)
            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
            return "left"
        elif self.direction in range(1,10000,4):
            start_pos=(self.position()[0]+self.size[1]/2,self.position()[1]+self.size[0])
            end_pos=(self.position()[0]+self.size[1]/2,beamyend)
            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
            return "down"
        elif self.direction in range(2,10000,4):
            start_pos=(self.position()[0]+self.size[1],self.position()[1]+self.size[0]/2)
            end_pos=(beamxend,self.position()[1]+self.size[0]/2)
            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
            return "right"
        elif self.direction in range(3,10000,4):
            start_pos=(self.position()[0]+self.size[1]/2,self.position()[1])
            end_pos=(self.position()[0]+self.size[1]/2,-beamyend)
            pygame.draw.line(self.screen, color, start_pos, end_pos, 2)
            return "up"

    
class Flat_mirror(Object):
    "Mirror object"
    def __init__(self,scr, pos=(0,0), current=0):
        Object.__init__(self,scr,pos, current)
        self.pathIm="\Photos_Materiel\lat_mirror.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_FLAT_MIRROR
    
    def TYPE(self):
        return self.type
    
    def action_beam(self,beamxIn,beamyIn,BeamRend=8000,color=(250,0,0)):
        "reflect the beam"
        if self.direction in range(0,10000,4):
            start_pos1=(beamxIn,beamyIn) #star of the beam (to the mirror inside the image)
            start_pos2=(beamxIn-(beamyIn-self.position()[1]),beamyIn) #start position of the reflected beam
            end_pos1=(beamxIn-(beamyIn-self.position()[1]),beamyIn) #end position of the beam (to the mirror inside the image)
            end_pos2=(beamxIn-(beamyIn-self.position()[1]),BeamRend) #end position of the reflected beam
            pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
            pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)
        if self.direction in range(1,10000,4):
            start_pos1=(beamxIn,beamyIn)
            start_pos2=(beamxIn-self.define_size()[1]+(beamyIn-self.position()[1]),beamyIn)
            end_pos2=(beamxIn-self.define_size()[1]+(beamyIn-self.position()[1]),-BeamRend)
            pygame.draw.line(self.screen, color, start_pos1, start_pos2, 2)
            pygame.draw.line(self.screen, color, start_pos2, end_pos2, 2)
        if self.direction in range(2,10000,4):
            start_pos1=(beamxIn,beamyIn)
            start_pos2=(beamxIn+(beamyIn-self.position()[1]),beamyIn)
            end_pos1=(beamxIn+(beamyIn-self.position()[1]),beamyIn)
            end_pos2=(beamxIn+(beamyIn-self.position()[1]),BeamRend)
            pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
            pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)
        if self.direction in range(3,10000,4):
            start_pos1=(beamxIn,beamyIn)
            start_pos2=(beamxIn+(beamyIn-self.position()[1]),beamyIn)
            end_pos1=(beamxIn+(beamyIn-self.position()[1]),beamyIn)
            end_pos2=(beamxIn+(beamyIn-self.position()[1]),-BeamRend)
            pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
            pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)

        pass

class Beam_splitter(Object):
    "Beam splitter object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\eam_splitter.png"
        self.load_image(self.pathIm)   
        self.type=TYPE_BEAM_SPLITTER
    
    def TYPE(self):
        return self.type

    def action_beam(self,beamxIn,beamyIn,BeamTRend=8000,BeamRend=8000,color=(250,0,0)):
        "Split the beam in two"
        if self.direction in range(0,10000,2):
            start_pos1=(beamxIn,beamyIn) #start position of the transmitted beam
            start_pos2=(beamxIn+(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]-self.define_size()[0]),beamyIn) #start position of the reflected beam
            end_pos1=(-BeamTRend,beamyIn) #end position of the transmitted beam
            end_pos2=(beamxIn+(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]-self.define_size()[0]),-BeamRend) #end position of the reflected beam
            pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
            pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)
        elif self.direction in range(1,10000,2):
            start_pos1=(beamxIn,beamyIn)
            start_pos2=(beamxIn-(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]),beamyIn) #start position of the reflected beam
            end_pos1=(-BeamTRend,beamyIn)
            end_pos2=(beamxIn-(self.define_size()[1]/self.define_size()[0])*(beamyIn-self.position()[1]),BeamRend) #end position of the reflected beam
            pygame.draw.line(self.screen, color, start_pos1,end_pos1 , 2)
            pygame.draw.line(self.screen, color, start_pos2,end_pos2 , 2)

class Fiber(Object):
    "Fibre object"
    def __init__(self, scr,pos=(0,0), current=0):
        Object.__init__(self,scr, pos, current)
        self.pathIm="\Photos_Materiel\ibre.jpg"
        self.load_image(self.pathIm)
        self.type=TYPE_FIBRE
    
    def TYPE(self):
        return self.type

    def action_beam(self,beamxIn,beamyIn,BeamRend=0,color=(250,0,0)):
        "Stop the beam"
        pass
        
