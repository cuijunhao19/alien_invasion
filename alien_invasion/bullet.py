import pygame 
from pygame.sprite import Sprite

#管理子弹的类
class Bullet(Sprite):
    def __init__(self, ai_game): 
        
        #在⻜船的当前位置创建⼀个⼦弹对象
        super().__init__() 
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color 
         


        # 在(0,0)处创建⼀个表⽰⼦弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) 
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储⽤浮点数表⽰的⼦弹位置
        self.y = float(self.rect.y)


    def update(self): 
          
        #更新⼦弹的准确位置
        self.y -= self.settings.bullet_speed 
        #更新表⽰⼦弹的rect的位置
        self.rect.y = self.y 
 
    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)