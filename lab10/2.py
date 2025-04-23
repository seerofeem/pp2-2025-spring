import pygame
import random
import psycopg2
import sys

# PostgreSQL setup
conn = psycopg2.connect(database="asd", user="postgres", password="Qwertylox007!", host="localhost", port="5432")
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    level INTEGER DEFAULT 1
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    username VARCHAR(50),
    score INTEGER,
    level INTEGER,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# Ask for username
username = input("Enter your username: ").strip()

# Check or create user
cursor.execute("SELECT level FROM users WHERE username = %s", (username,))
user_data = cursor.fetchone()
if user_data:
    level = user_data[0]
else:
    level = 1
    cursor.execute("INSERT INTO users (username, level) VALUES (%s, %s)", (username, level))
    conn.commit()

# Game settings
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
UI_HEIGHT = 50

WHITE, GREEN, RED, BLACK, BLUE, ORANGE = (255,255,255), (0,255,0), (255,0,0), (0,0,0), (0,0,255), (255,165,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + UI_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake and food
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (CELL_SIZE, 0)

def generate_food():
    while True:
        pos = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
               random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if pos not in snake:
            return pos, random.choice([1, 2, 3])

food, food_weight = generate_food()
food_timer = 100

# Score and speed
score = 0
speed = 10 + (level - 1) * 2

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause
                paused = not paused

            elif event.key == pygame.K_s:  # Save
                cursor.execute("INSERT INTO user_scores (username, score, level) VALUES (%s, %s, %s)",
                               (username, score, level))
                conn.commit()

            elif not paused:
                if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                    snake_dir = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                    snake_dir = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                    snake_dir = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                    snake_dir = (CELL_SIZE, 0)

    if paused:
        continue

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake):
        running = False

    snake.insert(0, new_head)
    if new_head == food:
        score += food_weight
        food, food_weight = generate_food()
        food_timer = 100
        if score % 5 == 0:
            level += 1
            speed += 2
            cursor.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))
            conn.commit()
    else:
        snake.pop()

    food_timer -= 1
    if food_timer <= 0:
        food, food_weight = generate_food()
        food_timer = 100

    blinking = food_timer < 20 and food_timer % 4 < 2

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    for segment in snake:
        pygame.draw.rect(screen, GREEN if score < 10 else BLUE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    if not blinking:
        color = RED if food_weight == 1 else BLUE if food_weight == 2 else ORANGE
        pygame.draw.rect(screen, color, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT, SCREEN_WIDTH, UI_HEIGHT))
    font = pygame.font.SysFont("Verdana", 20)
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, SCREEN_HEIGHT + 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (500, SCREEN_HEIGHT + 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
cursor.close()
conn.close()