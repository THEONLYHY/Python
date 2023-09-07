
import pygame, sys
from pygame.locals import *
import random
import datetime
from datetime import *

# BLOCK_SHAPE = [
#     [(0,0), (0,1), (1,0), (1,1)],#方型
#     [(0,0), (0,1), (0,2), (0,3)],#长条
#     [(0,0), (0,1), (1,1), (2,2)],#Z型
#     [(0,1), (1,0), (1,1), (1,2)],#飞机型
# ]

# idx = random.randint(0, len(BLOCK_SHAPE) - 1)
# for x in range(len(BLOCK_SHAPE[idx])):
#     print("idx= ", idx, "x = ", x, "last = 0" ,BLOCK_SHAPE[idx][x][0])
#     print("idx = ", idx, "x = ", x , "last = 1", BLOCK_SHAPE[idx][x][1])

# exp = [(1,0)]
# print ("exp[0][0] = ", exp[0][0])
# print ("exp[0][1] = ", exp[0][1])

# config = {
    
# }
    
# numbers = [1, 2, 3]
# numbers.insert(1, 4)
# print (numbers)

# exp = {
#     "name" : "karre",
#     "age" : 13
# }

# print (exp)

# exp.pop("name")
# print (exp)
# print (exp["age"])

# exp1 = {
#     'Type' : 1,
#     'String' : 2
# }
# print (exp1['Type'])

class Test:
    def __init__(self):
        self._name = "karre"
        self._birthday = 2000
    
    # @property
    # def GetAgeWithProperty(self):
    #     age = datetime.now().year - self._birthday
    #     return age
    
    # def GetAgeWithoutProperty(self):
    #     age = datetime.now().year - self._birthday
    #     return age
    
    @property
    def birthday(self):
        return self._birthdays

test = Test()
print(test._birthday)
test.birthday = 1000
print(test._birthday)


# print(test._name)
# #有property就可以无需()，当做访问属性一样访问
# print(test.GetAgeWithProperty)
# print(test.GetAgeWithoutProperty())