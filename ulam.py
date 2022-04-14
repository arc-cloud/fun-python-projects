import pygame

# Clock mechanism for the fps
clock = pygame.time.Clock()


# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


""" Change these values at will and see how the program works """
number_of_particles = 4096
fps = 60
primes_color = red
other_numbers_color = white
background_color = black
particle_size = 2
spacing_x = 10
spacing_y = -10
screen_width, screen_height = 700, 700




# Function for checking if a number is a prime number
def is_prime(num) -> bool:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False



""" Unnecessary code but just felt like I should keep it """
# Map primes into a list
primes = []
for i in range(1, 10):
    if is_prime(i):
        primes.append(i)



# Pygame window
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ulam Spiral")
running = True
screen.fill(background_color)

# Particle class
class Particle:
    def __init__(self, x, y) -> None:
        self.size = particle_size
        self.color = white
        self.x = x
        self.y = y
        self.vel_x = spacing_x
        self.vel_y = spacing_y
        
    # Drawing the particle
    def draw(self) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


# Main loop
while running:

    # Frame rate
    clock.tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    particle = Particle(screen_width / 2, screen_height / 2)
    turn_counter = 0
    steps_taken = 1
    steps = 1
    state = 0


    for i in range(number_of_particles):
        if is_prime(i):
            particle.color = primes_color
            

        else:
            particle.color = other_numbers_color



        particle.draw()
        # particle.draw_line()
        # particle.x += particle.vel_x
        
        if state == 0:
            particle.x += particle.vel_x

        elif state == 1:
            particle.y += particle.vel_y

        elif state == 2:
            particle.x -= particle.vel_x

        elif state == 3:
            particle.y -= particle.vel_y


        if steps % steps_taken == 0:
            state = (state + 1) % 4
            turn_counter += 1

            if turn_counter % 2 == 0:
                steps_taken += 1

        steps += 1


    pygame.display.update()



