import sys
import pygame
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien


class Rocke_Fly:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("火箭大战")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_aliens()

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(120)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #响应按下
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.rocket.moving_up = True 
                if event.key == pygame.K_s:
                    self.rocket.moving_down = True
                if event.key == pygame.K_d:
                    self.rocket.moving_right = True
                if event.key == pygame.K_a:
                    self.rocket.moving_left = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
                if event.key == pygame.K_q:
                    sys.exit()
            
            #响应抬起
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.rocket.moving_up = False 
                if event.key == pygame.K_s:
                    self.rocket.moving_down = False
                if event.key == pygame.K_d:
                    self.rocket.moving_right = False
                if event.key == pygame.K_a:
                    self.rocket.moving_left = False
    
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self): 
        self.bullets.update( )
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet) 
        self._check_bullet_alien_collisions()
        
    def _create_aliens(self):
        alien = Alien(self)
        self.aliens.add(alien)
        current_x = alien.rect.x
        current_y = alien.rect.y
        while current_y < self.settings.screen_height:
            new_alien = Alien(self)
            self.aliens.add(new_alien)
            current_x -= self.settings.alien_speed
            current_y += 100
            new_alien.rect.x = current_x
            new_alien.rect.y = current_y        
    
    def _update_aliens(self):
        self.aliens.update()    
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True,True)
        if not self.aliens: 
            self.bullets.empty() 
            self._create_aliens()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.rocket.blitme()
        pygame.display.flip()



if __name__ =='__main__':
    rf=Rocke_Fly()
    rf.run_game()

