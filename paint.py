import pygame
import sys

pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint App")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

current_color = BLACK
brush_size = 6
tool = "brush"  

drawing = False
start_pos = None
last_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)


def draw_text():
    text = f"Tool: {tool}   Size: {brush_size}   Keys: B-brush, R-rect, C-circle, E-eraser, 1/2/3/4-colors, SPACE-clear"
    img = font.render(text, True, BLACK)
    screen.blit(img, (10, 10))


def draw_color_boxes():
    pygame.draw.rect(screen, RED, (10, 40, 30, 30))
    pygame.draw.rect(screen, GREEN, (50, 40, 30, 30))
    pygame.draw.rect(screen, BLUE, (90, 40, 30, 30))
    pygame.draw.rect(screen, BLACK, (130, 40, 30, 30))


def draw_line(surface, color, start, end, width):

    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(abs(dx), abs(dy))

    if steps == 0:
        pygame.draw.circle(surface, color, start, width)
        return

    for i in range(steps + 1):
        x = int(start[0] + dx * i / steps)
        y = int(start[1] + dy * i / steps)
        pygame.draw.circle(surface, color, (x, y), width)


def make_rect(start, end):
    x1 = min(start[0], end[0])
    y1 = min(start[1], end[1])
    x2 = max(start[0], end[0])
    y2 = max(start[1], end[1])
    return pygame.Rect(x1, y1, x2 - x1, y2 - y1)


def draw_preview():
    if not drawing or start_pos is None:
        return

    mouse_pos = pygame.mouse.get_pos()

    if tool == "rect":
        rect = make_rect(start_pos, mouse_pos)
        pygame.draw.rect(screen, current_color, rect, 2)

    elif tool == "circle":
        radius = int(((mouse_pos[0] - start_pos[0]) ** 2 + (mouse_pos[1] - start_pos[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, current_color, start_pos, radius, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_b:
                tool = "brush"

            elif event.key == pygame.K_r:
                tool = "rect"

            elif event.key == pygame.K_c:
                tool = "circle"

            elif event.key == pygame.K_e:
                tool = "eraser"

            elif event.key == pygame.K_1:
                current_color = RED

            elif event.key == pygame.K_2:
                current_color = GREEN

            elif event.key == pygame.K_3:
                current_color = BLUE

            elif event.key == pygame.K_4:
                current_color = BLACK

            elif event.key == pygame.K_LEFTBRACKET:
                brush_size = max(1, brush_size - 1)

            elif event.key == pygame.K_RIGHTBRACKET:
                brush_size = min(50, brush_size + 1)

            elif event.key == pygame.K_SPACE:
                canvas.fill(WHITE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

                mx, my = event.pos
                if pygame.Rect(10, 40, 30, 30).collidepoint(mx, my):
                    current_color = RED
                    drawing = False
                elif pygame.Rect(50, 40, 30, 30).collidepoint(mx, my):
                    current_color = GREEN
                    drawing = False
                elif pygame.Rect(90, 40, 30, 30).collidepoint(mx, my):
                    current_color = BLUE
                    drawing = False
                elif pygame.Rect(130, 40, 30, 30).collidepoint(mx, my):
                    current_color = BLACK
                    drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "brush":
                    draw_line(canvas, current_color, last_pos, event.pos, brush_size)

                elif tool == "eraser":
                    draw_line(canvas, WHITE, last_pos, event.pos, brush_size)

                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos

                if tool == "rect":
                    rect = make_rect(start_pos, end_pos)
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                drawing = False
                start_pos = None
                last_pos = None
    screen.fill(GRAY)
    screen.blit(canvas, (0, 0))

    draw_text()
    draw_color_boxes()
    draw_preview()

    pygame.display.flip()
    clock.tick(60)