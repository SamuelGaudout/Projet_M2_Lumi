import pygame

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Optics Elements')
background_colour = (250,20,75)
screen.fill(background_colour)


pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
