from snaryadi import *
import random

class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Метка для снаряда (snaryadi.py строка 31)
        self.side = "enemy"
        #Хит-бокс
        self.rect = pygame.Rect(x, y, 72, 66)
        #ХП (он необходим даже в этом случае т.к. Снаряды не распознают мелких врагов)
        self.hp = 0.5
        #Random koefficient (чем дольше бубылда не стреляет, тем больше шанс, что он(а) выстрелит)
        self.rk = 0
        #Текущая картинка в анимации
        self.anim = 1
        self.dth_anim = 1
        #Скорость
        self.speed = 5
    
    def update(self, snaryadi):
        global score
        #Проверка ХП (умер/не умер)
        if self.hp <= 0:
            if self.dth_anim < 4:
                self.image = scale(pygame.image.load("Splash/splash_"+str(self.dth_anim)+".png"), (72, 66))
                self.dth_anim += 1
                return 0
            else:
                fila = open("score.txt", 'r')
                score = int(fila.read())
                score += 10
                fila.close()
                fila = open("score.txt", 'w')
                fila.write(str(score))
                fila.close()
                self.kill()
                return 0
        
        #Анимация
        self.image = scale(pygame.image.load("Bubilda_animation\Bubilda_"+str(round(self.anim))+".png"), (72, 66))
        self.anim += 0.25
        if self.anim == 2.5:
            self.anim = 1

        #Стрельба
        if random.randint(self.rk, 40) == 40:
            snaryadi.add(Projectile(self, 0, 1, self.side))
            self.rk = 0
        else:
            self.rk += 1
        
        #Рандомное движение
        self.rect.x += random.randint(-self.speed, self.speed)
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(960, self.rect.x)
    def draw(self, screen):
        screen.blit(self.image, self.rect)