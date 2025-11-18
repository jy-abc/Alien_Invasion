import os

class Settings:
    def __init__(self):
        
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        
        #飞船设置
        self.ship_limit=3
        
        #子弹设置
        self.bullet_width=100
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        
        #外星人设置
        self.fleet_drop_speed=10
        
        #加快游戏的节奏
        self.speedup_scale=1.1
        
        #提分速度
        self.score_scale=1.5
        
        #外星人炸弹设置
        self.alien_bullet_width=10
        self.alien_bullet_height=15
        self.alien_bullet_color=220,20,60
        self.alien_shoot_freq=0.010
        self.alien_bullet_limit=3
        
        #盾牌设置
        self.shield_height=10
        self.shield_color=240,255,255
        
        #音乐设置
        self.sound_dir=r"sound"
        self.bomb=os.path.join(self.sound_dir,"bomb.wav")
        self.shoot=os.path.join(self.sound_dir,"shoot.wav")
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''初始化随游戏而变化的设置'''
        self.ship_speed_factor=4
        self.alien_bullet_speed_factor=0.8
        self.bullet_speed_factor=5
        self.alien_speed=3
        self.alien_points=50
        
        self.fleet_direction=1  #1向右，-1向左
        
    def increase_speed(self):
        '''提高速度'''
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_bullet_speed_factor*=self.speedup_scale
        
        self.alien_points=int(self.alien_points*self.score_scale)

        print(self.alien_points)



