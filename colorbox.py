import pygame

pygame.init()
width,height=600,600
screen = pygame.display.set_mode((width,height))
screen.fill((0, 0, 0))

x,y,step,cell=0,0,8,10
for r in range(0,256,step):
    for g in range(0,256,step):
        for b in range(0,256,step):
            pygame.draw.rect(screen,(r,g,b),(x,y,cell,cell))
            x+=cell
            if x>=600:
                x=0
                y+=cell
            if y>=height:
                break
        if y>=height:
            break
    if y>=height:
        break
    
        
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()