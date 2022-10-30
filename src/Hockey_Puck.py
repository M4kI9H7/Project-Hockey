from pygame import mouse
from pygame import transform
from pygame import sprite
from pygame.math import Vector2
import SpriteManager
import math

class Hockey_Puck(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.pos = Vector2(x,y)
        self.spriteMan = SpriteManager.SpriteManager()
        self.og_image = self.spriteMan.req_image('Puck_Sprite')
        self.image = self.og_image
        self.rect = self.image.get_rect(center=(self.og_image.get_width()/2, self.og_image.get_height()/2))
        self.angle = Vector2(0, 0)
        self.move_vec = Vector2(0, 0)
        self.add()
        self.speed = 1

    def rotate(self):
        mouse_x, mouse_y = mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos[0], mouse_y - self.pos[1]
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image, self.rect = self.rot_center(self.og_image, self.rect, self.angle)
        print(self.rect.center)

    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        return rot_image,rot_rect

    def update(self):
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y
    