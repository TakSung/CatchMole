import pygame as pg
import sys
import time
from pygame.locals import *
import random

clock = pg.time.Clock() 
 
width = 810
height = 810
 
white = (255, 255, 255)
 
line_color = (0, 0, 0)

mole_image = pg.image.load('mole.png')
mole_image = pg.transform.scale(mole_image,(230, 200))
moles = []
# for i in range(0,3):
#     for j in range(0,3):
#         mole = mole_image.get_rect(left = width/3*i+20, top = height/3*j+35)
#         moles.append(mole) 

def draw_mole(i, j):
    mole = mole_image.get_rect(left = width/3*i+20, top = height/3*j+35)
    moles.append(mole)
 
 
# pg.init()
 
fps = 30
 
screen = pg.display.set_mode((width, height))
 
pg.display.set_caption("Test")

def game_initiating_window():
 
    # displaying over the screen
    #screen.blit(initiating_window, (0, 0))
 
    # updating the display
    pg.display.update()
    # time.sleep(3)
    screen.fill(white)
 
    # drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0),
                 (width / 3 * 2, height), 7)
 
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    pg.display.update()
    clock.tick(30)



game_initiating_window()
while True:
    event = pg.event.poll() #이벤트 처리
    if event.type == QUIT:
        pg.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.type == K_a :
            draw_mole(1,1)
    # elif event.type == KEYDOWN: # 키 입력시 키에 따른 공 위치 변화
    #     if event.key == K_LEFT:
    #         pass
    #     if event.key == K_RIGHT:
    #         pass
    #     if event.key == K_UP:
    #         pass
    #     if event.key == K_DOWN:
    #         pass
    for mole in moles:
        screen.blit(mole_image, mole)
    pg.display.update()
    clock.tick(30)

pg.quit() 
