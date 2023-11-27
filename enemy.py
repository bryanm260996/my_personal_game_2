import pygame
import random
from game_parameters import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('../assets/sprites/pizza.png').convert()
        self.image.set_colorkey((0,0,0))
        self.image= pygame.transform.flip(self.image, True, False)
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed= random.uniform(1,5)
        self.rect.center= (x,y)


    def update(self):
        self.y += self.speed
        self.rect.y= self.y

    def draw(self,surf):
        surf.blit(self.image, self.rect)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('../assets/sprites/burgerDouble.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed= random.uniform(1,5)
        self.rect.center= (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y= self.y

    def draw(self,surf):
        surf.blit(self.image, self.rect)

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('../assets/sprites/hotDog.png').convert()
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed= random.uniform(2,4)
        self.rect.center= (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x= self.x

    def draw(self,surf):
        surf.blit(self.image, self.rect)



enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies3= pygame.sprite.Group()

