import pygame 
from pygame.sprite import Sprite

#管理子弹的类
class Bullet(Sprite):
    def __init__(self, rf_game): 
        
        #在⻜船的当前位置创建⼀个⼦弹对象
        super().__init__() 
        self.screen = rf_game.screen 
        self.settings = rf_game.settings
        self.color = self.settings.bullet_color 
         

        # 在(0,0)处创建⼀个表⽰⼦弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) 
        self.rect.midright = rf_game.rocket.rect.midright

        #存储⽤浮点数表⽰的⼦弹位置
        self.x = float(self.rect.x)


    def update(self): 
          
        #更新⼦弹的准确位置
        self.x += self.settings.bullet_speed 
        #更新表⽰⼦弹的rect的位置
        self.rect.x = self.x 
 
    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)