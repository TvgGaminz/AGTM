from menu_choosing_bar import *
import time
from enemies import *
import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

pygame.mixer.music.load("menu_sound.mp3")
pygame.mixer.music.play()

#Список с позицией клавиш (нажата / не нажата)
keys_down = {"up":False, "down":False, "left":False, "right":False, "shoot":False}
#Генерация экрана
X = 1024
Y = 768
screen = pygame.display.set_mode((X, Y))
#Генерация фона
background = pygame.image.load('menu_bg.png')
canvas = scale(background, (X, Y))
#Геерация бокса выбора в меню 
herox = 170
heroy = 190
hero = Charapter(herox, heroy, "menu_choosing_thingy.png")
#Снаряды
snaryadi = pygame.sprite.Group()
#Объекты (персонаж, бубылды и др.)
entities = pygame.sprite.Group(hero)
#Random koefficient (чем больше времени не спавнились бубылды, тем больше шанс, что они заспавнятся)
rk = 0

while True:
    #Таймер для ФПС (строка 95)
    timer = time.time() + 0.03
    #Обработка экрана
    screen.blit(canvas, (0, 0))

    #Запись нажатых клавиш
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys_down["up"] = True
            if event.key == pygame.K_s:
                keys_down["down"] = True
            if event.key == pygame.K_j:
                #мы закрываем окно лончера, и открываем в другом окне то, что нам надо
                
                pygame.display.quit()
                
                if hero.rect.y==190:
                    print("Тут должна начинаться игра")
                    import main
                    
                elif hero.rect.y==250:
                    print("Тут должно открываться окно со статистикой")
                    print("В разаработке")
                elif hero.rect.y==310:
                    print("тут должен происходить бан")
                    print("В разаработке")
                elif hero.rect.y==370:
                    print("Тут должен открываться браузер с нашим сайтом (или что-то другое)")
                    print("В разаработке")
                
                    
            if event.key == pygame.K_ESCAPE:
                exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys_down["up"] = False
            if event.key == pygame.K_s:
                keys_down["down"] = False
    
    
    #Запись нажатых клавиш в персонажа
    hero.keys_update(keys_down)

    #Обработка entities (строка 23)
    for thing in entities:
        thing.update(snaryadi)
        thing.draw(screen)
    #Обработка снарядов (строка 21)
    for thing in snaryadi:
        thing.update(entities)
        thing.draw(screen)
        
    #Обработка дисплея
    pygame.display.update()
    
    #Задержка для регулировки ФПС
    while time.time() < timer:
        pass

    #print(hero.rect.x,hero.rect.y)