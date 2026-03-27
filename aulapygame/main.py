import pygame

pygame.init()

tela = pygame.display.set_mode((500,500))

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
    tela.fill('#ffffff')
    pygame.draw.rect(tela, (0,100,200), (235,235,30,30))
    pygame.display.update()
pygame.quit()