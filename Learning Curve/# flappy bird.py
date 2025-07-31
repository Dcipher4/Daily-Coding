import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Bird settings
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
BIRD_X = 50
BIRD_Y = SCREEN_HEIGHT // 2
GRAVITY = 0.5
JUMP = -10

# Pipe settings
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 200
PIPE_SPEED = 4

# Load assets with exception handling
try:
    bird_image = pygame.image.load('bird.png')
    pipe_top_image = pygame.image.load('pipe_top.png')
    pipe_bottom_image = pygame.image.load('pipe_bottom.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    exit()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Bird class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.vel_y = 0

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y
        if self.y > SCREEN_HEIGHT - BIRD_HEIGHT:
            self.y = SCREEN_HEIGHT - BIRD_HEIGHT
            self.vel_y = 0

    def flap(self):
        self.vel_y = JUMP

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.passed = False

    def draw(self):
        screen.blit(pipe_top_image, (self.x, self.height - PIPE_HEIGHT))
        screen.blit(pipe_bottom_image, (self.x, self.height + PIPE_GAP))

    def update(self):
        self.x -= PIPE_SPEED

# Main game loop
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        bird.draw()
        bird.update()

        for pipe in pipes:
            pipe.draw()
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe())
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
