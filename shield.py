import pygame

class Shield:
    '''盾牌类'''
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.ship=ai_game.ship
        self.settings=ai_game.settings
        self.color=self.settings.shield_color
        self.screen_rect=ai_game.screen.get_rect()
        
        self.shield_width=self.ship.rect.width
        self.rect=pygame.Rect(0,0,self.shield_width,self.settings.shield_height)
        self.rect.centerx=self.ship.rect.centerx
        self.rect.bottom=self.ship.rect.top-10
        
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
    def update(self):
        '''根据移动标志调整盾牌位置'''
        if self.ship.moving_right and self.ship.rect.right<self.ship.screen_rect.right:
            self.x+=self.settings.ship_speed_factor
        if self.ship.moving_left and self.ship.rect.left>0:
            self.x-=self.settings.ship_speed_factor
        if self.ship.moving_up and self.ship.rect.top>0:
            self.y-=self.settings.ship_speed_factor
        if self.ship.moving_down and self.ship.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed_factor
        
        self.rect.x=self.x
        self.rect.y=self.y
        
    def draw_shield(self):
        '''在指定位置绘制盾牌'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        
    def center_shield(self):
        '''将盾牌放在屏幕中央底部的飞船之上'''
        self.rect.centerx=self.ship.rect.centerx
        self.rect.bottom=self.ship.rect.top-10
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        

        
