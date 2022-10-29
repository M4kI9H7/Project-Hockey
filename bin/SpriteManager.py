import pygame

class SpriteManager:
    def __init__(self):
        self.PLAYER_SPRITE = pygame.image.load("sprite/hockey_paddle.png", "Player Hockey Paddle").convert_alpha()
        self.OPPONENT_SPRITE = pygame.image.load("sprite/hockey_paddle_opponent.png", "Opponent Hockey Paddle").convert_alpha()
        self.PUCK_SPRITE = pygame.image.load("sprite/hockey_puck.png", "Hockey Puck").convert_alpha()
        
        self.img_list = {'P_Sprite' : self.PLAYER_SPRITE,
                         'O_Sprite' : self.OPPONENT_SPRITE,
                         'Puck_Sprite' : self.PUCK_SPRITE
                        }
        print(self.PUCK_SPRITE.get_size())

    def req_image(self, SpriteName : str):
        try:
            return self.img_list[f'{SpriteName}']
        except Exception:
            print("해당 이름의 이미지가 존재하지 않음")
            exit()