import pygame
from datetime import datetime
from tools2 import flood_fill, draw_rhombus, draw_equilateral_triangle, draw_right_triangle

pygame.init()

WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint Application")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 180, 0)
YELLOW = (255, 255, 0)
PURPLE = (150, 0, 150)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

font = pygame.font.SysFont("Arial", 22)

current_color = BLACK
brush_size = 2
current_tool = "pencil"

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_pos = None
text_value = ""


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    text1 = font.render("Tools: P Pencil | L Line | R Rect | C Circle | S Square | A RightTri | Q EqTri | H Rhombus | F Fill | T Text | E Eraser", True, BLACK)
    text2 = font.render("Brush: 1 Small|2 Medium | 3 Large Colors: B Black| G Green| U Blue| Y Yellow | D Red | Ctrl+S Save", True, BLACK)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))

    info = font.render(f"Tool: {current_tool} | Size: {brush_size}", True, RED)
    screen.blit(info, (760, 40))


def get_canvas_pos(pos):
    x, y = pos
    return x, y - TOOLBAR_HEIGHT


def save_canvas():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paint_{now}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)


def draw_shape(surface, tool, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    if tool == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "circle":
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        pygame.draw.circle(surface, color, start, radius, size)

    elif tool == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        if x2 < x1:
            x1 = x1 - side
        if y2 < y1:
            y1 = y1 - side
        rect = pygame.Rect(x1, y1, side, side)
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "right_triangle":
        draw_right_triangle(surface, color, start, end, size)

    elif tool == "equilateral_triangle":
        draw_equilateral_triangle(surface, color, start, end, size)

    elif tool == "rhombus":
        draw_rhombus(surface, color, start, end, size)


running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    mouse_pos = pygame.mouse.get_pos()

    if drawing and start_pos is not None and current_tool not in ["pencil", "eraser", "fill", "text"]:
        preview = canvas.copy()
        end_pos = get_canvas_pos(mouse_pos)
        draw_shape(preview, current_tool, current_color, start_pos, end_pos, brush_size)
        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    if text_mode:
        txt = font.render(text_value + "|", True, current_color)
        screen.blit(txt, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

    draw_toolbar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LCTRL] and event.key == pygame.K_s:
                save_canvas()

            elif text_mode:
                if event.key == pygame.K_RETURN:
                    final_text = font.render(text_value, True, current_color)
                    canvas.blit(final_text, text_pos)
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

                else:
                    text_value += event.unicode

            else:
                if event.key == pygame.K_p:
                    current_tool = "pencil"
                elif event.key == pygame.K_l:
                    current_tool = "line"
                elif event.key == pygame.K_r:
                    current_tool = "rect"
                elif event.key == pygame.K_c:
                    current_tool = "circle"
                elif event.key == pygame.K_s:
                    current_tool = "square"
                elif event.key == pygame.K_a:
                    current_tool = "right_triangle"
                elif event.key == pygame.K_q:
                    current_tool = "equilateral_triangle"
                elif event.key == pygame.K_h:
                    current_tool = "rhombus"
                elif event.key == pygame.K_f:
                    current_tool = "fill"
                elif event.key == pygame.K_t:
                    current_tool = "text"
                elif event.key == pygame.K_e:
                    current_tool = "eraser"

                elif event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_b:
                    current_color = BLACK
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_u:
                    current_color = BLUE
                elif event.key == pygame.K_y:
                    current_color = YELLOW
                elif event.key == pygame.K_d:
                    current_color = RED

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > TOOLBAR_HEIGHT:
                pos = get_canvas_pos(event.pos)

                if current_tool == "fill":
                    flood_fill(canvas, pos[0], pos[1], current_color)

                elif current_tool == "text":
                    text_mode = True
                    text_pos = pos
                    text_value = ""

                else:
                    drawing = True
                    start_pos = pos
                    last_pos = pos

        if event.type == pygame.MOUSEMOTION:
            if drawing and event.pos[1] > TOOLBAR_HEIGHT:
                pos = get_canvas_pos(event.pos)

                if current_tool == "pencil":
                    pygame.draw.line(canvas, current_color, last_pos, pos, brush_size)
                    last_pos = pos

                elif current_tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, pos, brush_size)
                    last_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and event.pos[1] > TOOLBAR_HEIGHT:
                end_pos = get_canvas_pos(event.pos)

                if current_tool not in ["pencil", "eraser"]:
                    draw_shape(canvas, current_tool, current_color, start_pos, end_pos, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

    pygame.display.update()
    clock.tick(60)

pygame.quit()