from re import S
import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pos_x = 200
pos_y = 200

while True:
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1
    
    if key_event[pygame.K_RIGHT]:
        pos_x += 1
        
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,255), (pos_x, pos_y), 20)
    
    pygame.display.update()