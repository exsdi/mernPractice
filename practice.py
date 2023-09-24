import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Define the size of each grid cell
cell_size = 20

# Define the initial position and size of the snake
snake_x = width // 2
snake_y = height // 2
snake_size = 1
snake_speed = 5
snake_x_change = 0
snake_y_change = 0

# Define the initial position of the food
food_x = round(random.randrange(0, width - cell_size) / cell_size) * cell_size
food_y = round(random.randrange(0, height - cell_size) / cell_size) * cell_size

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -cell_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = cell_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -cell_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = cell_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        snake_size += 1
        food_x = round(random.randrange(0, width - cell_size) / cell_size) * cell_size
        food_y = round(random.randrange(0, height - cell_size) / cell_size) * cell_size

    # Draw background
    window.fill(black)

    # Draw snake
    pygame.draw.rect(window, green, (snake_x, snake_y, cell_size, cell_size))

    # Draw food
    pygame.draw.rect(window, red, (food_x, food_y, cell_size, cell_size))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()