# snake_game.py
"""
A simple implementation of the classic Snake game using Pygame.
"""

import pygame
import sys
import random

# Constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BLOCK_SIZE = 20

# Initialize Pygame
pygame.init()
# Display setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.food = (400, 300)
        self.direction = (1, 0)
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                    self.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                    self.direction = (1, 0)

    def update(self):
        head = self.snake[-1]
        new_head = (head[0] + self.direction[0] * BLOCK_SIZE, head[1] + self.direction[1] * BLOCK_SIZE)
    
        # Boundary collision detection
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            print("Game Over! Boundary collision.")
            pygame.quit()
            sys.exit()

        # Self-collision detection
        if new_head in self.snake[:-1]:
            print("Game Over! Self-collision.")
            pygame.quit()
            sys.exit()

        self.snake.append(new_head)

        # Check if the snake has eaten the food
        if self.snake[-1] == self.food:
            self.food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, 
                         random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
        else:
            self.snake.pop(0)
            self.score = len(self.snake) - 3

    def draw(self):
        screen.fill(BACKGROUND_COLOR)
        for x, y in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, FOOD_COLOR, (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

        # Score display
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
