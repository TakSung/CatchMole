import __init__
from typing import List
import pygame as pg
import sys
import time
from pygame.locals import *
import random
from icecream import ic

from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common import ObjectType, ObjectState

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard
from Application.GameManage import PlayerActor
from Game.RoomManager import RoomManager

clock = pg.time.Clock()

WIDTH = 600
HEIGHT = 600
STATUS = 800
CELL_SIZE = WIDTH // 3
outline_thickness = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cursor_color = (0, 0, 255)

line_color = (0, 0, 0)

mole_image = pg.image.load("mole.png")
effect_image = pg.image.load("boom.png")
mole_image = pg.transform.scale(mole_image, (120, 100))
effect_image = pg.transform.scale(effect_image, (120, 00))

fps = 30

game_screen = pg.display.set_mode((WIDTH, HEIGHT))
satus_screen = pg.display.set_mode((WIDTH, STATUS))
room_manager = RoomManager(3)


pg.display.set_caption("Test")


def move_cursor(key):
    global cursor_x, cursor_y
    global player
    global score

    if key == pg.K_UP:
        player.down()
    elif key == pg.K_DOWN:
        player.up()
    elif key == pg.K_LEFT:
        player.left()
    elif key == pg.K_RIGHT:
        player.right()
    elif key == pg.K_k:
        (attack_y, attack_x) = player.get_cursor()
        t = board.try_attack(attack_y, attack_x)
        effect = effect_image.get_rect(
            left=WIDTH / 3 * attack_x + 20, top=HEIGHT / 3 * attack_y + 20
        )
        game_screen.blit(effect_image, effect)
        score += convert_score(t)

    (cursor_y, cursor_x) = player.get_cursor()
    room_manager.set_curser(cursor_y, cursor_x)


# 게임 변수 설정
player = PlayerActor(3)
cursor_x, cursor_y = 0, 0


def print_room(y: int, x: int, type: ObjectType, is_cursor: bool):
    rect_width, rect_height = 195, 195
    X = WIDTH / 3 * x
    Y = HEIGHT / 3 * y
    pg.draw.rect(
        game_screen,
        BLACK,
        (
            X - outline_thickness,
            Y - outline_thickness,
            rect_width + outline_thickness * 2,
            rect_height + outline_thickness * 2,
        ),
    )
    pg.draw.rect(game_screen, WHITE, [X, Y, 195, 195], 1000)

    if is_cursor == True:
        cursor_pos_x = x * CELL_SIZE + CELL_SIZE // 2
        cursor_pos_y = y * CELL_SIZE + CELL_SIZE // 2
        pg.draw.circle(game_screen, cursor_color, (cursor_pos_x, cursor_pos_y), 50)
    match type:
        case ObjectType.BASIC_MOLE:
            mole = mole_image.get_rect(left=WIDTH / 3 * x + 20, top=HEIGHT / 3 * y + 20)
            game_screen.blit(mole_image, mole)


class RoomUpdater(IMoleObserver):
    def __init__(self, room_manager: RoomManager):
        self.room_manager = room_manager

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        pass

    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        self.room_manager.set_obj(y, x, type)


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


board = MoleBoard(mole_observers=[RoomUpdater(room_manager)], factory=TestObjFactory(4))

import threading
import time


def auto_raise():
    for _ in range(90):
        time.sleep(1)
        xr = random.randrange(0, 3)
        yr = random.randrange(0, 3)
        ic("raise mole", xr, yr)
        board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)


game_screen.fill(WHITE)

while True:
    threading.Thread(target=auto_raise).start()

    for _ in range(500):
        t = ObjectType.none
        event = pg.event.poll()  # 이벤트 처리

        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # 키 입력을 처리
            move_cursor(event.key)

        for item in room_manager.get_changed_list():
            (y, x, type, cursor) = item
            print_room(y, x, type, cursor)
        text_surface = my_font.render(f"Score : {score}", False, (0, 0, 0))
        pg.draw.rect(game_screen, WHITE, [0, 600, 600, 200], 1000)
        game_screen.blit(text_surface, (0, 610))
        pg.display.update()
        room_manager.check_room()
        clock.tick(30)


pg.quit()
