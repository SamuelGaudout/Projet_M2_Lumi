import pygame
import random
import math



(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Optics Elements')
background_colour = (250,250,240)
screen.fill(background_colour)

gravity = [math.pi, 0.002]
drag = 0.999
elasticity = 0.75



def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return angle, length



def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None




class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        self.thickness = 3
        self.speed = 0.1
        self.angle = 0



    def display(self):
      pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self):
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0],gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag
        #self.speed *= elasticity


    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle





number_of_particles = 10
my_particles = []





for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particle = Particle(x, y, size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)
    my_particles.append(particle)







pygame.display.flip()
running = True
selected_particle = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            selected_particle = findParticle(my_particles, mouseX, mouseY)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None
    
    if selected_particle:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5 * math.pi + math.atan2(dy,dx) 
        selected_particle.speed = math.hypot(dx, dy) * 0.01
        #selected_particle.x = dx 
        #selected_particle.y = dy 


    screen.fill(background_colour)
    for particle in my_particles:
        if particle != selected_particle:
            particle.move()
            particle.bounce()
        particle.display()

    

    
    pygame.display.update()


