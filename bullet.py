import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''子弹'''
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.centerx=ai_game.ship.rect.centerx
        self.rect.top=ai_game.ship.rect.top
        
        self.y=float(self.rect.y)
        self.color=self.settings.bullet_color
        self.speed_factor=self.settings.bullet_speed_factor
        
    def update(self):
        '''向上移动子弹'''
        self.y-=self.speed_factor
        self.rect.y=self.y
    
    def draw_bullet(self):
        '''在屏幕绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)