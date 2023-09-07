import pygame, sys
from pygame.locals import *
from blockGroup import *
from const import *


class Game(pygame.sprite.Sprite):
    def GetRelPos(self):
        return (240, 50)
    
    def __init__(self, surface):
        self.surface = surface
        self.fixedBlockGroup = BlockGroup(BlockGroupType.FIXED, BLOCK_SIZE_W, BLOCK_SIZE_H, [], self.GetRelPos())
        self.dropBlockGroup = None

    def GenerateDropBlockGroup(self):
        #从屏幕上方中间位置开始生成
        conf = BlockGroup.GenerateBlockGroupConfig(0, GAME_COL/2 - 1)
        self.dropBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.GetRelPos())

    #碰撞检测，将静态的block全部映射到hash中，如果下落的位置在hash中能找到，那就说明进行了碰撞，返回True;如果超过游戏所给行数也返回True
    def WillCollide(self):
        hash = {}
        allIndexes = self.fixedBlockGroup.GetBlockIndexes()
        for idx in allIndexes:
            hash[idx] = 1
        dropIndexes = self.dropBlockGroup.GetBlockNextIndexes()

        for dropIndex in dropIndexes:
            if hash.get(dropIndex):
                return True
            if dropIndex[0] >= GAME_ROW:
                return True
        return False
    
    def Update(self):
        self.fixedBlockGroup.Update()
        #如果有下落的就直接更新
        if self.dropBlockGroup:
            self.dropBlockGroup.Update()
        else:#否则就生成新的下落的
            self.GenerateDropBlockGroup()

        #如果发生碰撞，将碰撞的下落方块合并到静态方块中,再将下落的方块置空    
        if self.WillCollide():
            blocks = self.dropBlockGroup.GetBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlock(blk)
            self.dropBlockGroup.CleanBlocks()
            self.dropBlockGroup = None

    def Draw(self):
        self.fixedBlockGroup.Draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.Draw(self.surface)


    