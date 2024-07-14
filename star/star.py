import sys
import pygame
from random import randint
from ying import Ying

class Star:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("我是雷电将军的狗")
        self.yings = pygame.sprite.Group() 
        

    def run_game(self):
        while True:
            self._check()
            self._creat_yings()
            self._update_screen()

    def _check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _creat_yings(self):
        ying = Ying(self)
        self.yings.add(ying)
        # current_x = ying.rect.width
        # current_y = ying.rect.height
        n=0
        while n<1 :
            new_ying = Ying(self)
            new_ying.rect.x = randint(10,800)
            new_ying.rect.y = randint(10,800)
            self.yings.add(new_ying)
            n=n+1
        # while current_y <(600-2*ying.rect.height): 
        #     while current_x < (1000-2*ying.rect.width):
        #         new_ying = Ying(self)
        #         new_ying.rect.x = current_x
        #         new_ying.rect.y = current_y
        #         self.yings.add(new_ying)
        #         current_x += ying.rect.width
        #     current_x = ying.rect.width
        #     current_y += ying.rect.height

       
    
    def _update_screen(self):
        self.screen.fill((255,192,203))
        self.yings.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    st=Star()
    st.run_game()