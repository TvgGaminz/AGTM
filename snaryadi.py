import pygame
from pygame.transform import scale
import math
class Projectile(pygame.sprite.Sprite):
    def __init__(self, hero, shoot_x, shoot_y, side):
        pygame.sprite.Sprite.__init__(self)
        # Координаты в комнате
        self.rect = pygame.Rect(hero.rect.x + hero.rect.width/2, hero.rect.y + hero.rect.height/2, 20, 20)
        # Владелец
        self.hero = hero
        self.side = side
        # Картинка
        if self.side == "hero":
            self.image = scale(pygame.image.load("ball.png"), (20, 20))
        else:
            self.image = scale(pygame.image.load("projecticle.png"), (20, 20))
        # Физическая скорость
        self.speed = 20
        # Рассчет координатной скорости
        self.xspeed = self.speed/(shoot_x**2+shoot_y**2)**0.5*shoot_x
        self.yspeed = self.speed/(shoot_x**2+shoot_y**2)**0.5*shoot_y

    def update(self, entities):
        # Двежение
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if not (self.rect.x in range(-20, 1024) and self.rect.y in range(-20, 786)):
            self.kill()
        
        #Проверка на касание
        for thing in entities:
            if self.rect.colliderect(thing.rect) and self.side != thing.side:
                thing.hp -= 0.5
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)