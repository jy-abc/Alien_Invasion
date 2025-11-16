import pygame
import sys
from time import sleep
import random

from setting import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from alien_bomb import AlienBomb
from shield import Shield

class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        #帧率控制
        self.clock=pygame.time.Clock()
        
        #参数设置
        self.settings=Settings()
        
        #创建屏幕对象screen、
        #飞船对象ship、
        #存储子弹bullet和外星人的编组alien、按钮button、盾牌shield
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect=self.screen.get_rect()
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        self.ship=Ship(self)
        self.bullets=Group()
        self.aliens=Group()
        self.alien_bombs=Group()
        self.play_button=Button(self,"play")
        self.shield=Shield(self)  
        
        #创建用于存储游戏统计信息的实例、积分牌
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        
        #加载音乐
        #sound_bomb爆炸声、sound_shoot发射声
        pygame.mixer.init()
        self.sound_bomb=pygame.mixer.Sound(self.settings.bomb)
        self.sound_shoot=pygame.mixer.Sound(self.settings.shoot)
        self.sound_bomb.set_volume(0.8)
        self.sound_shoot.set_volume(0.8)
        
        #创建外星人舰队
        self._create_fleet()
        
        #屏幕标题
        pygame.display.set_caption("Alien Invasion")  
        
        #设置游戏状态
        self.game_active=False
        
    def run_game(self):
        '''开始游戏的主循环'''
        
        #游戏主循环
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.shield.update()
                self._update_bullets()
                self._update_alien_bombs() 
                self._update_aliens() 
                
            self._update_screen()
            self.clock.tick(60)
            
    def _check_keydown_events(self,event):
        '''响应按键'''
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_TAB:   #当用户按TAB可重新开始游戏
            self._start_game()
        elif event.key==pygame.K_BACKSPACE: #当用户按backspace时退出游戏
            self.stats.save_high_score()
            sys.exit()
        
    def _check_keyup_events(self,event):
        '''相应松开'''
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stats.save_high_score()
                    sys.exit()      
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)  
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                

    def _update_screen(self):
        '''更新屏幕图像'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bomb in self.alien_bombs.sprites():
            bomb.draw_alien_bullet()
        self.ship.blitme()
        self.shield.draw_shield()
        self.aliens.draw(self.screen)
        
        #显示得分
        self.sb.show_score()
        
        #如果游戏处于非活动状态，绘制play按钮
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()
        
    def _update_bullets(self):
        '''更新子弹位置，删除已消失子弹'''
        self.bullets.update()
            
        #删除已消失子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()       
        
            
    def _check_bullet_alien_collisions(self):
        '''响应子弹和外星人的碰撞'''
        collsions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if collsions:
            for aliens in collsions.values():
                self.stats.score+=self.settings.alien_points*len(aliens)
                self.sound_bomb.play()  #碰撞发生爆炸声
                self.sb.prep_score()
                self.sb.check_high_score()
        
        #如果舰队被击落，删除现有子弹并生成新舰队
        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()
            
            #提高等级
            self.stats.level+=1
            self.sb.prep_level()
            
            self._create_fleet()       
        
    def _fire_bullet(self):
        '''如果还没有到达限制就发射一颗子弹'''
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            self.sound_shoot.play() #发射子弹发出发射声
            
    def _create_fleet(self):
        '''创建一个外星人舰队'''
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<(self.settings.screen_height-3*alien_height):
            while current_x<(self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_height
            
    def _create_alien(self,x_position,y_position):
        '''创建一个外星人'''
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        '''检查是否达到边缘，更新外星舰队所有外星人位置'''
        self._check_fleet_edges()
        self.aliens.update()
        
        #监测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            
        #检查是否有外星人到达屏幕下边缘
        self._check_aliens_bottom()
        
        #外星人随机发射炸弹
        self._alien_shoot()
        
    def _check_fleet_edges(self):
        '''有外星人到达边缘时转向'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        '''外星舰队向下移动并改变它们方向'''
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
        
    def _ship_hit(self):
        '''响应飞船和外星人的碰撞'''
        self.stats.ships_left-=1 
        self.sound_bomb.play()  #碰撞发出爆炸声
        self.sb.prep_ships()
        
        if self.stats.ships_left>0:   
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.shield.center_shield()
            
            #暂停
            sleep(0.5)
        else:
            self.game_active=False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        '''检查是否有外星人达到屏幕下边缘'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.settings.screen_height:
                self._ship_hit()
                break
            
    def _check_play_button(self,mouse_pos):
        '''若玩家单击play按钮开始新游戏'''
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()
            
            #隐藏光标
            pygame.mouse.set_visible(False)
            
    def _start_game(self):
        #还原游戏设置
        self.settings.initialize_dynamic_settings()
        
        #重置游戏统计信息
        self.stats.reset_stats()
        
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
              
        self.game_active=True
        
        #清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()
            
        #创建新的外星舰队
        self._create_fleet()
        self.ship.center_ship()
        self.shield.center_shield()
        
    def _alien_shoot(self):
        '''随机挑一个外星人发射炸弹'''
        if not self.aliens:
            return
        if random.random()<self.settings.alien_shoot_freq and len(self.alien_bombs)<self.settings.alien_bullet_limit:
            shooter=random.choice(self.aliens.sprites())
            bomb=AlienBomb(self,shooter) 
            self.alien_bombs.add(bomb)

            
    def _update_alien_bombs(self):
        '''更新所有外星人炸弹的位置并检测碰撞'''
        for bomb in self.alien_bombs.copy():
            bomb.down()
                
            #出界删除
            if bomb.rect.bottom>=self.screen_rect.bottom or bomb.rect.left>=self.screen_rect.right or bomb.rect.right<=0:
                self.alien_bombs.remove(bomb)
                continue
            
            #炸弹碰到盾牌无效
            if bomb.rect.colliderect(self.shield.rect):
                self.alien_bombs.remove(bomb)
                continue
            
            #响应炸弹与飞船的碰撞
            if bomb.rect.colliderect(self.ship.rect):
                self.alien_bombs.remove(bomb)
                self._ship_hit()        

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

