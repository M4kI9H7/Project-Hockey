import pygame
from pygame.math import Vector2
import sys
import Player1
import Player2
import Hockey_Puck
import math



def main():
    _SCREEN_WIDTH = 480
    _SCREEN_HEIGHT = 640

    pygame.init()
    pygame.display.set_caption("Pygame")
    screen = pygame.display.set_mode((_SCREEN_WIDTH, _SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player1 = Player1.Player1(_SCREEN_WIDTH / 2 - 32, _SCREEN_HEIGHT-64) #플레이어 생성
    player2 = Player2.Player2(_SCREEN_WIDTH / 2 - 32, 0) #플레이어 생성
    puck = Hockey_Puck.Hockey_Puck(_SCREEN_WIDTH / 2 - 32, _SCREEN_HEIGHT / 2 - 32) #퍽 생성


    while True:
        clock.tick(120) #프레임 120FPS 로 설정
        df = clock.tick(120) #프레임간 델타 시간
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        key_event = pygame.key.get_pressed() # 눌러진 키를 확인함
        if key_event[pygame.K_LEFT]:
            player1.pos[0] -= 1 * df
        
        if key_event[pygame.K_RIGHT]:
            player1.pos[0] += 1 * df
            
        if key_event[pygame.K_UP]:
            player1.pos[1] -= 1 * df
        
        if key_event[pygame.K_DOWN]:
            player1.pos[1] += 1 * df
            
        key_event = pygame.key.get_pressed() # 눌러진 키를 확인함
        if key_event[pygame.K_a]:
            player2.pos[0] -= 1 * df
        
        if key_event[pygame.K_d]:
            player2.pos[0] += 1 * df
            
        if key_event[pygame.K_w]:
            player2.pos[1] -= 1 * df
        
        if key_event[pygame.K_s]:
            player2.pos[1] += 1 * df    
            
            
        screen.fill((0,0,0)) # 화면을 검정색으로 채움
        
        player1.update() #플레이어와 퍽에 있는 update() 함수 호출, 각각의 Rect라는 Collider 를 각자의 위치에 맞게 업데이트함
        player2.update()
        puck.update()
        
        
        # 하키 퍽이 화면 가장자리에서 튕기게 하는 로직
        if (puck.pos[0] < 0):
            if puck.move_vec[0] < 0: #하키 퍽이 화면 가장자리에서 무한정 이동방향을 반전시키지 않게 확인
                puck.move_vec[0] *= -1
            
        if (puck.pos[1] < 0):
            if puck.move_vec[1] < 0: #하키 퍽이 화면 가장자리에서 무한정 이동방향을 반전시키지 않게 확인
                puck.move_vec[1] *= -1
            
        if (puck.pos[0] + 64 > _SCREEN_WIDTH):
            if puck.move_vec[0] > 0: #하키 퍽이 화면 가장자리에서 무한정 이동방향을 반전시키지 않게 확인
                puck.move_vec[0] *= -1
            
        if (puck.pos[1] + 64 > _SCREEN_HEIGHT):
            if puck.move_vec[1] > 0: #하키 퍽이 화면 가장자리에서 무한정 이동방향을 반전시키지 않게 확인
                puck.move_vec[1] *= -1
                
        
        
        #플레이어와 하키 퍽이 충돌했을 때 로직
        if (pygame.sprite.collide_mask(player1, puck)):
            fDistance = math.sqrt(math.pow((player1.pos[0] - puck.pos[0]), 2) + math.pow((player1.pos[1] - puck.pos[1]), 2))
            puck.move_vec = [puck.pos[0] - player1.pos[0], puck.pos[1] - player1.pos[1]]
            puck.move_vec[0] = puck.move_vec[0] / fDistance
            puck.move_vec[1] = puck.move_vec[1] / fDistance
            
        #2번째 플레이어와 하키 퍽이 충돌했을 때를 구현해야 함
        if (pygame.sprite.collide_mask(player2, puck)):
            fDistance = math.sqrt(math.pow((player2.pos[0] - puck.pos[0]), 2) + math.pow((player2.pos[1] - puck.pos[1]), 2))
            puck.move_vec = [puck.pos[0] - player2.pos[0], puck.pos[1] - player2.pos[1]]
            puck.move_vec[0] = puck.move_vec[0] / fDistance
            puck.move_vec[1] = puck.move_vec[1] / fDistance
        #하키 퍽이 각 진영의 골에 도달했을 때 스코어를 올리고 게임 판을 초기화하는 로직을 구현해야 함
        
        #플레이어1, 플레이어2가 화면 가장자리를 벗어나지 못하게 하는 것을 구현해야 함
        if (player1.pos[0] < 0):
            player1.pos[0] = 0
        if (player1.pos[1] < 0):
            player1.pos[1] = 0
        if (player1.pos[0] + 64 > _SCREEN_WIDTH):
            player1.pos[0] = _SCREEN_WIDTH - 64
        if (player1.pos[1] + 64 > _SCREEN_HEIGHT):
            player1.pos[1] = _SCREEN_HEIGHT - 64
        
        if (player2.pos[0] < 0):
            player2.pos[0] = 0
        if (player2.pos[1] < 0):
            player2.pos[1] = 0
        if (player2.pos[0] + 64 > _SCREEN_WIDTH):
            player2.pos[0] = _SCREEN_WIDTH - 64
        if (player2.pos[1] + 64 > _SCREEN_HEIGHT):
            player2.pos[1] = _SCREEN_HEIGHT - 64
            
        
        #플레이어1, 플레이어2가 각각의 진영을 벗어나지 못하게 하는 것을 구현해야 함


        #하키 퍽의 x,y 위치를 이동방향(x,y) * 속도(1) * 프레임 델타의 값으로 움직임
        puck.move((puck.move_vec[0] * puck.speed * df ), (puck.move_vec[1] * puck.speed * df ))
        
        screen.blit(puck.image, (puck.pos[0], puck.pos[1]))
        screen.blit(player1.image, (player1.pos[0], player1.pos[1]))
        screen.blit(player2.image, (player2.pos[0], player2.pos[1]))
        
        pygame.display.update()

if (__name__ == '__main__'):
    main()
