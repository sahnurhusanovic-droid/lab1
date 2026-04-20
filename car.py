import pygame
import random
import os
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()

GREEN = (0,150,0)
GRAY = (80,80,80)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,215,0)

ROAD_WIDTH = 240
ROAD_X = (WIDTH - ROAD_WIDTH)//2
ROAD_LEFT = ROAD_X
ROAD_RIGHT = ROAD_X + ROAD_WIDTH

CAR_W = 50
CAR_H = 80

BASE_DIR = os.path.dirname(__file__)

score = 0
coins_collected = 0

def load_img(name):
    path = os.path.join(BASE_DIR,"images",name)
    img = pygame.image.load(path)
    img = pygame.transform.scale(img,(CAR_W,CAR_H))
    img.set_colorkey((255,255,255))
    return img


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_img("red.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT-20

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT]:
            self.rect.x += 6

        if self.rect.left < ROAD_LEFT:
            self.rect.left = ROAD_LEFT
        if self.rect.right > ROAD_RIGHT:
            self.rect.right = ROAD_RIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [load_img("blue.jpg"), load_img("yellow.jpg")]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.image = random.choice(self.images)
        self.rect.x = random.randint(ROAD_LEFT, ROAD_RIGHT - CAR_W)
        self.rect.y = -100

    def move(self):
        global score
        self.rect.y += 6

        if self.rect.top > HEIGHT:
            score += 1   
            self.reset()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30,30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15,15), 12)

        self.rect = self.image.get_rect()
        self.active = False
        self.hide()

    def spawn(self):
        self.rect.center = (random.randint(ROAD_LEFT+20, ROAD_RIGHT-20), -20)
        self.active = True

    def hide(self):
        self.rect.center = (-100,-100)
        self.active = False

    def move(self):
        if self.active:
            self.rect.y += 6
            if self.rect.top > HEIGHT:
                self.hide()


player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)

font = pygame.font.SysFont("Arial", 22)

SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 2000)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_COIN:
            if not coin.active:
                if random.randint(1,2) == 1:
                    coin.spawn()

    player.move()
    enemy.move()
    coin.move()

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, (ROAD_X,0,ROAD_WIDTH,HEIGHT))

    pygame.draw.line(screen, WHITE, (ROAD_LEFT,0),(ROAD_LEFT,HEIGHT),4)
    pygame.draw.line(screen, WHITE, (ROAD_RIGHT,0),(ROAD_RIGHT,HEIGHT),4)

    y = 0
    while y < HEIGHT:
        pygame.draw.rect(screen, WHITE, (WIDTH//2-3,y,6,40))
        y += 65

    for s in all_sprites:
        screen.blit(s.image, s.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        print("GAME OVER")
        pygame.time.delay(1500)
        break

    if coin.active and pygame.sprite.collide_rect(player, coin):
        coins_collected += 1
        coin.hide()

    score_text = font.render("Score: " + str(score), True, BLACK)
    coin_text = font.render("Coins: " + str(coins_collected), True, BLACK)

    screen.blit(score_text, (10,10))
    screen.blit(coin_text, (WIDTH-120,10))

    pygame.display.update()

pygame.quit()
sys.exit()