from math import cos, pi, sin
import random
import pygame

pygame.init()
clock = pygame.time.Clock()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Fun with particles')

num_of_particles = 2


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)



# Particle class
class Particle:
    def __init__(self, x, y, radius, color) -> None:
        self.x = x
        self.x2 = x
        self.y = y
        self.y2 = y
        self.radius = radius
        self.color = color
        self.radians = random.random() * pi * 2
        self.vel = 0.05
        self.dist = random.randint(50, 100)

    def draw(self) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        self.oscillate()

    def oscillate(self):
        self.x = self.x2 + cos(self.radians) * self.dist
        self.y = self.y2 + sin(self.radians) * self.dist


particle_list = []

for i in range(num_of_particles):
    particle_list.append(Particle(window_width / 2, window_height / 2, 5, black))


running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(white)
    #window.set_alpha(255)

    for particle in particle_list:
        particle.draw()
        particle.radians += particle.vel

    pygame.display.update()