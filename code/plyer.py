from tokenize import group
from turtle import pos
import pygame
# from setting import*
from bulletclass import*
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,bullet_sprite):
        super().__init__(groups)
        self.image=pygame.image.load('../tiles/content/right.png').convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2()
        self.bullet_sprites= bullet_sprite
        self.speed = 10
        self.pos=pos
        self.obstacle_sprites=groups[1]
        self.group=self.bullet_sprites
        # self.bullet=Bullet(pos,groups)
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            hj=0
            self.direction.y=-1
            self.direction.x=0
            self.image=pygame.image.load('../tiles/content/tank.png').convert_alpha()
            if keys[pygame.K_RCTRL]==1:
                # print(self.obstacle_sprites)
            # print("exe")
                self.bullet=Bullet(self.rect.center,self.group,hj,self.obstacle_sprites)
        elif keys[pygame.K_DOWN]:
            hj=1
            self.direction.y=1
            self.direction.x=0
            self.image=pygame.image.load('../tiles/content/down.png').convert_alpha()
            if keys[pygame.K_RCTRL]==1:
            # print("exe")
                self.bullet=Bullet(self.rect.center,self.group,hj,self.obstacle_sprites)
            
        # else:
        #     hj=0
        #     self.direction.y=0
            
            # if keys[pygame.K_SPACE]==1:
            # # print("exe")
            #     self.bullet=Bullet(self.rect.center,self.group,hj)
                 
        elif keys[pygame.K_RIGHT]:
            hj=2
            self.image=pygame.image.load('../tiles/content/left.png').convert_alpha()
            self.direction.x=1
            self.direction.y=0
            if keys[pygame.K_RCTRL]==1:
            # print("exe")
                self.bullet=Bullet(self.rect.center,self.group,hj,self.obstacle_sprites)
        elif keys[pygame.K_LEFT]:
            hj=3
            self.image=pygame.image.load('../tiles/content/right.png').convert_alpha()
            self.direction.x=-1
            self.direction.y=0
            if keys[pygame.K_RCTRL]==1:
            # print("exe")
                self.bullet=Bullet(self.rect.center,self.group,hj,self.obstacle_sprites)

        else:
            hj=2
            self.direction.x=0
            self.direction.y=0
            # if keys[pygame.K_SPACE]==1:
            # # print("exe")
            #     self.bullet=Bullet(self.rect.center,self.group,hj) 
        # if keys[pygame.K_SPACE]==1:
        #     # print("exe")
        #     self.bullet=Bullet(self.rect.center,self.group,t)
    def move(self,speed):
        if self.direction.magnitude()!=0:
            self.direction=self.direction.normalize()
        
        self.rect.center += self.direction*speed
        if self.rect.x<16:
            self.rect.x=16
        if self.rect.x>1200:
            self.rect.x=1200
        if self.rect.y<14:
            self.rect.y=14
        if self.rect.y>620:
            self.rect.y=620        
        # print(self.rect.center)
        # self.rect.x += self.direction.x*speed
        # self.collision('horizontal')
        # self.rect.y += self.direction.y*speed
        # self.collision('vertical')    
    # def collision(self,direction):
    #     if direction =='horizontal':
    #         for sprite in self.obstacle_sprites:
    #             if sprite.rect.colliderect(self.rect):
    #                 if self.direction.x > 0:
    #                     self.rect.right=sprite.rect.left
    #                 if self.direction.x < 0:
    #                     self.rect.left=sprite.rect.right 
    #     if direction =='vertical':
    #         for sprite in self.obstacle_sprites:
    #             if sprite.rect.colliderect(self.rect):
    #                 if self.direction.y > 0:
    #                     self.rect.bottom=sprite.rect.top
    #                 if self.direction.y < 0:
    #                     self.rect.top=sprite.rect.bottom                                       
    def update(self):
        # print(self.rect.center)
        self.input()
        self.move(self.speed)        