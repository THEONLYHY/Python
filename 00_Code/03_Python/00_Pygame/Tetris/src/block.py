import pygame, sys
from pygame.locals import *
from const import *
from utils import *

#pygame.sprite.Sprite ：Simple base class for visible game objects.
class Block(pygame.sprite.Sprite):
    #类的构造方法
    def __init__(self, 
                 blockType,                 
                 blockShape, 
                 blockRotate, 
                 blockGroupIdx, 
                 baseRowIdx,
                 baseColIdx,
                 width, 
                 height, 
                 relPos):
        #调用父类的构造方法
        super().__init__()
        self.blockType = blockType
        self.blockShape = blockShape
        self.blockRotate = blockRotate
        self.blockGroupIdx = blockGroupIdx
        self.baseRowIdx = baseRowIdx
        self.baseColIdx = baseColIdx
        self.width = width
        self.height = height
        self.relPos = relPos
        
        self.blink = False
        self.blinkCount = 0
        self.LoadImage()
        self.UpdateImagePos()

    def StartBlink(self):
        self.blink = True
        self.blinkTime = GetCurrentTime()

    def LoadImage(self):
        #ps obj无image，从pygame中获得, BlockType是self的
        self.image = pygame.image.load(BLOCK_RES[self.blockType])
        #pygame.tranform.scale : resize to new resolution
        #重新设置图片的比列
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def UpdateImagePos(self):
        self.rect = self.image.get_rect()
        #箱子的宽度*第几个箱子
        self.rect.left = self.relPos[0] + self.width * self.ColIdx
        #箱子的高度*第几个箱子
        self.rect.top = self.relPos[1] + self.height * self.RowIdx 

    
    def Draw(self, surface):
        #
        self.UpdateImagePos()
        if self.blink and self.blinkCount % 2 == 0:
            return 
        surface.blit(self.image, self.rect)

    def Drop(self):
        self.baseRowIdx += 1

    #获取当前坐标
    def GetIndex(self):
        return (int(self.RowIdx), int(self.ColIdx))
    #获取下落的坐标
    def GetNextIndex(self):
        return (int(self.RowIdx + 1), int(self.ColIdx))

    def IsLeftBound(self):
        return self.ColIdx == 0
    
    def IsRightBound(self):
        return self.ColIdx == GAME_COL - 1
    
    def DoLeft(self):
        self.baseColIdx -= 1

    def DoRight(self):
        self.baseColIdx += 1
    
    def GetcolIdx(self):
        return self.ColIdx

    def DoRotate(self):
        self.blockRotate += 1
        if self.blockRotate >= len(BLOCK_SHAPE[self.blockShape]):
            self.blockRotate = 0
    
    def GetBlockConfigIndex(self):
        return BLOCK_SHAPE[self.blockShape][self.blockRotate][self.blockGroupIdx]
    
    @property
    def RowIdx(self):
        return self.baseRowIdx + self.GetBlockConfigIndex()[0]
    
    @property
    def ColIdx(self):
        return self.baseColIdx + self.GetBlockConfigIndex()[1]  
    
    def Update(self):
        if self.blink:
            diffTime = GetCurrentTime() - self.blinkTime
            self.blinkCount = int(diffTime / 30)