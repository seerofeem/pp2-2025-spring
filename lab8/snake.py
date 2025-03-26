import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20  # Size of each cell in the grid
UI_HEIGHT = 50  # Extra space for UI elements

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + UI_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control speed
clock = pygame.time.Clock()

# Snake settings
snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake body
snake_dir = (CELL_SIZE, 0)  # Initial direction (right)

# Food settings
def generate_food():
    while True:
        food_pos = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if food_pos not in snake:  # Ensure food does not spawn on the snake
            return food_pos

food = generate_food()

# Game variables
score = 0
level = 1
speed = 10  # Initial speed

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check for wall collision
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake):  # Check if the snake collides with itself
        running = False  # End game

    # Add new head to the snake
    snake.insert(0, new_head)
    
    # Check if the snake eats food
    if new_head == food:
        score += 1
        food = generate_food()
        
        # Increase level every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2  # Increase speed
    else:
        snake.pop()  # Remove tail if no food is eaten
    
    # Draw everything
    screen.fill(BLACK)
    
    # Draw game area
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Draw UI area
    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT, SCREEN_WIDTH, UI_HEIGHT))
    
    # Display score and level
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, SCREEN_HEIGHT + 10))
    screen.blit(level_text, (500, SCREEN_HEIGHT + 10))
    
    # Update display
    pygame.display.flip()
    
    # Control speed
    clock.tick(speed)

# Quit pygame
pygame.quit()
