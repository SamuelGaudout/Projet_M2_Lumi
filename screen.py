import pygame
import Objects
import Buttons


#création de l'interface graphique avec pygame
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Optics Elements')
background_colour = (200,200,200,0)
screen.fill(background_colour)


print(screen)

optical_elements = []



list_buttons=[Buttons.Button("Laser",(10, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Laser(screen),object_list=optical_elements),
Buttons.Button("Laser",(10, 300),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Laser(screen),object_list=optical_elements),
Buttons.Button("Flat Mirror",(100, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Flat_mirror(screen),object_list=optical_elements),
Buttons.Button("Beam Splitter",(230, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Beam_splitter(screen),object_list=optical_elements),
Buttons.Button("Curve Mirror",(400, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Curve_mirror(screen),object_list=optical_elements)]


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
        list_buttons=[Buttons.Button("Laser",(10, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Laser(screen),object_list=optical_elements),
                Buttons.Button("Laser",(10, 300),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Laser(screen),object_list=optical_elements),
                Buttons.Button("Flat Mirror",(100, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Flat_mirror(screen),object_list=optical_elements),
                Buttons.Button("Beam Splitter",(230, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Beam_splitter(screen),object_list=optical_elements),
                Buttons.Button("Curve Mirror",(400, 10),font=30,scrn=screen,bg="navy",feedback="You clicked me",object=Objects.Curve_mirror(screen),object_list=optical_elements)]

    
    if len(optical_elements) != 0:
        for e in optical_elements:
            e.draw()

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
    
    b=Objects.Beam(screen,object_list=optical_elements)
    b.beam_lines_laser(color='red')
    
    if selected_object:
        mouseX=pygame.mouse.get_pos()[0]
        mouseY=pygame.mouse.get_pos()[1]
        b.beam_lines_laser(color='erase')
        selected_object.display(mouseX, mouseY)
        b.beam_lines_laser(color='red')
        
        
    pygame.display.flip()