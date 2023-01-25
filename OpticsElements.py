import pygame

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



