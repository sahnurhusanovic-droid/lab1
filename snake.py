import pygame
import random
import sys

pygame.init()
WIDTH = 600
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
DARK_GREEN = (0, 120, 0)
RED = (255, 0, 0)
GRAY = (120, 120, 120)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

snake = [(100, 100), (80, 100), (60, 100)]  
dx = CELL  
dy = 0

score = 0
level = 1
speed = 7

foods_for_next_level = 3   

walls = [
    pygame.Rect(200, 200, 20, 100),
    pygame.Rect(380, 300, 20, 120),
    pygame.Rect(260, 100, 100, 20)
]


def generate_food():
    """
    Generate food at random position.
    Food must not appear:
    1) on snake
    2) on wall
    """
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        food_rect = pygame.Rect(x, y, CELL, CELL)

        if (x, y) in snake:
            continue

        on_wall = False
        for wall in walls:
            if food_rect.colliderect(wall):
                on_wall = True
                break

        if on_wall:
            continue

        return (x, y)


food = generate_food()


def draw_grid():
    """Optional grid for better view."""
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_snake():
    """Draw snake body."""
    for i, part in enumerate(snake):
        rect = pygame.Rect(part[0], part[1], CELL, CELL)
        if i == 0:
            pygame.draw.rect(screen, DARK_GREEN, rect)  
        else:
            pygame.draw.rect(screen, GREEN, rect)       


def draw_food():
    """Draw food."""
    rect = pygame.Rect(food[0], food[1], CELL, CELL)
    pygame.draw.rect(screen, RED, rect)


def draw_walls():
    """Draw all walls."""
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)


def draw_info():
    """Draw score and level."""
    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))


def game_over():
    """Show game over text."""
    screen.fill(WHITE)
    text = big_font.render("GAME OVER", True, RED)
    screen.blit(text, (170, 260))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        game_over()

    if new_head in snake:
        game_over()

    head_rect = pygame.Rect(new_head[0], new_head[1], CELL, CELL)
    for wall in walls:
        if head_rect.colliderect(wall):
            game_over()

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generate_food()

        if score % foods_for_next_level == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    screen.fill(WHITE)
    draw_grid()
    draw_walls()
    draw_snake()
    draw_food()
    draw_info()

    pygame.display.update()

pygame.quit()
sys.exit()