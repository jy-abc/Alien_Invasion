import os
import json

class GameStats:
    '''跟踪游戏的统计信息'''    
    def __init__(self,ai_game):
        self.high_score_path=r"high_score_path.json"
        self.settings=ai_game.settings
        self.high_score=self._get_high_score()
        self.reset_stats()
        
    def reset_stats(self):
        '''初始化游戏期间变化的统计信息'''
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1
        
    def _get_high_score(self):
        '''从文件中读取最高分,否则返回0'''
        try:
            with open(self.high_score_path,"r") as f:
                return int(json.load(f))
        except:
            return 0
        
    def save_high_score(self):
        '''将最高分存进文件'''
        with open(self.high_score_path,"w") as f:

            json.dump(self.high_score,f)

