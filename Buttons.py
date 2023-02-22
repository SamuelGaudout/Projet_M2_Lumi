import runpy
import pygame
import runpy

'''
Ce fichier créer les boutons de l'interface graphique de l'application. Les boutons sont des objets de la classe Button qui
permettent de créer des boutons avec un texte, une position, une couleur de fond, une police d'écriture, une action à effectuer
lorsque l'on clique sur le bouton, etc. Les boutons sont gérés dans ce fichier et les éléments optiques dans le fichier
"Objects.py". Les boutons sont créés dans le fichier "screen.py".
'''


pygame.init()
font = pygame.font.SysFont("Arial", 20)
 
class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font,scrn, bg="black", feedback="",object=None,object_list=None):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("freesansbold.ttf", font)
        self.screen = scrn
        self.object=object
        self.object_list=object_list
        self.object=object
        self.object_list=object_list
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def position(self):
        return (self.x, self.y)

    def optical_element(self):
        return self.object
    
    def draw_object(self):
        self.object.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+100)
        self.screen.blit(self.object.image[0], self.object.pos)
        self.object_list.append(self.object)
        


    def position(self):
        return (self.x, self.y)

    def optical_element(self):
        return self.object
    
    def draw_object(self):
        self.object.pos=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+100)
        self.screen.blit(self.object.image[0], self.object.pos)
        self.object_list.append(self.object)
        

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    #def show(self):
        #self.screen.blit(button1.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.draw_object()
                    
 


class Button_Launch(Button):
    def launch_Screen(self):
       runpy.run_path("screen.py")
    
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, "lightblue")
                    self.launch_Screen()
                   
class Button_save(Button):
   def save(self):
    pygame.image.save(self.screen, "setup.jpg")     
   
    
   def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.save()
 