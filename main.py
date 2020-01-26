from charapter import *
import time
from enemies import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

pygame.mixer.music.load("level_sound.mp3")
pygame.mixer.music.play()

#Список с позицией клавиш (нажата / не нажата)
keys_down = {"up":False, "down":False, "left":False, "right":False, "shoot":False, "up_shoot":False,
    "down_shoot":False, "left_shoot":False, "right_shoot":False, "dash":False}
#Генерация экрана
X = 1024
Y = 768
screen = pygame.display.set_mode()#####(X, Y), flags=pygame.FULLSCREEN)
#Генерация фона
background = pygame.image.load('bg.png')
canvas = scale(background, (X, Y))
#Генерация персонажа
herox = 512
heroy = 600
hero = Charapter(herox, heroy)
#Снаряды
snaryadi = pygame.sprite.Group()
#Объекты (персонаж, бубылды и др.)
entities = pygame.sprite.Group(hero)
#Random koefficient (чем больше времени не спавнились бубылды, тем больше шанс, что они заспавнятся)
rk = 0

font = pygame.font.Font("ARCADE_N.TTF", 40)

fila = open("score.txt", 'w')
fila.write("0")
fila.close()
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
            if event.key == pygame.K_a:
                keys_down["left"] = True
            if event.key == pygame.K_d:
                keys_down["right"] = True
            
            if event.key == pygame.K_k:
                keys_down["shoot"] = True
                keys_down["up_shoot"] = True
            if event.key == pygame.K_m:
                keys_down["shoot"] = True
                keys_down["down_shoot"] = True
            if event.key == pygame.K_n:
                keys_down["shoot"] = True
                keys_down["left_shoot"] = True
            if event.key == pygame.K_COMMA:
                keys_down["shoot"] = True
                keys_down["right_shoot"] = True
            if event.key == pygame.K_j:
                keys_down["dash"] = True

            if event.key == pygame.K_ESCAPE:
                exit()
            #Анимация пустышки (тест)
            if event.key == pygame.K_0:
                for i in range(9):
                    screen.blit(scale(pygame.image.load("Blank_animation/blank"+str(i+1)+".png"), (1024, 768)), (0, 0))
                    pygame.display.update()
                    screen.blit(canvas, (0, 0))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys_down["up"] = False
            if event.key == pygame.K_s:
                keys_down["down"] = False
            if event.key == pygame.K_a:
                keys_down["left"] = False
            if event.key == pygame.K_d:
                keys_down["right"] = False
            if event.key == pygame.K_j:
                keys_down["dash"] = False
            
            if event.key == pygame.K_k:
                keys_down["up_shoot"] = False
            if event.key == pygame.K_m:
                keys_down["down_shoot"] = False
            if event.key == pygame.K_n:
                keys_down["left_shoot"] = False
            if event.key == pygame.K_COMMA:
                keys_down["right_shoot"] = False
            if not (keys_down["up_shoot"] or keys_down["down_shoot"] or keys_down["left_shoot"] or keys_down["right_shoot"]):
                keys_down["shoot"] = False
    
    #Генерация бубылд
    if random.randint(rk, 100) == 100:
        if len(entities) < 10:
            entities.add(Slime(random.randint(0, 960), random.randint(0, 100)))
        rk = 0
    else:
        rk += 1
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

    #Рисовка ХПшек-нот
    for i in range(3):
        if i+1 <= hero.hp:
            img = "hp.png"
        else:
            if i+0.5 == hero.hp:
                img = "hp_half.png"
            else:
                img = "hp_null.png"
        screen.blit(scale(pygame.image.load(img), (60, 60)), (i*40, 672))
    #Рисовка маны
    for i in range(5):
        if i+1 <= hero.mana:
            img = "mannaya kasha/mana.png"
        else:
            img = "mannaya kasha/mana_null.png"
        screen.blit(
            scale(pygame.image.load(img), (60, 60)), (940 - i*60, 672)
        )
    
    fila = open("score.txt", 'r')
    score = fila.read()
    fila.close()
    txt = font.render("Score:"+str(score), True, (255, 255, 255))
    screen.blit(txt, (20, 20))
    #Обработка дисплея
    pygame.display.update()
    
    #Задержка для регулировки ФПС
    while time.time() < timer:
        pass
