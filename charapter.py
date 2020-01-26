from snaryadi import *
import random

class Charapter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 3
        self.mana = 5
        #Метка для снаряда (snaryadi.py строка 31)
        self.side = "hero"
        #Хит-бокс
        self.rect = pygame.Rect(x, y, 80, 80)
        self.image = scale(pygame.image.load("mage.png"), (80, 80))
        #Скорость
        self.speed = 20
        self.dash = False
    
    #Запись нажатых клавиш
    def keys_update(self, keys):
        if not self.dash:
            self.keys = keys.copy()
        
        keys["shoot"] = False
    
    def update(self, snaryadi):
        #Прверка на ХП (умер/не умер)
        if self.hp <= 0:
            exit()
        
        #Дэш
        if self.keys["dash"]:
            self.side = "enemy"
            self.dash = True
            self.image = scale(pygame.image.load("mage phase.png"), (80, 80))
            self.speed = 30
        
        #Передвижение
        if self.keys["up"]:
            self.rect.y -= self.speed
        if self.keys["down"]:
            self.rect.y += self.speed
        if self.keys["left"]:
            self.rect.x -= self.speed
        if self.keys["right"]:
            self.rect.x += self.speed
        
        #Стрельба
        if self.keys["shoot"] and self.mana >= 1 and not self.dash:
            self.mana -= 1
            shoot_x = 0
            if self.keys["right_shoot"]:
                shoot_x = 1
            elif self.keys["left_shoot"]:
                shoot_x = -1
            
            shoot_y = 0
            if self.keys["down_shoot"]:
                shoot_y = 1
            elif self.keys["up_shoot"]:
                shoot_y = -1
            
            snaryadi.add(Projectile(self, shoot_x, shoot_y, self.side))

        #Проверка на касание границ
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(960, self.rect.x)
        self.rect.y = max(0, self.rect.y)
        self.rect.y = min(672, self.rect.y)

        #Регенерация маны
        if self.dash:
            if self.mana >= 0.5:
                self.mana -= 0.5
            else:
                self.dash = False
                self.side = "hero"
                self.image = scale(pygame.image.load("mage.png"), (80, 80))
                self.speed = 20
        elif self.mana < 5:
            self.mana += 0.08
        
    def draw(self, screen):
        self.camrect = self.rect
        screen.blit(self.image, self.camrect)