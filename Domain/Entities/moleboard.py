# from Domain.Interfaces.IBoard import IBoard
# from Common.ObjectType import OjectType
import random
a = random.randrange(0,3)
b = random.randrange(0,3)

Board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0] ]

Board[a][b] = 1

for x, y, z in Board:
    print(x,y,z)

#class moleboard(IBoard):

#if __name__ == '__main__':
    # 1 print board
    # 2 raise mole and print board
    # 3 random raise mole and print board