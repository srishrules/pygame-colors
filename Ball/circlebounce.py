import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((100, 0, 200))
pygame.draw.circle(screen, (200, 200, 0), (250, 250), 100)
pygame.display.flip()
x,y=250,250
dy=50

running = True
while running:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    y+=dy
    bounce=False

    if y>=450 or y<=50:
        dy=-dy
        bounce=True
    
    screen.fill((100,0,200))     
    if bounce:
        rect=pygame.Rect(x-130,y-70,260,140)
        pygame.draw.ellipse(screen,(200,200,0),rect)
    else:
        pygame.draw.circle(screen,(200,200,0),(x,y),100)
    pygame.display.flip()  
pygame.quit()