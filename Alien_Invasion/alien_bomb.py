import pygame
from pygame.sprite import Sprite
from alien import Alien

class AlienBomb(Sprite):
    '''外星人投下炸弹'''
    def __init__(self,ai_game,alien):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        
        self.rect=pygame.Rect(0,0,self.settings.alien_bullet_width,self.settings.alien_bullet_height)
        self.rect.x=alien.rect.x
        self.rect.top=alien.rect.bottom
        
        self.y=float(self.rect.y)
        
        self.color=self.settings.alien_bullet_color
        self.speed_factor=self.settings.alien_bullet_speed_factor
        
    def down(self):
        '''向下移动炸弹'''
        self.y+=self.speed_factor
        self.rect.y=self.y
        
    def draw_alien_bullet(self):
        '''在屏幕绘制炸弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)