from snaryadi import *
import pygame

class Charapter(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 5
        #Метка для снаряда (snaryadi.py строка 31)
        self.side = "hero"
        #Хит-бокс
        self.rect = pygame.Rect(x, y, 256, 56)
        self.image = scale(pygame.image.load(image), (256, 56))
    
    #Запись нажатых клавиш
    def keys_update(self, keys):
        self.keys = keys
    
    def update(self, snaryadi):
        #Прверка на ХП (умер/не умер)
        if self.hp <= 0:
            exit()
        
        #Передвижение
        if self.keys["up"]:
            self.rect.y -= 60
        if self.keys["down"]:
            self.rect.y += 60

        
        #Стрельба
        if self.keys["shoot"] and (self.keys["up"] or self.keys["down"] or self.keys["left"] or self.keys["right"]):
            shoot_x = 0
            if self.keys["right"]:
                shoot_x = 1
            elif self.keys["left"]:
                shoot_x = -1
            
            shoot_y = 0
            if self.keys["down"]:
                shoot_y = 1
            elif self.keys["up"]:
                shoot_y = -1
            snaryadi.add(Projectile(self, shoot_x, shoot_y, self.side))

        #Проверка на касание границ
        self.rect.x = max(170, self.rect.x)
        self.rect.x = min(170, self.rect.x)
        self.rect.y = max(190, self.rect.y)
        self.rect.y = min(370, self.rect.y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
