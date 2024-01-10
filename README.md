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
python Game/random_test_v3.py
```
### 게임방법
- 방향키
- K를 누러면 두더지를 잡을 수 있음

# Test
```bash
python -m unittest Tests/Domain/Entities/test_board.py Tests/Domain/Entities/test_mole.py Tests/Application/GameManage/test_player_cursor_control.py Tests/Application/StateFilter/test_player_filter.py Tests\Application\GameManage\test_game_manager_p2.py
python Game/random_test.py
python Game/random_test_v2.py
python Game/random_test_v3.py
python Game/random_test_v4.py
```

# 이미지 라이센스
| image        | url                                                         |
| ------------ | ----------------------------------------------------------- |
| hacker.png   | https://www.flaticon.com/kr/free-icon/hacker_4228171        |
| boomboom.png | https://kor.pngtree.com/freepng/bomb-explosion_2503362.html |
