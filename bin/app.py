import pygame
from pygame.math import Vector2
import sys
import Player
import Hockey_Puck
import math



def main():
    _SCREEN_WIDTH = 480
    _SCREEN_HEIGHT = 640

    pygame.init()
    pygame.display.set_caption("Pygame")
    screen = pygame.display.set_mode((_SCREEN_WIDTH, _SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player.Player(200, 200) #플레이어 생성
    puck = Hockey_Puck.Hockey_Puck(200,400) #퍽 생성
    
    print(puck.rect.center)

    while True:
        clock.tick(120) #프레임 120FPS 로 설정
        df = clock.tick(120) #프레임간 델타 시간
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        key_event = pygame.key.get_pressed() # 눌러진 키를 확인함
        if key_event[pygame.K_LEFT]:
            player.pos[0] -= 1 * df
        
        if key_event[pygame.K_RIGHT]:
            player.pos[0] += 1 * df
            
        if key_event[pygame.K_UP]:
            player.pos[1] -= 1 * df
        
        if key_event[pygame.K_DOWN]:
            player.pos[1] += 1 * df
            
        screen.fill((0,0,0)) # 화면을 검정색으로 채움
        
        player.update() #플레이어와 퍽에 있는 update() 함수 호출, 각각의 Rect라는 Collider 를 각자의 위치에 맞게 업데이트함
        puck.update()
        
        
        
        
        if (pygame.sprite.collide_mask(player, puck)):
            fDistance = math.sqrt(math.pow((player.pos[0] - puck.pos[0]), 2) + math.pow((player.pos[1] - puck.pos[1]), 2))
            puck.move_vec = [puck.pos[0] - player.pos[0], puck.pos[1] - player.pos[1]]
            puck.move_vec[0] = puck.move_vec[0] / fDistance
            puck.move_vec[1] = puck.move_vec[1] / fDistance
            
        if (puck.pos[0] < 0):
            if puck.move_vec[0] < 0:
                puck.move_vec[0] *= -1
            
        if (puck.pos[1] < 0):
            if puck.move_vec[1] < 0:
                puck.move_vec[1] *= -1
            
        if (puck.pos[0] + 64 > _SCREEN_WIDTH):
            if puck.move_vec[0] > 0:
                puck.move_vec[0] *= -1
            
        if (puck.pos[1] + 64 > _SCREEN_HEIGHT):
            if puck.move_vec[1] > 0:
                puck.move_vec[1] *= -1

        puck.move((puck.move_vec[0] * puck.speed * df ), (puck.move_vec[1] * puck.speed * df ))
        
        screen.blit(puck.image, (puck.pos[0], puck.pos[1]))
        screen.blit(player.image, (player.pos[0], player.pos[1]))
        
        pygame.display.update()
        

if (__name__ == '__main__'):
    main()