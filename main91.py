import pygame
import math
from datetime import datetime

pygame.init()

WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

timer = pygame.time.Clock()
clock_face = pygame.image.load("imagex/clock_face.jpg").convert_alpha()
hand_img = pygame.image.load("imagex/hand.png").convert_alpha()

clock_face = pygame.transform.smoothscale(clock_face, (760, 760))
hand_img = pygame.transform.smoothscale(hand_img, (120, 320))


left_hand_img = hand_img
right_hand_img = pygame.transform.flip(hand_img, True, False)


center_x = WIDTH // 2
center_y = HEIGHT // 2

face_rect = clock_face.get_rect(center=(center_x, center_y))

font = pygame.font.SysFont("arial", 36, bold=True)


def draw_hand(surface, image, center_x, center_y, angle, length):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect()

    rad = math.radians(-angle)

    x = center_x + int(math.sin(rad) * length)
    y = center_y - int(math.cos(rad) * length)

    rotated_rect.center = (x, y)
    surface.blit(rotated_image, rotated_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    second_angle = -seconds * 6
    minute_angle = -minutes * 6

    screen.fill((230, 230, 230))
    screen.blit(clock_face, face_rect)

    draw_hand(
        screen,
        left_hand_img,
        center_x,
        center_y,
        second_angle + 30,
        90
    )

    draw_hand(
        screen,
        right_hand_img,
        center_x,
        center_y,
        minute_angle - 30,
        70
    )

    pygame.draw.circle(screen, (20, 20, 20), (center_x, center_y), 10)

    text = font.render(f"{minutes:02d}:{seconds:02d}", True, (20, 20, 20))
    text_rect = text.get_rect(center=(center_x, 840))
    screen.blit(text, text_rect)

    pygame.display.flip()
    timer.tick(60)

pygame.quit()