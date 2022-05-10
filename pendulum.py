from math import pi
import pygame

pygame.init()
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

""" Variables """
bob_radius = 15
string_length = 200
fps = 60

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simple pendulum')



class Pendulum:
    def __init__(self) -> None:
        self.string_length = string_length
        self.color = white
        self.x = window_width / 2
        self.y = window_height / 2
        

        

    def draw(self) -> None:
        pygame.draw.line(window, self.color, (self.x, self.y), (self.x, self.y + self.string_length), 2)


pendulum = Pendulum()

running = True

# Main loop
while running:
    clock.tick(fps)
    window.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pendulum.draw()
    pendulum.rotate()

    pygame.display.update()