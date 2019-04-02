#!/usr/bin/env python3
#-*- coding: utf8 -*-
import sys
import pygame#импорт модуля pygame
import random
pygame.init()#импортирует весь инструментарий pygame
WIN_WIDTH = 800
WIN_HEIGHT = 550
rooms = [i for i in range(20)]

def location():
    return random.choice(rooms)

def locations():
    random.shuffle(rooms)
    return rooms

def give_random_door_pic():
    seqpic = ['Door0.png','Door1.png','Door2.png','Door3.png','Door4.png','Door5.png','Door6.png','Door7.png','Door8.png','Door9.png','Door10.png','Door11.png']
    return random.choice(seqpic)

def begin():
    play = True
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT),pygame.RESIZABLE)#размер изменияем
    sc.fill((100, 150, 200))#заполнение цветом фона 
    f = pygame.font.SysFont('serif', 28)
    text = f.render("Помоги черепашке отнести её подруге - фруктовой летучей мыши", 1, (5, 75, 0)) 
    sc.blit(text, (10, 80))
    text2 = f.render("по имени Wumpus яблоки, чтобы она проснулась и поела.", 1, (0, 80, 0)) 
    sc.blit(text2, (25, 110))
    text3 = f.render("Чтобы начать, надо кликнуть по экрану.", 1, (10, 0, 60)) 
    sc.blit(text3, (90, 230))
    hero_surf = pygame.image.load('Hero.png')#загрузка изображения
    hero_surf = pygame.transform.scale(hero_surf, (300, 200))
    hero_rect = hero_surf.get_rect(bottomright=(600, 600))
    sc.blit(hero_surf, hero_rect)#наложить поверхность  
    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                play = False
            elif i.type == pygame.MOUSEBUTTONUP:
                return True  
        pygame.display.update()
        pygame.time.delay(40)
    return play

def game():
    thisgamerooms = locations()
    WUMPUS_LOCATION = thisgamerooms[0]
    HERO_LOCATION = thisgamerooms[1]
    DOORS = thisgamerooms[2:5]
    PIT = thisgamerooms[5:7]
    PORTAL = thisgamerooms[7]
    APPLES = 5
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))#экран размер
    sc.fill((100, 150, 200))#заполнение цветом фона    
    surf_left = pygame.Surface((WIN_WIDTH//3, WIN_HEIGHT))#левая поверхность, равная одной 3ти окна
    surf_left.fill((100, 150, 200))#заполнение цветом фона
    surf_middle = pygame.Surface((WIN_WIDTH//3, WIN_HEIGHT))#серединная поверхность, равная другой 3ти окна
    surf_middle.fill((100, 150, 200))#заполнение цветом фона
    surf_right = pygame.Surface((WIN_WIDTH//3, WIN_HEIGHT))#правая поверхность, равная другой 3ти окна
    surf_right.fill((100, 150, 200))#заполнение цветом фона
    sc.blit(surf_left, (0, 0))#разместить поверхности на главной
    sc.blit(surf_middle, (WIN_WIDTH//3, 0))#указывая координаты
    sc.blit(surf_right, ((WIN_WIDTH//3)*2, 0))#их верхних левых углов
    active_left = False#до первого клика - никакая
    active_middle = False#3ть НЕ активна
    active_right = False
    door_surf = pygame.image.load(give_random_door_pic())#двери
    door_surf = pygame.transform.scale(door_surf, (200, 250))
    sc.blit(door_surf, (0, 0))
    door_surf = pygame.image.load(give_random_door_pic())
    door_surf = pygame.transform.scale(door_surf, (200, 250))
    sc.blit(door_surf, ((WIN_WIDTH//3), 0))
    door_surf = pygame.image.load(give_random_door_pic())
    door_surf = pygame.transform.scale(door_surf, (200, 250))
    sc.blit(door_surf, ((WIN_WIDTH//3)*2, 0))
    while APPLES:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit() 
            elif i.type == pygame.MOUSEBUTTONUP:                
                if i.pos[0] < WIN_WIDTH//3:#клик меньше 3ти
                    active_left = True
                elif i.pos[0] < ((WIN_WIDTH//3)*2):
                    active_middle = True
                elif i.pos[0] > ((WIN_WIDTH//3)*2):
                    active_right = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    APPLES -= 1
                    if(DOORS[0] == WUMPUS_LOCATION):
                        return True 
                    if (random.random() > 0.25):
                        WUMPUS_LOCATION = location()
                elif i.key == pygame.K_UP:
                    APPLES -= 1
                    if(DOORS[1] == WUMPUS_LOCATION):
                        return True
                    if (random.random() > 0.25):
                        WUMPUS_LOCATION = location()
                elif i.key == pygame.K_RIGHT:
                    APPLES -= 1
                    if(DOORS[2] == WUMPUS_LOCATION):
                        return True
                    if (random.random() > 0.25):
                        WUMPUS_LOCATION = location()           
        if((PIT[0] in DOORS) or (PIT[1] in DOORS)):
            f = pygame.font.SysFont('serif', 18)
            textp = f.render("идёт сквозняк, какая-то из этих дверей ведёт на выход", 0, (15, 140, 5))
            sc.blit(textp, (9, 350))            
        if(PORTAL in DOORS):
            f = pygame.font.SysFont('serif', 18)
            texto = f.render("пахнет озоном, где-то рядом портал", 0, (15, 140, 5))
            sc.blit(texto, (9, 367)) 
        if(WUMPUS_LOCATION in DOORS):
            f = pygame.font.SysFont('serif', 18)
            texto = f.render("слышу дыхание спящей Wumpus", 0, (15, 140, 5))
            sc.blit(texto, (9, 380)) 
        f = pygame.font.SysFont('serif', 18)
        textapl = f.render("Осталось яблок: "+"_ "*APPLES+ str(APPLES), 0, (200, 0, 0))
        sc.blit(textapl, (9, 450)) 
        if(active_right or active_middle or active_left):
            sc.blit(surf_left, (0, 0))#заново левая поверхность 
            sc.blit(surf_middle, ((WIN_WIDTH//3), 0))#cередина
            sc.blit(surf_right, ((WIN_WIDTH//3)*2, 0))#правая
            sc.fill((100, 150, 200))#заполнение цветом фона
            door_surf = pygame.image.load(give_random_door_pic())#отрисовать
            door_surf = pygame.transform.scale(door_surf, (200, 250))#новые
            sc.blit(door_surf, (0, 0))#двери
            door_surf = pygame.image.load(give_random_door_pic())#загрузка изображения
            door_surf = pygame.transform.scale(door_surf, (200, 250))
            sc.blit(door_surf, ((WIN_WIDTH//3), 0))#наложить поверхность
            door_surf = pygame.image.load(give_random_door_pic())
            door_surf = pygame.transform.scale(door_surf, (200, 250))
            sc.blit(door_surf, ((WIN_WIDTH//3)*2, 0))
        if active_left:#активна левая поверхность              
            active_left = False
            HERO_LOCATION = DOORS[0]
        elif active_middle:#активна правая - то же самое            
            active_middle = False
            HERO_LOCATION = DOORS[1]
        elif active_right:
            active_right = False
            HERO_LOCATION = DOORS[2]
        if (HERO_LOCATION == PORTAL):#в портале
            HERO_LOCATION = location()
        if (WUMPUS_LOCATION == HERO_LOCATION):
            return True
        if (HERO_LOCATION in PIT):
            return False
        while(HERO_LOCATION in DOORS):
            thisgamerooms = locations()
            DOORS = thisgamerooms[0:3] 
        f = pygame.font.SysFont('serif', 30)#Какая комната
        textrn = f.render("Нажми на дверь, чтобы перейти. Номер этой комнаты: "+str(HERO_LOCATION), 1, (5, 0, 60)) 
        sc.blit(textrn, (50, 500))
        textns = f.render("Двери ведут в комнаты "+str(DOORS[0])+", "+str(DOORS[1])+", "+str(DOORS[2])+" ", 1, (22, 4, 160)) 
        sc.blit(textns, (10, 300))
        f = pygame.font.SysFont('serif', 19)#Какая комната
        texta = f.render("Вкатить яблоко в левую комнату -клавиша клавиатуры влево, в правую -вправо, среднюю -вверх", 0, (60, 10, 0))
        sc.blit(texta, (9, 400))
        pygame.display.update() 
    return False

def herowin():
    play = True
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    sc.fill((100, 150, 200))#заполнение цветом фона 
    f = pygame.font.SysFont('serif', 28)
    text = f.render("Ура", 1, (5, 75, 0)) 
    sc.blit(text, (10, 80))
    h_surf = pygame.image.load('Hero.png')#загрузка изображения
    h_surf = pygame.transform.scale(h_surf, (310, 210))
    h_rect = h_surf.get_rect(bottomright=(480, 480))
    sc.blit(h_surf, h_rect)#наложить поверхность  
    w_surf = pygame.image.load('Wumpus.png')
    w_surf = pygame.transform.scale(w_surf, (350, 250))
    w_rect = w_surf.get_rect(bottomright=(500, 300))
    sc.blit(w_surf, w_rect)#наложить поверхность 
    q_surf = pygame.image.load('quality.png')
    q_surf = pygame.transform.scale(q_surf, (300, 200))
    q_rect = q_surf.get_rect(bottomright=(800, 200))
    sc.blit(q_surf, q_rect)#наложить поверхность  
    apple_surf = pygame.image.load('apple.png')
    apple_surf = pygame.transform.scale(apple_surf, (250, 215))
    apple_rect = apple_surf.get_rect(topleft=(105, 150))
    sc.blit(apple_surf, apple_rect)#наложить поверхность 
    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                play = False
            elif i.type == pygame.MOUSEBUTTONUP:                
                play = False       
        pygame.display.update()
        pygame.time.delay(40)

def heroloose():
    play = True
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    sc.fill((100, 150, 200))#заполнение цветом фона 
    f = pygame.font.SysFont('serif', 28)
    textf = f.render("Cегодня черепаха не нашла летучую мышь, ", 1, (130, 35, 0)) 
    sc.blit(textf, (240, 190))
    textf = f.render("нажми на экран чтобы попытаться ещё раз.", 1, (130, 35, 0)) 
    sc.blit(textf, (260, 260))
    h_surf = pygame.image.load('Hero.png')#загрузка изображения
    h_surf = pygame.transform.scale(h_surf, (300, 200))
    h_rect = h_surf.get_rect(bottomright=(590, 590))
    sc.blit(h_surf, h_rect)#наложить поверхность  
    c_surf = pygame.image.load('cross.png')
    c_surf = pygame.transform.scale(c_surf, (300, 200))
    c_rect = c_surf.get_rect(bottomright=(400, 200))
    sc.blit(c_surf, c_rect)#наложить поверхность  
    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                play = False
            elif i.type == pygame.MOUSEBUTTONUP:
                return True  
        pygame.display.update()
        pygame.time.delay(40)
    return play

def main():
    docontinue = begin()  
    while docontinue:#continue True
        herow = game()
        if herow:
            herowin()
            docontinue = False
        else:
            docontinue = heroloose()
    exit()#выход

if __name__ == "__main__":
    main()
#=.= code by (ab)
