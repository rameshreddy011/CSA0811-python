import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (CELL_SIZE, 0)

# Food variables
food = (random.randint(0, (WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)

# Obstacles
obstacles = [(200, 100), (220, 100), (240, 100), (220, 80), (220, 120),
             (240, 80), (240, 120), (400, 200), (380, 200), (420, 200),
             (400, 180), (400, 220), (100, 300), (80, 300), (120, 300),
             (100, 280), (100, 320)]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game state
game_over = False

# Game loop
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, CELL_SIZE):
        snake_direction = (0, -CELL_SIZE)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -CELL_SIZE):
        snake_direction = (0, CELL_SIZE)
    elif keys[pygame.K_LEFT] and snake_direction != (CELL_SIZE, 0):
        snake_direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-CELL_SIZE, 0):
        snake_direction = (CELL_SIZE, 0)

    # Move snake
    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [head] + snake[:-1]

    # Check collisions
    if head == food:
        snake.append(snake[-1])
        food = (random.randint(0, (WIDTH-CELL_SIZE)//CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT-CELL_SIZE)//CELL_SIZE) * CELL_SIZE)
        score += 1
    elif head in obstacles:
        game_over = True

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]:
        game_over = True

    # Draw background
    screen.fill(BLACK)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, (obstacle[0], obstacle[1], CELL_SIZE, CELL_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
screen.fill(BLACK)
game_over_text = font.render(f"Game Over - Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH//4, HEIGHT//2))
pygame.display.flip()

# Wait for a few seconds before exiting
pygame.time.wait(3000)
pygame.quit()
sys.exit()
