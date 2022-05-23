import pygame,sys
from setting import *
from plyer import Player
from ememy import Enemy
from bulletclass import*
from tile import Tile
# from main import sp1
r=0
class level:
    def __init__(self) :
        self.r=r
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.ig=pygame.image.load('../tiles/content/map.png')
        # self.ig1=pygame.image.load('../tiles/border.png')
        self.display_surface=pygame.display.get_surface()
        self.visible_sprites=pygame.sprite.Group()
        self.obstacles_sprites=pygame.sprite.Group()
        self.bullet_sprites=pygame.sprite.Group()
        self.creat_map()
        self.score=Bullet.sp1
        self.score1=Bullet.sp2
        self.font=pygame.font.Font('freesansbold.ttf',32)
    def show_score(self):
        
        self.score=Bullet.sp1
        self.score1=Bullet.sp2
        self.scorer=self.font.render("P1G:"+str(self.score),True,(225,225,225))
        self.screen.blit(self.scorer,(50,40))
    def show_score1(self):
        self.score=Bullet.sp1
        self.score1=Bullet.sp2
        self.scorer=self.font.render("P2B:"+str(self.score1),True,(225,225,225))
        self.screen.blit(self.scorer,(250,40))    

    def creat_map(self):
        # self.screen.fill('black')
        # self.screen.blit(self.ig,(64 ,64))
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x=col_index*TILESIZE
                y=row_index*TILESIZE
                if col=='x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col=='P':
                    self.player=Player((x,y),[self.visible_sprites,self.obstacles_sprites],[self.visible_sprites,self.bullet_sprites])
                
                if col=='Y':
                    self.enemy=Enemy((x,y),[self.visible_sprites,self.obstacles_sprites],[self.visible_sprites,self.bullet_sprites])

    def run(self):
        # print(self.score,self.score1)
        self.screen.fill('black')
        self.screen.blit(self.ig,(0,0))
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        # self.screen.blit(self.ig1,(0,0))         
        self.show_score()
        self.show_score1()
        if self.score>110:
            # print('fff')
            return 2
        if self.score1>110:
            return 3
                   



            