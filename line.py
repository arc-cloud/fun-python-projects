from math import cos, sin
import pygame

pygame.init()
clock = pygame.time.Clock()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Line')

# Line class
class Line:
    def __init__(self) -> None:
        self.end_x = window_width / 2
        self.end_x2 = window_width / 2
        self.end_y = window_height / 2 
        self.end_y2 = window_height / 2 
        self.radians = 0
        self.vel = 0.1

    def draw(self):
        pygame.draw.circle(window, 'black', (self.end_x, self.end_y), 10)
        pygame.draw.line(window, 'black', (self.end_x2, self.end_y2), (self.end_x, self.end_y), 1)
        self.oscillate()

    def oscillate(self):
        self.end_x = self.end_x2 + cos(self.radians) * 100
        self.end_y = self.end_y2 + sin(self.radians) * 100
        self.radians += -self.vel



line = Line()

running = True

while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((128, 128, 128))
    line.draw()
    pygame.display.update()