# from sys import ps1, ps2
from tkinter import CENTER
import pygame
# from level import*
# from ememy import*
from setting import*
# from main import sp1,sp2

class Bullet(pygame.sprite.Sprite):
    sp1=0
    sp2=0
    def __init__(self,pos,group,hj,obstacle_sprite):
        # self.lev=level().screen
        self.obstacle_sprites=obstacle_sprite
        self.hj=hj
        self.t=[]
        # self.sp1=sp1
        # self.sp2=sp2
        for i in self.obstacle_sprites:
            self.t.append(i)
        super().__init__(group)
        self.image=pygame.image.load('../tiles/content/bullet.png')
        if self.hj==0:
            self.rect=self.image.get_rect(center=(pos[0],pos[1]-68))
        elif self.hj==1:
            self.rect=self.image.get_rect(center=(pos[0],pos[1]+68))
        elif self.hj==2:
            self.rect=self.image.get_rect(center=(pos[0]+68,pos[1]))    
        elif self.hj==3:
            self.rect=self.image.get_rect(center=(pos[0]-68,pos[1]))
    def collision(self,direction):
        
        if direction =='horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    # print(1)
                    # if self.direction.x > 0:
                    #     self.rect.right=sprite.rect.left
                    # if self.direction.x < 0:
                        # self.rect.left=sprite.rect.right
                    self.rect.x=-40
                    self.rect.y=-40
                    if sprite==self.t[0]:
                        Bullet.sp1+=1
                    elif sprite==self.t[1]:
                        Bullet.sp2+=1       
        if direction =='vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    # print(2)
                    # if self.direction.y > 0:
                    #     self.rect.bottom=sprite.rect.top
                    # if self.direction.y < 0:
                    #     self.rect.top=sprite.rect.bottom
                    self.rect.x=-40
                    self.rect.y=-40
                    if sprite==self.t[0]:
                        Bullet.sp1+=1
                    elif sprite==self.t[1]:
                        Bullet.sp2+=1  
                    # print(type(sprite)) 
    # def score(self):
    #     print(sp1,sp2)
        # self.font=pygame.font.Font('freesansbold.ttf',30,True,(225,225,225))
        # self.font.render
        
        pass   
    def update(self):
        # self.score()
        # print(Bullet.sp1,Bullet.sp2)

        # print(self.rect.center)
        # self.rect.x += self.direction.x*20
        self.collision('horizontal')
        # self.rect.y += self.direction.y*20
        # self.collision('vertical')
        if self.hj==0: 
            self.rect.y-=20
            self.collision('horizontal')
        # self.rect.y += self.direction.y*20
            # self.collision('vertical')
        elif self.hj==1:
            self.rect.y+=20
            self.collision('horizontal')
        # self.rect.y += self.direction.y*20
            # self.collision('vertical')
        elif self.hj==2:
            self.rect.x+=20
            self.collision('horizontal')
        # self.rect.y += self.direction.y*20
            self.collision('vertical')
        elif self.hj==3:
            self.rect.x-=20 
            # self.collision('horizontal')
        # self.rect.y += self.direction.y*20
            self.collision('vertical')       
                
# class score:
#     def score(self):
#         if self.p1s==True:
#             print(1)         
                


