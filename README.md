# [CatchMole](https://github.com/TakSung/CatchMole)
This is a whack-a-mole discussion project in python.

# How to Start

```bash
git clone https://github.com/TakSung/CatchMole.git
cd CatchMole
pip install -r requirements.txt
```

# Play Game
### EXE
```python
python Game/Catch_Mole_P1.py
```
### 게임방법 & 설명 
- 방향키로 커서 이동 and 스페이스바로 두더지를 잡을 수 있음
- 150점 이상 달성시 종료
- 두더지 잡으면 +1점 획득
- 해커를 누르면 방향키가 3초간 바뀜(버그 있음), 잡으면 5점
- 황금두더지는 7번 때려야 잡힘. 20점 획득, 2초안에 못잡으면 빨간폭탄 나옴
- 폭탄은 -3점, 빨간폭탄은 -10점 감점

# Test
```bash
python -m unittest Tests/Domain/Entities/test_board.py Tests/Domain/Entities/test_mole.py Tests/Application/GameManage/test_player_cursor_control.py Tests/Application/StateFilter/test_player_filter.py Tests\Application\GameManage\test_game_manager_p2.py
python Game/random_test.py
python Game/random_test_v2.py
python Game/random_test_v3.py
python Game/Catch_Mole_P1.py
```

# Bug
- 해커로 방향키가 바뀌었을 때, 제한시간이 끝나기 전에 해킹을 한번 더 하면, 두번째 해커가 적용이 안됨
> 그 이유는 Reversed 상태 전파 되면, Reversed 상태로 변경하고 시간을 타이머를 재서 Nomal 상태로 변경한다.
> 이 과정에서 갱신을 할 수 있는 로직인 없어서, 각자의 타이머는 개별로 돌아가고, 타이머가 돌면 이유없는 정상상태로 돌린다.

# 이미지 라이센스
| image        | url                                                         |
| ------------ | ----------------------------------------------------------- |
| hacker.png   | https://www.flaticon.com/kr/free-icon/hacker_4228171        |
| boomboom.png | https://kor.pngtree.com/freepng/bomb-explosion_2503362.html |
