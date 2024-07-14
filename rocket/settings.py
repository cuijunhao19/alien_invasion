# 存储游戏《外星⼈⼊侵》中所有设置的类
class Settings:
    
    #初始化游戏的设置
    def __init__(self):
        
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255,192,203)
        
        #火箭的设置
        self.rocket_speed = 2.5

        #子弹设置
        self.bullet_speed = 4 
        self.bullet_width = 15 
        self.bullet_height = 3 
        self.bullet_color = (123, 21, 61)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1