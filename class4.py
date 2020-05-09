# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:53:51 2020

@author: 88690
"""

# -*- coding: utf-8 -*-

import random
import pygame
import math

WHITE = (255, 255, 255)
GREEN = ( 0, 255 , 0 )
RED = ( 255, 0 , 0 )
BLUE = ( 0 , 0 , 255 )
YELLOW = ( 255, 255, 0 )
BLACK = ( 0 , 0 , 0 )
ORANGE = ( 255 , 140 , 0 )
PINK = ( 255 , 20 , 147 )

LEFT_BUTTON = 1
RIGHT_BUTTON = 3
pygame.init() 
(width, height) = ( 900 , 600 )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("解藥")
COLOR = [WHITE,GREEN ,RED,BLUE,YELLOW,BLACK,ORANGE,PINK]
X = 150
Y = 100

pygame.mixer.music.load("哆啦A夢道具音效.mp3")
clock = pygame.time.Clock()
running = True
pygame.mixer.music.play(-1)
momo = pygame.image.load("錢幣.png").convert()
momoRect = momo.get_rect()
momo = pygame.transform.scale(momo,( 30, 30 ))
momo.set_colorkey(BLACK)
don = pygame.mixer.Sound("39ed0-16nct.ogg")


while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            don.play()
        if event.type == pygame.MOUSEMOTION:
            pygame.mouse.get_pos()
            momox = pygame.mouse.get_pos()[0]
            momoy = pygame.mouse.get_pos()[1]
           # pygame.draw.circle( screen , ORANGE , ( mouse_x , mouse_y ) , 10 )
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Y = Y - 15
                I = random.randrange(8)
                pygame.draw.rect(screen, COLOR[I], [X, Y, 100, 100])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X = X - 15 
                I = random.randrange(8)
                pygame.draw.rect(screen, COLOR[I], [X, Y, 100, 100])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                X = X + 15 
                I = random.randrange(8)
                pygame.draw.rect(screen, COLOR[I], [X, Y, 100, 100])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Y = Y + 15
                I = random.randrange(8)
                pygame.draw.rect(screen, COLOR[I], [X, Y, 100, 100])
    p = random.randrange(0,100)
    pygame.mixer.music.set_volume(p/500)
    #momox = random.randrange(0,900)
    #momoy = random.randrange(0,600)
    
    momoRect.x = momox
    momoRect.y = momoy
  
    screen.blit( momo , momoRect )
           # ( move_x , move_y ) = pygame.mouse.get_rel()
    clock.tick(100000)
    pygame.display.flip()
pygame.quit()