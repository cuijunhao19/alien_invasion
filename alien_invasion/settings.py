# 存储游戏《外星⼈⼊侵》中所有设置的类
class Settings:
    
    #初始化游戏的设置
    def __init__(self):
        
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255,255,255)
        
        #⻜船的设置
        self.ship_speed =5
        self.ship_limit = 3 

        #子弹设置
        self.bullet_speed = 7.0
        self.bullet_width = 4
        self.bullet_height = 12 
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表⽰向右移动,为-1表⽰向左移动 
        self.fleet_direction = 1.0
