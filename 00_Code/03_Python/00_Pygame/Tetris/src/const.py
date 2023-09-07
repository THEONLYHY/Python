
#定义游戏区域，行17，列10
GAME_ROW = 17
GAME_COL = 14

#定义方块的高、宽常量
BLOCK_SIZE_W = 32
BLOCK_SIZE_H= 32

#block颜色类型
class BlockType:
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    PURPLE = 5
    BLOCKTYPEMAX = 6

#block不同颜色对应不同路径
BLOCK_RES = {
    BlockType.RED: "./Tetris/pic/red.png",
    BlockType.ORANGE: "./Tetris/pic/orange.png",
    BlockType.YELLOW: "./Tetris/pic/yellow.png",
    BlockType.GREEN: "./Tetris/pic/green.png",
    BlockType.BLUE: "./Tetris/pic/blue.png",
    BlockType.PURPLE: "./Tetris/pic/purple.png",
}

#block的形状
BLOCK_SHAPE = [
    [((0,0), (0,1), (1,0), (1,1))],#方型
    [((0,0), (0,1), (0,2), (0,3)), ((0,0), (1,0), (2,0), (3,0))],#长条
    [((0,0), (0,1), (1,1), (2,2)), ((0,1), (1,0), (1,1), (2,0))],#Z型
    [((0,1), (1,0), (1,1), (1,2)), 
     ((1,0), (1,1), (1,2), (2,1)), 
     ((0,1), (1,0), (1,1), (2,1)), 
     ((0,1), (1,1), (1,2), (2,1))],#飞机型
]

#定义两种类型的方块，一种是静态的、一种是下落的
class BlockGroupType:
    FIXED = 0
    DROP = 1

