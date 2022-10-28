import pygame

class Player:
    def __init__(self):
        self.pos_x = 200
        self.pos_y = 200
        
    def show_pos(self):
        print(f'{self.pos_x}, {self.pos_y}')