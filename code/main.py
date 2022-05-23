from turtle import Screen, width
import pygame,sys
from bulletclass import Bullet
from setting import*
from level import level


class game:
    def __init__(self):
        # gernal setup
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.ig=pygame.image.load('../tiles/content/front.png')
        pygame.display.set_caption('tank')
        pygame.display.set_icon(pygame.image.load('../tiles/content/tank.png')) 
        self.clock=pygame.time.Clock()
        self.level=level()
    def run(self):
        t=0
        r=0
        while True:
            
            self.screen.fill('black')
            self.screen.blit(self.ig,(0,0))               
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                        t=1
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_5:
                        r=1    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_6:
                        r=0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_0:
                        pygame.QUIT
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_7:
                        Bullet.sp2=0
                        Bullet.sp1=0
                        return Game.run()        

                        
                                                 
            if r==1:
                self.screen.fill('black')
                self.yu=pygame.image.load('../tiles/content/control.png')
                self.screen.blit(self.yu,(0,0))
                
            
            if t==1:
                self.level.run()
                self.i=self.level.run()
                if self.i==2:
                    # print('fgg')
                    self.winimg=pygame.image.load('../tiles/content/win p1g.png')
                    self.screen.fill('black')
                    self.screen.blit(self.winimg,(0,0))
                if self.i==3:
                    # print('fgg')
                    self.winimg=pygame.image.load('../tiles/content/winp2g.png')
                    self.screen.fill('black')
                    self.screen.blit(self.winimg,(0,0))    

                  
                
            pygame.display.update()
            self.clock.tick(FPS)
if __name__=='__main__':
    Game=game()
    Game.run()
