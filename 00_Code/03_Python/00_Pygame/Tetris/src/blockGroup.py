import pygame, sys
from pygame.locals import *
from const import *
from block import *
from utils import *
import random
import time

class BlockGroup(object):
    #生成方块组的配置信息
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        #方块类型和颜色都随机
        shapeIdx = random.randint(0, len(BLOCK_SHAPE) - 1)
        bType = random.randint(0, BlockType.BLOCKTYPEMAX - 1)
        rotIdx = 0
        #配置列表
        configList = []
        for i in range( len(BLOCK_SHAPE[shapeIdx][rotIdx]) ):
            config = {
                'blockType' : bType,
                'blockShape' : shapeIdx,
                'blockRot' : rotIdx,
                'blockGroupIdx' : i,
                'rowIdx' : rowIdx,
                'colIdx' : colIdx 
            }
            configList.append(config)
        return configList
    
    def __init__(self, 
                 blockGroupType, 
                 width, 
                 height, 
                 blockConfigList, 
                 relPos):
        super().__init__()
        self.blockGroupType = blockGroupType
        self.time = GetCurrentTime()
        self.pressTime = {}
        self.blocks = []
        self.dropInterval = 300
        self.isEliminating = False
        self.eliminatingTime = 3
        
        self.eliminateRow = 0

        for config in blockConfigList:
            blk = Block(config['blockType'], 
                        config['blockShape'],
                        config['blockRot'],
                        config['blockGroupIdx'],
                        config['rowIdx'],
                        config['colIdx'],
                        width, 
                        height, 
                        relPos)
            self.blocks.append(blk)


    def Update(self):
        oldTime = self.time
        curTime = GetCurrentTime()
        diffTime = curTime - oldTime
        #如果是下落类型方块才进行时间的判定
        if self.blockGroupType == BlockGroupType.DROP:
            if diffTime >= self.dropInterval:
                self.time = curTime
                for b in self.blocks:
                    b.Drop()
            self.KeyDownHandler()
        
        for blk in self.blocks:
            blk.Update()

        if self.IsEliminating():
            if GetCurrentTime() - self.eliminatingTime > 500:
                tmpBlocks = []
                for blk in self.blocks:
                    if blk.GetIndex()[0] != self.eliminateRow:
                        if blk.GetIndex()[0] < self.eliminateRow:
                            blk.Drop()
                        tmpBlocks.append(blk)
                self.blocks = tmpBlocks
                self.SetEliminate(False)


    def Draw(self, surface):
        for b in self.blocks:
            b.Draw(surface)

    def GetBlocks(self):
        return self.blocks
    
    def CleanBlocks(self):
        self.blocks = []

    def addBlock(self, blk):
        self.blocks.append(blk)
    
    def GetBlockIndexes(self):
        return [block.GetIndex() for block in self.blocks]
    
    def GetBlockNextIndexes(self):
        return [block.GetNextIndex() for block in self.blocks]
    
    def CheckAndSetPressTime(self, key):
        ret = False
        if GetCurrentTime() - self.pressTime.get(key, 0) > 30:
            ret = True  
        self.pressTime[key] = GetCurrentTime()
        return ret

    #控制移动
    def KeyDownHandler(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.CheckAndSetPressTime(K_LEFT):
            isMove = True
            for blk in self.blocks:
                if blk.IsLeftBound():
                    isMove = False
                    break
            if isMove:
                for blk in self.blocks:
                    blk.DoLeft()

        elif pressed[K_RIGHT] and self.CheckAndSetPressTime(K_RIGHT):
            isMove = True
            for blk in self.blocks:
                if blk.IsRightBound():
                    isMove = False
                    break
            if isMove:
                for blk in self.blocks:
                    blk.DoRight()

        if pressed[K_DOWN]:
            self.dropInterval = 30
        else:
            self.dropInterval = 800
        
        if pressed[K_UP] and self.CheckAndSetPressTime(K_UP):
            for blk in self.blocks:
                blk.DoRotate()

    def DoEliminate(self, row):
        self.SetEliminate(True)
        eliminateRow = {}
        self.eliminateRow = row
        for col in range(0, GAME_COL):
            idx = (row, col)
            eliminateRow[idx] = 1
        
        for blk in self.blocks:
            if eliminateRow.get( blk.GetIndex()):
                blk.StartBlink()


    def ProcessEliminate(self):

        hash = {}
        allIndexes = self.GetBlockIndexes()
        
        for idx in allIndexes:
            hash[idx] = 1

        for row in range(GAME_ROW - 1, -1, -1):
            full = True
            for col in range(0, GAME_COL):
                idx = (row, col)
                if not hash.get(idx):
                    full = False
                    break
            
            if full:
                self.DoEliminate(row)
                return
    
    def SetEliminate(self, bEI):
        self.isEliminating = bEI
        
    def IsEliminating(self):
        return self.isEliminating
