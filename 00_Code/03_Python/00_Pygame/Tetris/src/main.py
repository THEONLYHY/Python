import pygame, sys
from pygame.locals import *
from const import *
from game import *

import random

pygame.init()
DISPLAYSUF = pygame.display.set_mode((800, 600))
game = Game(DISPLAYSUF)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.Update()
    #每次移动画布的渲染不会去除上次渲染的结果，所以每次渲染都要把屏幕涂黑,(0,0,0)代表黑色RGB
    DISPLAYSUF.fill((0,0,0))
    game.Draw()

    pygame.display.update()


