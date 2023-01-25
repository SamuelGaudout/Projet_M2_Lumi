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
mass_of_air = 0.2



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

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)

    if dist < p1.size + p2.size:
        tangent = math.atan2(dy, dx)
        total_mass = p1.mass + p2.mass
        angle = 0.5 * math.pi + tangent
        angle1=addVectors(p1.angle,p1.speed*(p1.mass-p2.mass)/total_mass,angle,2*p2.speed*(p2.mass/total_mass))[0]
        angle2=addVectors(p2.angle,p2.speed*(p2.mass-p1.mass)/total_mass,angle,2*p1.speed*(p1.mass/total_mass))[0]
        speed1 = p2.speed * elasticity
        speed2 = p1.speed * elasticity
        overlap = 0.5 * (p1.size + p2.size - dist + 1)
        p1.angle, p1.speed = angle1, speed1
        p2.angle, p2.speed = angle2, speed2
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap


class Particle:
    def __init__(self, x, y, size,mass=1):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (200 - density * 10, 200 - density * 10, 255)
        self.thickness = 3
        self.speed = 0.1
        self.angle = 0
        self.mass=mass
        self.drag = (self.mass/(self.mass + mass_of_air)) ** self.size




    def display(self):
      pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self):
        #self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0],gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag
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





number_of_particles = 2
my_particles = []





for n in range(number_of_particles):
    size = random.randint(10, 20)
    density = random.randint(1, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particle = Particle(x, y, size, density*size**2)
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


    screen.fill(background_colour)


    for i,particle in enumerate(my_particles):
        particle.move()
        particle.bounce()
        for particle2 in my_particles[i+1:]:
            collide(particle, particle2)
        particle.display()

    

    
    pygame.display.update()


