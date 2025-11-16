import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''飞船类'''
    def __init__(self,ai_game):
        super().__init__()
        
        #屏幕对象和设置
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        
        self.image=pygame.image.load(r"D:\app\vscode\Alien_Invasion\ship_photo.bmp")
        self.rect=self.image.get_rect() #获得图像矩形
        self.screen_rect=ai_game.screen.get_rect()  #获得屏幕矩形
        
        #将飞船放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom
        
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.y-=self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed_factor
        
        self.rect.x=self.x
        self.rect.y=self.y

        
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        '''将飞船放在屏幕中央底部'''
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        