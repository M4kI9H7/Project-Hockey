import pygame
import sys
import Player

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
df = pygame.time.get_ticks()


player = Player.Player()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        player.pos_x -= 1
    
    if key_event[pygame.K_RIGHT]:
        player.pos_x += 1
        
    screen.fill((0,0,0))
    

    pygame.draw.circle(screen, (255,255,255), (player.pos_x, player.pos_y), 20)
    
    pygame.display.update()