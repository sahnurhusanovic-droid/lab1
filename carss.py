import pygame
import random
import os

pygame.init()

# SCREEN SETTINGS
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (20, 150, 20)
GRAY = (80, 80, 80)
YELLOW = (255, 215, 0)
SILVER = (180, 180, 180)
BRONZE = (205, 127, 50)

# ROAD SETTINGS
ROAD_WIDTH = 260
ROAD_X = (WIDTH - ROAD_WIDTH) // 2

# CAR SETTINGS
CAR_WIDTH = 50
CAR_HEIGHT = 90

player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - 120
player_speed = 7

enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - CAR_WIDTH)
enemy_y = -120
enemy_speed = 5

# SCORE SETTINGS
score = 0
coins_collected = 0
N = 5   # every N collected coins enemy speed increases

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 42)

# IMAGE LOADING
BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")

def load_car_image(filename):
    path = os.path.join(IMAGES_DIR, filename)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (CAR_WIDTH, CAR_HEIGHT))
    return img

# Player always red
player_img = load_car_image("red.jpg")

# Enemy cars only (NO RED)
enemy_car_files = ["black.jpg", "yellow.jpg", "blue.jpg"]

enemy_img = load_car_image(random.choice(enemy_car_files))

if enemy_y > HEIGHT:
    enemy_y = -120
    enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - CAR_WIDTH)

    # NEW enemy car (not red)
    enemy_img = load_car_image(random.choice(enemy_car_files))

# COIN CLASS
class Coin:
    def __init__(self):
        # Random position on the road
        self.size = 24
        self.x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - self.size)
        self.y = -50
        self.speed = 4

        # Random coin type with different weights
        coin_type = random.choice(["bronze", "silver", "gold"])

        if coin_type == "bronze":
            self.weight = 1
            self.color = BRONZE
        elif coin_type == "silver":
            self.weight = 2
            self.color = SILVER
        else:
            self.weight = 3
            self.color = YELLOW

    def move(self):
        # Move coin down
        self.y += self.speed

    def draw(self, surface):
        # Draw coin as circle
        pygame.draw.circle(
            surface,
            self.color,
            (self.x + self.size // 2, self.y + self.size // 2),
            self.size // 2
        )

    def get_rect(self):
        # Rectangle for collision
        return pygame.Rect(self.x, self.y, self.size, self.size)


# Create first coin
coin = Coin()

# MAIN LOOP
running = True
game_over = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        # Move player left
        if keys[pygame.K_LEFT] and player_x > ROAD_X:
            player_x -= player_speed

        # Move player right
        if keys[pygame.K_RIGHT] and player_x < ROAD_X + ROAD_WIDTH - CAR_WIDTH:
            player_x += player_speed

        # Move enemy down
        enemy_y += enemy_speed

        # If enemy leaves screen, create new enemy on top
        if enemy_y > HEIGHT:
            enemy_y = -120
            enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - CAR_WIDTH)

            # Choose new random image for enemy
            enemy_img = load_car_image(random.choice(enemy_car_files))

        # Move coin
        coin.move()

        # If coin leaves screen, create new coin
        if coin.y > HEIGHT:
            coin = Coin()

        # Rectangles for collision
        player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, CAR_WIDTH, CAR_HEIGHT)
        coin_rect = coin.get_rect()

        # Check collision with coin
        if player_rect.colliderect(coin_rect):
            score += coin.weight
            coins_collected += 1
            coin = Coin()

            # Increase enemy speed every N collected coins
            if coins_collected % N == 0:
                enemy_speed += 1

        # Check collision with enemy
        if player_rect.colliderect(enemy_rect):
            game_over = True
        # Draw grass
        screen.fill(GREEN)

        # Draw road
        pygame.draw.rect(screen, GRAY, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

        # Draw middle road lines
        for y in range(0, HEIGHT, 60):
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 35))

        # Draw player image
        screen.blit(player_img, (player_x, player_y))

        # Draw enemy image
        screen.blit(enemy_img, (enemy_x, enemy_y))

        # Draw coin
        coin.draw(screen)

        # Draw texts
        score_text = font.render("Score: " + str(score), True, WHITE)
        coins_text = font.render("Coins: " + str(coins_collected), True, WHITE)
        speed_text = font.render("Enemy speed: " + str(enemy_speed), True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(coins_text, (10, 45))
        screen.blit(speed_text, (10, 80))

    else:
        # Game over screen
        screen.fill(BLACK)

        over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        final_score = font.render("Final score: " + str(score), True, WHITE)
        final_coins = font.render("Coins: " + str(coins_collected), True, WHITE)

        screen.blit(over_text, (130, 280))
        screen.blit(final_score, (160, 350))
        screen.blit(final_coins, (185, 390))

    pygame.display.update()

pygame.quit()