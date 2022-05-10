import random
import pygame


pygame.init()
clock = pygame.time.Clock()


# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

""" Game variables """
window_width, window_height = 800, 600
fps = 500

# Paddle
paddle_speed = 1
paddle_color = black

# Ball
ball_speed = 1
ball_color = blue


# Paddle class
class Paddle:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.vel = paddle_speed
        self.width = 15
        self.height = 100
        self.color = paddle_color

    def draw(self) -> None:
        if self.y <= 0:
            self.y = 0

        if self.y >= window_height - self.height:
            self.y = window_height - self.height

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))



# Ball class
class Ball:
    def __init__(self) -> None:
        self.x = window_width / 2
        self.y = window_height / 2
        self.color = ball_color
        self.vel_x = ball_speed
        self.vel_y = 0
        self.radius = 10

    def draw(self) -> None:
        if self.y <= 0 + self.radius:
            self.vel_y *= -1

        if self.y >= window_height - self.radius:
            self.vel_y *= -1


        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Ping Pong')

running = True
l_paddle = Paddle(20, (window_height / 2 - 50))
r_paddle = Paddle(window_width - 40, (window_height / 2 - 50))
ball = Ball()


# Main game loop
while running:
    clock.tick(fps)
    window.fill(white)
    keys = pygame.key.get_pressed()

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    l_paddle.draw()
    r_paddle.draw()
    ball.draw()

    ball.x += ball.vel_x
    ball.y += ball.vel_y

    if ball.x < l_paddle.x + l_paddle.width:
        if ball.y >= l_paddle.y and ball.y <= l_paddle.y + l_paddle.height:
            ball.vel_x *= -1
            ball.vel_y = random.random() * ball.vel_x
            

    if ball.x >= r_paddle.x:
        if ball.y >= r_paddle.y and ball.y <= r_paddle.y + r_paddle.height:
            ball.vel_x *= -1
            ball.vel_y = random.random() * ball.vel_x

            

    # Left paddle up
    if keys[pygame.K_w]:
        l_paddle.y -= l_paddle.vel

    # Left paddle down
    if keys[pygame.K_s]:
        l_paddle.y += l_paddle.vel
        
    # Right paddle up
    if keys[pygame.K_UP]:
        r_paddle.y -= l_paddle.vel

    # Right paddle down
    if keys[pygame.K_DOWN]:
        r_paddle.y += l_paddle.vel

    pygame.display.flip()

    
