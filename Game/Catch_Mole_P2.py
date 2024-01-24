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
from Application.GameManage import PlayerCursorControl, OneBoardGameManager
from Application.StateFilter import DebuffFilter, ObjectPlayerLinker

from Game.RoomManager import RoomManager

clock = pg.time.Clock()

ALL_W = 1000
STATUS = 1000
HEIGHT = 800
BOARD_WIDTH = 800
CELL_SIZE = BOARD_WIDTH // 4
outline_thickness = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cursor_color = (0, 0, 255)

line_color = (0, 0, 0)

mole_image = pg.image.load("mole.png")
gold_mole_image = pg.image.load("gold_mole.png")
bomb_image = pg.image.load("bomb.webp")
hacker_image = pg.image.load("hacker.png")
effect_image = pg.image.load("boom.png")
red_bomb_image = pg.image.load("red_bomb.png")
mole_image = pg.transform.scale(mole_image, (120, 100))
gold_mole_image = pg.transform.scale(gold_mole_image, (120, 100))
hacker_image = pg.transform.scale(hacker_image, (120, 100))
effect_image = pg.transform.scale(effect_image, (120, 100))
bomb_image = pg.transform.scale(bomb_image, (120, 100))
red_bomb_image = pg.transform.scale(red_bomb_image, (120, 100))

fps = 30

game_screen = pg.display.set_mode((ALL_W, HEIGHT))
satus_screen = pg.display.set_mode((ALL_W, STATUS))
room_manager = RoomManager(4)


pg.display.set_caption("Test")


def move_cursor(key, player):
    global cursor_x, cursor_y
    global score

    (cursor_y, cursor_x) = player.get_cursor()
    if key == pg.K_UP:
        player.down()
    elif key == pg.K_DOWN:
        player.up()
    elif key == pg.K_LEFT:
        player.left()
    elif key == pg.K_RIGHT:
        player.right()
    elif key == pg.K_SPACE:
        t = player.try_attack()
        # effect = effect_image.get_rect(
        #     left=BOARD_WIDTH / 4 * cursor_x + 20, top=HEIGHT / 4 * cursor_y + 20
        # )
        # game_screen.blit(effect_image, effect)
        score += convert_score(t)

    (cursor_y, cursor_x) = player.get_cursor()
    room_manager.set_cursor(cursor_y, cursor_x)


def print_room(y: int, x: int, type: ObjectType, is_cursor: bool):
    rect_width, rect_height = 195, 195
    X = BOARD_WIDTH / 4 * x
    Y = HEIGHT / 4 * y
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
            mole = mole_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )
            game_screen.blit(mole_image, mole)
        case ObjectType.BOMB:
            bomb = bomb_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )
            game_screen.blit(bomb_image, bomb)
        case ObjectType.HACKER:
            hacker = hacker_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )
            game_screen.blit(hacker_image, hacker)
        case ObjectType.GOLD_MOLE:
            gold_mole = gold_mole_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )
            game_screen.blit(gold_mole_image, gold_mole)
        case ObjectType.RED_BOMB:
            red_bomb = red_bomb_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )
            game_screen.blit(red_bomb_image, red_bomb)


class RoomUpdater(IMoleObserver):
    def __init__(self, room_manager: RoomManager):
        self.room_manager = room_manager
        self.render_effect_image = None

    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        self.room_manager.set_obj(y, x, type)

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        if type == ObjectType.GOLD_MOLE and state == ObjectState.LOW:
            board.raise_obj(y, x, type=ObjectType.RED_BOMB)
        if state == ObjectState.CATCHED:
            self.render_effect_image = effect_image.get_rect(
                left=BOARD_WIDTH / 4 * x + 38, top=HEIGHT / 4 * y + 40
            )

    def rend_effect(self):
        if self.render_effect_image is not None:
            game_screen.blit(effect_image, self.render_effect_image)
            self.render_effect_image = None


# 게임 변수 설정
updater = RoomUpdater(room_manager)
board = MoleBoard(mole_observers=[updater])
debuff = DebuffFilter(3)
manager = OneBoardGameManager(
    board=board,
    player_num=2,
    debuff_filter=debuff,
)
player1 = manager.player_list[0]
player2 = manager.player_list[1]

pg.font.init()  # you have to call this at the start,
# if you want to use this module.
my_font = pg.font.SysFont("Comic Sans MS", 30)
score = 0


def convert_score(type: ObjectType) -> int:
    match type:
        case ObjectType.BASIC_MOLE:
            return 1
        case ObjectType.BOMB:
            return -3
        case ObjectType.GOLD_MOLE:
            return 20
        case ObjectType.RED_BOMB:
            return -10
        case ObjectType.HACKER:
            return 5
        case _:
            return 0


import threading
import time


def auto_raise():
    for _ in range(90):
        time.sleep(1)
        xr = random.randrange(0, 4)
        yr = random.randrange(0, 4)
        t = random.randrange(0, 1000)
        ic("raise mole", xr, yr)
        if t < 200:
            board.raise_obj(yr, xr, type=ObjectType.BOMB)
        elif t < 400:
            board.raise_obj(yr, xr, type=ObjectType.HACKER)
        elif t < 951:
            board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)
        else:
            board.raise_obj(yr, xr, type=ObjectType.GOLD_MOLE)


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
            move_cursor(event.key, player1)

        for item in room_manager.get_changed_list():
            (y, x, type, cursor) = item
            print_room(y, x, type, cursor)
        updater.rend_effect()
        text_surface = my_font.render(f"Score : {score}", False, (0, 0, 0))
        pg.draw.rect(game_screen, WHITE, [800, 0, 200, 800], 1000)
        game_screen.blit(text_surface, (810, 0))
        pg.display.update()
        room_manager.check_room()
        clock.tick(30)


pg.quit()
