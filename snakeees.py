import pygame
import random
pygame.init()
# SCREEN SETTINGS
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
PURPLE = (180, 0, 180)

CELL = 20

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 40)

# SNAKE SETTINGS
snake = [(100, 100), (80, 100), (60, 100)]
dx = CELL
dy = 0

score = 0
game_over = False

# FOOD CLASS
class Food:
    def __init__(self):
        # Random position
        self.x = random.randrange(0, WIDTH, CELL)
        self.y = random.randrange(0, HEIGHT, CELL)

        # Random type (weight)
        food_type = random.choice(["small", "medium", "big"])

        if food_type == "small":
            self.weight = 1
            self.color = RED
            self.lifetime = 5000   # 5 sec
        elif food_type == "medium":
            self.weight = 2
            self.color = YELLOW
            self.lifetime = 4000   # 4 sec
        else:
            self.weight = 3
            self.color = PURPLE
            self.lifetime = 3000   # 3 sec

        # Save spawn time
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        # Draw food
        pygame.draw.rect(screen, self.color, (self.x, self.y, CELL, CELL))

    def is_expired(self):
        # Check if time is over
        now = pygame.time.get_ticks()
        return now - self.spawn_time > self.lifetime


def create_food():
    # Create food not inside snake
    while True:
        f = Food()
        if (f.x, f.y) not in snake:
            return f


food = create_food()

running = True

# MAIN LOOP
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Direction control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL

    if not game_over:
        # If food expired → create new
        if food.is_expired():
            food = create_food()

        # Move snake
        head_x = snake[0][0] + dx
        head_y = snake[0][1] + dy
        new_head = (head_x, head_y)

        # Collision with wall
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True

        # Collision with itself
        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            # Eat food
            if new_head == (food.x, food.y):
                score += food.weight

                # Increase snake length depending on weight
                for i in range(food.weight - 1):
                    snake.append(snake[-1])

                food = create_food()
            else:
                snake.pop()

        # DRAWING
        screen.fill(BLACK)

        # Draw snake
        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL, CELL))

        # Draw food
        food.draw()

        # Score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Timer
        time_left = max(0, (food.lifetime - (pygame.time.get_ticks() - food.spawn_time)) // 1000)
        timer_text = font.render("Food: " + str(time_left), True, WHITE)
        screen.blit(timer_text, (10, 40))

    else:
        # Game over screen
        screen.fill(BLACK)

        over_text = big_font.render("GAME OVER", True, RED)
        score_text = font.render("Score: " + str(score), True, WHITE)

        screen.blit(over_text, (160, 250))
        screen.blit(score_text, (200, 320))

    pygame.display.update()

pygame.quit()