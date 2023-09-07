import pygame, sys
from pygame.locals import*

pygame.init()


screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('你好')
screen.fill('white')

face = pygame.Surface((50, 50), flags = HWSURFACE)
face.fill(color = 'pink')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(face, (100, 100))
    pygame.display.flip()


