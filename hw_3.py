# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:42:36 2020

@author: 88690
"""

import pygame
import math
import random

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
pygame.display.set_caption("武漢")

COLOR = [WHITE,GREEN ,RED,BLUE,YELLOW,BLACK,ORANGE,PINK]

X = 150
Y = 100
pygame.draw.rect(screen, WHITE, [ X, Y, 100, 100]) 


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    clock.tick(90)
    pygame.display.flip()
pygame.quit()