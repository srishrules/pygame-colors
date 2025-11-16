import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((100, 0, 200))
pygame.draw.circle(screen, (200, 200, 0), (250, 250), 100)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()