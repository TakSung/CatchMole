import __init__
from typing import List
import pygame as pg
import sys
import time
from pygame.locals import *
import random
from icecream import ic

from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard
from Application.GameManage import PlayerActionSet
from Game.RoomManager import RoomManager

clock = pg.time.Clock()

WIDTH = 810
HEIGHT = 811
CELL_SIZE = WIDTH // 3
outline_thickness = 3

WHITE = (255, 255, 255)
BLACK = (0,0,0)
cursor_color = (0, 0, 255)

line_color = (0, 0, 0)

mole_image = pg.image.load("mole.png")
effect_image = pg.image.load('boom.png')
mole_image = pg.transform.scale(mole_image, (240, 200))
effect_image = pg.transform.scale(effect_image, (240, 200))

# pg.init()

fps = 30

screen = pg.display.set_mode((WIDTH, HEIGHT))
room_manager = RoomManager(3)


pg.display.set_caption("Test")

def move_cursor(key):
    global cursor_x, cursor_y
    global player
    
    if key == pg.K_UP:
        player.down()
    elif key == pg.K_DOWN:
        player.up()
    elif key == pg.K_LEFT:
        player.left()
    elif key == pg.K_RIGHT:
        player.right()
    elif key == pg.K_k:
        (attack_y,attack_x) = player.get_cursor()
        board.try_attack(attack_y, attack_x)
        effect = effect_image.get_rect(
                left=WIDTH / 3 * attack_x + 20, top=HEIGHT / 3 * attack_y + 20
            )
        screen.blit(effect_image, effect)
        
        
    (cursor_y, cursor_x) = player.get_cursor()
    room_manager.set_curser(cursor_y, cursor_x)
    

# 게임 변수 설정
player = PlayerActionSet(3)
cursor_x, cursor_y = 0, 0

def print_room(y:int, x:int, type:ObjectType, is_cursor:bool):
    rect_width, rect_height = 270,270
    X = WIDTH / 3 * x
    Y = HEIGHT / 3 * y
    pg.draw.rect(screen, BLACK, (X - outline_thickness, Y - outline_thickness,
                                     X + rect_width + outline_thickness * 2, Y + rect_height + outline_thickness * 2))
    pg.draw.rect(screen, WHITE, [X, Y, X+270, Y+270], 100)
    
    if is_cursor == True:
        cursor_pos_x = x * CELL_SIZE + CELL_SIZE // 2
        cursor_pos_y = y * CELL_SIZE + CELL_SIZE // 2
        pg.draw.circle(screen, cursor_color, (cursor_pos_x, cursor_pos_y), 100)
    match type:
        case ObjectType.BASIC_MOLE:
            mole = mole_image.get_rect(
                left=WIDTH / 3 * x + 20, top=HEIGHT / 3 * y + 20
            )
            screen.blit(mole_image,mole)
    
        
        


    
    

def game_initiating_window():
    # displaying over the screen
    # screen.blit(initiating_window, (0, 0))

    # updating the display
    pg.display.update()
    # time.sleep(3)
    screen.fill(WHITE)

    # drawing vertical lines
    pg.draw.line(screen, line_color, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(screen, line_color, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)

    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(screen, line_color, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
    pg.display.update()
    clock.tick(30)

class RoomUpdater(IMoleObserver):
    def __init__(self, room_manager:RoomManager):
        self.room_manager = room_manager
        
    def update_state(self, y: int, x: int, type:ObjectType) -> None:
        self.room_manager.set_obj(y,x,type)

pg.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pg.font.SysFont("Comic Sans MS", 30)
score = 0


def convert_score(type: ObjectType) -> int:
    match type:
        case ObjectType.BASIC_MOLE:
            return 1
        case _:
            return 0


board = MoleBoard(factory=TestObjFactory(4))
board.register_mole_observers([RoomUpdater(room_manager)])
# for y in range(3):
#     for x in range(3):
#         board.raise_obj(y, x, type=ObjectType.BASIC_MOLE)
        
import threading
import time     
def auto_raise():
    for _ in range(30): 
        time.sleep(4)
        xr = random.randrange(0, 3)
        yr = random.randrange(0, 3)
        ic("raise mole",xr, yr)
        board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)


threading.Thread(target=auto_raise).start()

game_initiating_window()

while True:
    if score >= 100:
        threading.Thread(target=auto_raise).start()
        score -= 9
    t = ObjectType.NONE
    event = pg.event.poll()  # 이벤트 처리
    
    if event.type == QUIT:
        pg.quit()
        sys.exit()
    elif event.type == pg.KEYDOWN:  # 키 입력을 처리
            move_cursor(event.key)
        # screen.fill(WHITE)
        
    # draw_board()
    # game_initiating_window()
    
    # 현재 커서 위치에 빨간색 원 그리기
    # cursor_pos_x = cursor_x * CELL_SIZE + CELL_SIZE // 2
    # cursor_pos_y = cursor_y * CELL_SIZE + CELL_SIZE // 2
    # pg.draw.circle(screen, cursor_color, (cursor_pos_x, cursor_pos_y), 100)
    
        
    score += convert_score(t)
    # for mole in moles:
    #     screen.blit(mole_image, mole)
    for item in room_manager.get_changed_list():
        (y,x,type,cursor) = item
        print_room(y,x,type,cursor)
    text_surface = my_font.render(f"Score : {score}", False, (0, 0, 0))
    screen.blit(text_surface, (0, 0))
    pg.display.update()
    room_manager.check_room()
    clock.tick(30)
    

pg.quit()