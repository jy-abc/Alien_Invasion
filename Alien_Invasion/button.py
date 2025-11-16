import pygame.font

class Button:
    '''游戏按钮'''
    def __init__(self,ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        
        #设置按钮尺寸、颜色
        self.width,self.height=200,50
        self.button_color=(0,135,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        
        self.rect=pygame.Rect(0,0,self.width,self.width)
        self.rect.center=self.screen_rect.center
        
        self._prep_msg(msg)
        
    def _prep_msg(self,msg):
        '''将msg渲染为图像,并在按钮中居中'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        '''绘制按钮和文本'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)