import pygame

pygame.init()
width, height = 500,500
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))

cols = 100
rows = 100
cell_w = width // cols
cell_h = height // rows
x = y = 0

for row in range(rows):
    for col in range(cols):
        r = (col * 255) // (cols - 1)
        g = (row * 255) // (rows - 1)
        b = (abs(col - row) * 255) // (cols - 1)

        pygame.draw.rect(screen, (r, g, b),
        (col * cell_w, row * cell_h, cell_w, cell_h))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
