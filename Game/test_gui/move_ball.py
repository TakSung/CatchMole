# [공 움직이기](https://wikidocs.net/95024)
import pygame
import sys
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# 기본 세팅
pygame.init()
pygame.display.set_caption("Test Window")
pygame.key.set_repeat(10,10)                 # 키입력 반복하는 정도 세팅
Surface = pygame.display.set_mode((500,400)) # 디스플레이 세팅
FPSCLOCK = pygame.time.Clock()

def main():
    # 초기 공위치 설정
    xpos = 100
    ypos = 100
    
    while True:
        Surface.fill(BLACK)
        for event in pygame.event.get(): # 누적된 이벤트 처리
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: # 키 입력시 키에 따른 공 위치 변화
                if event.key == K_LEFT:
                    xpos -= 10
                if event.key == K_RIGHT:
                    xpos += 10
                if event.key == K_UP:
                    ypos -= 10
                if event.key == K_DOWN:
                    ypos += 10
                    
        pygame.draw.circle(Surface, (WHITE), (xpos, ypos), 20) # 공 그리기
        pygame.display.update() #모든 화면 그리기 업데이트
        FPSCLOCK.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값
if __name__ == '__main__':
    main()
