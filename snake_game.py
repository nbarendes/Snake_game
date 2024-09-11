# snake_game.py
"""
A simple implementation of the classic Snake game using Pygame.
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Display setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.Font(None, 36)

# Snake and food setup
snake = [(200, 200), (220, 200), (240, 200)]   
food = (400, 300)
direction = (1, 0)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move the snake
    head = snake[-1]
    new_head = (head[0] + direction[0] * 20, head[1] + direction[1] * 20)
    
    # Boundary collision detection
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over! Boundary collision.")
        pygame.quit()
        sys.exit()

    # Self-collision detection
    if new_head in snake[:-1]:
        print("Game Over! Self-collision.")
        pygame.quit()
        sys.exit()

    snake.append(new_head)

    # Check if the snake has eaten the food
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - 20) // 20 * 20, 
                random.randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake.pop(0)

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    for x, y in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, 20, 20))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], 20, 20))

    # Score display
    score = len(snake) - 3
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)
