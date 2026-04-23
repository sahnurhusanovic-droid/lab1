import pygame
import sys
import math

pygame.init()

WIDTH = 900
HEIGHT = 600
TOP_PANEL = 85

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint App")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 18)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (120, 120, 120)

current_color = BLACK
brush_size = 6
tool = "brush"

drawing = False
start_pos = None
last_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)


def draw_text():
    line1 = "1-Brush   2-Rect   3-Circle   4-Square   5-RightTri   6-EquiTri   7-Rhombus"
    line2 = "R-Red   G-Green   B-Blue   K-Black   E-Eraser   q / p -Size   SPACE-Clear"

    img1 = font.render(line1, True, BLACK)
    img2 = font.render(line2, True, BLACK)

    screen.blit(img1, (10, 8))
    screen.blit(img2, (10, 35))

    info = f"Tool: {tool}   Size: {brush_size}"
    img3 = small_font.render(info, True, BLACK)
    screen.blit(img3, (10, 60))


def draw_color_boxes():
    pygame.draw.rect(screen, RED, (700, 10, 30, 30))
    pygame.draw.rect(screen, GREEN, (740, 10, 30, 30))
    pygame.draw.rect(screen, BLUE, (780, 10, 30, 30))
    pygame.draw.rect(screen, BLACK, (820, 10, 30, 30))


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


def clamp_to_canvas(pos):
    x = max(0, min(WIDTH - 1, pos[0]))
    y = max(TOP_PANEL, min(HEIGHT - 1, pos[1]))
    return (x, y)


def draw_size_text(start, end):
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    text = f"W: {w}  H: {h}"
    img = small_font.render(text, True, BLACK)

    tx = min(start[0], end[0])
    ty = min(start[1], end[1]) - 20

    if ty < TOP_PANEL:
        ty = min(start[1], end[1]) + 5

    screen.blit(img, (tx, ty))


def get_square_rect(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = min(abs(dx), abs(dy))

    if dx >= 0:
        x = start[0]
    else:
        x = start[0] - side

    if dy >= 0:
        y = start[1]
    else:
        y = start[1] - side

    return pygame.Rect(x, y, side, side)


def get_right_triangle_points(start, end):
    x1, y1 = start
    x2, y2 = end
    return [(x1, y1), (x1, y2), (x2, y2)]


def get_equilateral_triangle_points(start, end):
    x1, y1 = start
    side = abs(end[0] - start[0])

    if side < 10:
        side = 10

    direction = 1
    if end[0] < start[0]:
        direction = -1

    height = int(math.sqrt(3) * side / 2)

    p1 = (x1, y1)
    p2 = (x1 + direction * side, y1)
    p3 = (x1 + direction * side // 2, y1 - height)

    return [p1, p2, p3]


def get_rhombus_points(start, end):
    x1, y1 = start
    x2, y2 = end

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    return [
        (center_x, y1),   
        (x2, center_y),   
        (center_x, y2), 
        (x1, center_y)    
    ]


def draw_preview():
    if not drawing or start_pos is None:
        return

    mouse_pos = clamp_to_canvas(pygame.mouse.get_pos())

    if tool == "rect":
        rect = make_rect(start_pos, mouse_pos)
        pygame.draw.rect(screen, current_color, rect, 2)
        draw_size_text(start_pos, mouse_pos)

    elif tool == "circle":
        radius = int(((mouse_pos[0] - start_pos[0]) ** 2 + (mouse_pos[1] - start_pos[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, current_color, start_pos, radius, 2)

        text = f"R: {radius}"
        img = small_font.render(text, True, BLACK)
        screen.blit(img, (start_pos[0] + 10, start_pos[1] - 20))

    elif tool == "square":
        rect = get_square_rect(start_pos, mouse_pos)
        pygame.draw.rect(screen, current_color, rect, 2)

        text = f"Side: {rect.width}"
        img = small_font.render(text, True, BLACK)
        screen.blit(img, (rect.x, rect.y - 20 if rect.y - 20 >= TOP_PANEL else rect.y + rect.height + 5))

    elif tool == "right_triangle":
        points = get_right_triangle_points(start_pos, mouse_pos)
        pygame.draw.polygon(screen, current_color, points, 2)
        draw_size_text(start_pos, mouse_pos)

    elif tool == "equilateral_triangle":
        points = get_equilateral_triangle_points(start_pos, mouse_pos)
        pygame.draw.polygon(screen, current_color, points, 2)

        side = abs(mouse_pos[0] - start_pos[0])
        text = f"Side: {side}"
        img = small_font.render(text, True, BLACK)
        screen.blit(img, (start_pos[0], start_pos[1] + 10))

    elif tool == "rhombus":
        points = get_rhombus_points(start_pos, mouse_pos)
        pygame.draw.polygon(screen, current_color, points, 2)
        draw_size_text(start_pos, mouse_pos)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_1:
                tool = "brush"

            elif event.key == pygame.K_2:
                tool = "rect"

            elif event.key == pygame.K_3:
                tool = "circle"

            elif event.key == pygame.K_4:
                tool = "square"

            elif event.key == pygame.K_5:
                tool = "right_triangle"

            elif event.key == pygame.K_6:
                tool = "equilateral_triangle"

            elif event.key == pygame.K_7:
                tool = "rhombus"

            elif event.key == pygame.K_e:
                tool = "eraser"

            elif event.key == pygame.K_r:
                current_color = RED

            elif event.key == pygame.K_g:
                current_color = GREEN

            elif event.key == pygame.K_b:
                current_color = BLUE

            elif event.key == pygame.K_k:
                current_color = BLACK

            elif event.key == pygame.K_q:
                brush_size = max(1, brush_size - 1)

            elif event.key == pygame.K_p:
                brush_size = min(50, brush_size + 1)

            elif event.key == pygame.K_SPACE:
                canvas.fill(WHITE)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = event.pos

                if pygame.Rect(700, 10, 30, 30).collidepoint(mx, my):
                    current_color = RED
                    continue
                elif pygame.Rect(740, 10, 30, 30).collidepoint(mx, my):
                    current_color = GREEN
                    continue
                elif pygame.Rect(780, 10, 30, 30).collidepoint(mx, my):
                    current_color = BLUE
                    continue
                elif pygame.Rect(820, 10, 30, 30).collidepoint(mx, my):
                    current_color = BLACK
                    continue

                if my > TOP_PANEL:
                    drawing = True
                    start_pos = clamp_to_canvas(event.pos)
                    last_pos = start_pos

                    if tool == "brush":
                        pygame.draw.circle(canvas, current_color, start_pos, brush_size)

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                pos = clamp_to_canvas(event.pos)

                if tool == "brush":
                    draw_line(canvas, current_color, last_pos, pos, brush_size)

                elif tool == "eraser":
                    draw_line(canvas, WHITE, last_pos, pos, brush_size)

                last_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = clamp_to_canvas(event.pos)

                if tool == "rect":
                    rect = make_rect(start_pos, end_pos)
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                elif tool == "square":
                    rect = get_square_rect(start_pos, end_pos)
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif tool == "right_triangle":
                    points = get_right_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, current_color, points, 2)

                elif tool == "equilateral_triangle":
                    points = get_equilateral_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, current_color, points, 2)

                elif tool == "rhombus":
                    points = get_rhombus_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, current_color, points, 2)

                drawing = False
                start_pos = None
                last_pos = None

    screen.fill(GRAY)
    screen.blit(canvas, (0, 0))

    pygame.draw.rect(screen, (235, 235, 235), (0, 0, WIDTH, TOP_PANEL))
    pygame.draw.line(screen, DARK_GRAY, (0, TOP_PANEL), (WIDTH, TOP_PANEL), 2)

    draw_text()
    draw_color_boxes()
    draw_preview()

    pygame.display.flip()
    clock.tick(60)