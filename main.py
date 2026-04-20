import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Түстер
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Шар
x, y = WIDTH // 2, HEIGHT // 2
RADIUS = 25
STEP = 20

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x - STEP - RADIUS >= 0:
                x -= STEP
            if event.key == pygame.K_RIGHT and x + STEP + RADIUS <= WIDTH:
                x += STEP
            if event.key == pygame.K_UP and y - STEP - RADIUS >= 0:
                y -= STEP
            if event.key == pygame.K_DOWN and y + STEP + RADIUS <= HEIGHT:
                y += STEP

    pygame.draw.circle(screen, RED, (x, y), RADIUS)

    pygame.display.update()
    clock.tick(60)

pygame.quit()