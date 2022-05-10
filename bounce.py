import pygame
import random

pygame.init()
clock = pygame.time.Clock()

""" Game variables """
bg_color = 'cyan'
ball_color = 'red'
ball_radius = 10
jump_height = 4
brick_color = 'brown'
brick_width = 30
brick_height = 15
gap = 1
# fps
game_speed = 300



# Window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Bounce')



# Ball class
class Ball:
    def __init__(self) -> None:
        self.x = 0 + ball_radius
        self.y = window_height - brick_height * 3 - ball_radius + 1
        self.color = ball_color
        self.radius = ball_radius
        self.jumping = False
        self.vel_x = 1
        self.vel_y = jump_height
    
    def draw(self) -> None:
        if self.x <= 0 + self.radius:
            self.x = 0 + self.radius

        if self.x >= window_width - self.radius:
            self.x = window_width - self.radius

        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move_right(self) -> None:
        self.x += self.vel_x
    
    def move_left(self) -> None:
        self.x -= self.vel_x


    def jump(self) -> None:
        if self.jumping:
            self.y -= self.vel_y
            self.vel_y -= 0.05
            if self.vel_y <= -jump_height:
                self.jumping = False
                self.vel_y = jump_height



# Brick class
class Brick:
    all_bricks = []
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = brick_color
        Brick.all_bricks.append(self)


    def draw(self) -> None:
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


floor_bricks_list = []
x = 0
y = window_height - 45
for i in range((window_width // brick_width) * 4):
    floor_bricks_list.append(Brick(x, y, brick_width, brick_height))
    x += brick_width + gap
    if x >= window_width:
        y += brick_height + gap
        x = random.randint(-5, -2)

    


ball = Ball()



running = True
while running:
    clock.tick(game_speed)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('cyan')

    ball.draw()

    if keys[pygame.K_UP] and ball.jumping == False:
        ball.jumping = True
    ball.jump()


    if keys[pygame.K_RIGHT]:
        ball.move_right()
    
    if keys[pygame.K_LEFT]:
        ball.move_left()


    for brick in floor_bricks_list:
        brick.draw()





    pygame.display.update()
