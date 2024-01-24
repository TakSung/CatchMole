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
- 방향키로 커서 이동 and 스페이스바를 누러면 두더지를 잡을 수 있음
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

# 이미지 라이센스
| image        | url                                                         |
| ------------ | ----------------------------------------------------------- |
| hacker.png   | https://www.flaticon.com/kr/free-icon/hacker_4228171        |
| boomboom.png | https://kor.pngtree.com/freepng/bomb-explosion_2503362.html |
