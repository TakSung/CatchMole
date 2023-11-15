import __init__
from typing import List
import pygame as pg
import sys
import time
from pygame.locals import *
import random
from icecream import ic

from Domain.Interfaces.IBoardObserver import IBoardObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard


clock = pg.time.Clock() 
 
WIDTH = 810
HEIGHT = 810
 
white = (255, 255, 255)
 
line_color = (0, 0, 0)

mole_image = pg.image.load('mole.png')
mole_image = pg.transform.scale(mole_image, (240, 200))
 
 
# pg.init()
 
fps = 30
 
screen = pg.display.set_mode((WIDTH, HEIGHT))
 
pg.display.set_caption("Test")

def game_initiating_window():
 
    # displaying over the screen
    #screen.blit(initiating_window, (0, 0))
 
    # updating the display
    pg.display.update()
    # time.sleep(3)
    screen.fill(white)
 
    # drawing vertical lines
    pg.draw.line(screen, line_color, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(screen, line_color, (WIDTH / 3 * 2, 0),
                 (WIDTH / 3 * 2, HEIGHT), 7)
 
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(screen, line_color, (0, HEIGHT / 3 * 2),
                 (WIDTH, HEIGHT / 3 * 2), 7)
    pg.display.update()
    clock.tick(30)

class GUI_Printer(IBoardObserver):
    def update_board(self, type: List[List[ObjectType]]) -> None:
        row = len(type)
        col = len(type[0])
        
        moles = []

        for y in range(row):
            for x in range(col):
                match type[y][x]:
                    case ObjectType.BASIC_MOLE:
                        mole = mole_image.get_rect(left = WIDTH/3*x+20, top = HEIGHT/3*y+20)
                        moles.append(mole)
                    case _:
                        pass
        
        game_initiating_window()
        for mole in moles:
            screen.blit(mole_image, mole)
        pg.display.update()
        clock.tick(30)
            
board = MoleBoard(observers=[GUI_Printer()])


while True:
    event = pg.event.poll() #이벤트 처리
    if event.type == QUIT:
        pg.quit()
        sys.exit()
    elif event.type == KEYDOWN: # 키 입력시 키에 따른 공 위치 변화
        ## 램덤한 xrandom yrandom 구하기
        xr = random.randrange(0, 3)
        yr = random.randrange(0, 3)
        ic(xr, yr)
        board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)
        
    pg.display.update()
    clock.tick(30)

    
    

pg.quit() 
