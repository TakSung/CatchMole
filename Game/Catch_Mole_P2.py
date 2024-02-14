import __init__
from typing import List, Dict, Tuple, NamedTuple
import pygame as pg
import sys
import threading
import time
from pygame.locals import *
import random
from icecream import ic

from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common import ObjectType, ObjectState

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard
from Application.GameManage import PlayerActor, PlayerCursorControl, OneBoardGameManager
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
cursor_color: List[Tuple[int, int, int]] = [(0, 0, 125), (0, 125, 0)]

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
room_manager = RoomManager((4, 4), 2)

pg.display.set_caption("Test")

from collections import namedtuple


class KeyMatchDict(NamedTuple):
    up: int
    down: int
    left: int
    right: int
    attack: int


keycode_tuple: Tuple[KeyMatchDict, KeyMatchDict] = (
    KeyMatchDict(
        up=pg.K_KP8,
        down=pg.K_KP5,
        left=pg.K_KP4,
        right=pg.K_KP6,
        attack=pg.K_RETURN,
    ),
    KeyMatchDict(
        up=pg.K_w,
        down=pg.K_s,
        left=pg.K_a,
        right=pg.K_d,
        attack=pg.K_SPACE,
    ),
)


def move_cursor(key, player1: PlayerActor, player2: PlayerActor):
    global scores

    for i, keycode in enumerate(keycode_tuple):
        player = player1 if i == 0 else player2

        match key:
            case keycode.up:
                player.down()
            case keycode.down:
                player.up()
            case keycode.left:
                player.left()
            case keycode.right:
                player.right()
            case keycode.attack:
                t = player.try_attack()
                scores[i] += convert_score(t)
            case _:
                continue

        (cursor_y, cursor_x) = player.get_cursor()
        room_manager.set_cursor(cursor_y, cursor_x, i)
        break


def print_room(y: int, x: int, type: ObjectType, cursors: List[bool]):
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
    
    ic()
    print(cursors)
    ic(cursors)

    if cursors[0] == True:
        cursor_pos_x = x * CELL_SIZE + CELL_SIZE // 2 + 40
        cursor_pos_y = y * CELL_SIZE + CELL_SIZE // 2
        pg.draw.circle(game_screen, cursor_color[0], (cursor_pos_x, cursor_pos_y), 28)
    if cursors[1] == True:
        cursor_pos_x = x * CELL_SIZE + CELL_SIZE // 2 - 40
        cursor_pos_y = y * CELL_SIZE + CELL_SIZE // 2
        pg.draw.circle(game_screen, cursor_color[1], (cursor_pos_x, cursor_pos_y), 28)
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
scores: List[int] = [0, 0]


def convert_score(type: ObjectType) -> int:
    match type:
        case ObjectType.BASIC_MOLE:
            return 5
        case ObjectType.BOMB:
            return -3
        case ObjectType.GOLD_MOLE:
            return 60
        case ObjectType.RED_BOMB:
            return -20
        case _:
            return 0


end_event = threading.Event()


def auto_raise():
    for _ in range(90):
        if end_event.is_set():
            break
        time.sleep(1)
        xr = random.randrange(0, 4)
        yr = random.randrange(0, 4)
        t = random.randrange(0, 1000)
        ic("raise mole", xr, yr)
        try:
            if t < 200:
                board.raise_obj(yr, xr, type=ObjectType.BOMB)
            elif t < 300:
                board.raise_obj(yr, xr, type=ObjectType.HACKER)
            elif t < 951:
                board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)
            else:
                board.raise_obj(yr, xr, type=ObjectType.GOLD_MOLE)
        except:
            pass


timmer = 0


def tic_timer():
    global timmer
    while True:
        if end_event.is_set():
            break
        time.sleep(0.1)
        timmer += 1


game_screen.fill(WHITE)

threading.Thread(target=tic_timer).start()
threading.Thread(target=auto_raise).start()
target_score = 150
ic.disable()
end_flag = False
while not end_flag:
    for _ in range(500):
        for score in scores:
            if score >= target_score:
                end_event.set()
                end_flag = True
                break
        if end_flag:
            break
        t = ObjectType.none
        event = pg.event.poll()  # 이벤트 처리

        if event.type == QUIT:
            end_event.set()
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:  # 키 입력을 처리
            move_cursor(event.key, player1, player2)

        chaged_rooms = room_manager.get_changed_list()
        room_manager.check_room()

        for item in chaged_rooms:
            (y, x, type, cursors) = item
            print_room(y, x, type, cursors)
        updater.rend_effect()
        text_surface = my_font.render(f"Time : {timmer/10}", False, (0, 0, 0))
        pg.draw.rect(game_screen, WHITE, [800, 0, 200, 800], 1000)
        game_screen.blit(text_surface, (810, 0))
        for idx in range(2):
            y_pos = 40 + (idx * 40)
            text_surface = my_font.render(
                f"Score : {scores[idx]}", False, cursor_color[idx]
            )
            pg.draw.rect(game_screen, WHITE, [800, y_pos, 200, 800], 1000)
            game_screen.blit(text_surface, (810, y_pos))
        pg.display.update()
        clock.tick(30)
    threading.Thread(target=auto_raise).start()

winner = 0 if scores[0] > scores[1] else 1
text_surface = my_font.render(
    f"Congratulations! Winner is Player{(winner+1)}",
    False,
    cursor_color[winner],
)
pg.draw.rect(game_screen, WHITE, [0, 500, 1000, 540], 40)
game_screen.blit(text_surface, (210, 500))
pg.display.update()
time.sleep(5)
pg.quit()
