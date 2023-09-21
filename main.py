import pygame

pygame.init()

width, height = 800, 600
board = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Board")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

drawing = False

def draw(pos):
    pygame.draw.circle(board, BLACK, pos, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if drawing:
                    draw(event.pos)

    board.fill(WHITE)

    pygame.display.flip()

pygame.quit()
