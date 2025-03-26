import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 10
    mode = 'blue'  # Default drawing color
    tool = 'pen'  # Default tool
    drawing = False
    start_pos = None
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Tool selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'pen'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
                elif event.key == pygame.K_v:
                    tool = 'right_triangle'
                elif event.key == pygame.K_y:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_u:
                    tool = 'rhombus'
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True
                
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if tool == 'circle':
                    draw_circle(screen, start_pos, event.pos, mode)
                elif tool == 'rectangle':
                    draw_rectangle(screen, start_pos, event.pos, mode)
                elif tool == 'right_triangle':
                    draw_right_triangle(screen, start_pos, event.pos, mode)
                elif tool == 'equilateral_triangle':
                    draw_equilateral_triangle(screen, start_pos, event.pos, mode)
                elif tool == 'rhombus':
                    draw_rhombus(screen, start_pos, event.pos, mode)
                
            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'pen':
                    pygame.draw.circle(screen, get_color(mode), event.pos, radius)
                elif tool == 'eraser':
                    pygame.draw.circle(screen, BLACK, event.pos, radius)
                
        pygame.display.flip()
        clock.tick(600)


def get_color(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return WHITE


def draw_circle(screen, start, end, mode):
    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, get_color(mode), start, radius, 2)


def draw_rectangle(screen, start, end, mode):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(screen, get_color(mode), rect, 2)


def draw_right_triangle(screen, start, end, mode):
    pygame.draw.polygon(screen, get_color(mode), [start, (start[0], end[1]), end], 2)


def draw_equilateral_triangle(screen, start, end, mode):
    height = abs(end[1] - start[1])
    base = abs(end[0] - start[0])
    midpoint = ((start[0] + end[0]) // 2, start[1] - height)
    pygame.draw.polygon(screen, get_color(mode), [start, (end[0], start[1]), midpoint], 2)


def draw_rhombus(screen, start, end, mode):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    mid_x, mid_y = (start[0] + end[0]) // 2, (start[1] + end[1]) // 2
    points = [(mid_x, start[1]), (end[0], mid_y), (mid_x, end[1]), (start[0], mid_y)]
    pygame.draw.polygon(screen, get_color(mode), points, 2)

main()