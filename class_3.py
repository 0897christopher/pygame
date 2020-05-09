# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:23:25 2020

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
pygame.display.set_caption("解藥")

clock = pygame.time.Clock()
running = True

x = random.randrange( 0 , 900 )
y = random.randrange( -10000 , 0 )
v = random.randrange( 1 , 5 )

snow = []
for snow_flower in range( 10000 ):
    atr_snow = []
    atr_snow.append(x)
    atr_snow.append(y)
    atr_snow.append(v)

    snow.append( atr_snow )
    v = random.randrange( 1 , 5 )
    x = random.randrange( 0 , 900 )
    y = random.randrange( -10000 , 0 )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("635655")
                for snow_flower in range( len ( snow )):
                    snow[snow_flower][1] = 0
        
    v = random.randrange( 1 , 5 )
    screen.fill(BLACK)
    
    for snow_flower in range( len ( snow ) ):
        snow[snow_flower][2] = random.randrange( 1 , 5 )
        x1 = snow[snow_flower][0]
        y1 = snow[snow_flower][1]
        v1 = snow[snow_flower][2]
        

        pygame.draw.circle( screen , WHITE , ( x1 , y1 ) , 10 )
        snow[snow_flower][1] = snow[snow_flower][1] + snow[snow_flower][2]
        if snow[snow_flower][1] > 600:
            snow[snow_flower][1] = 0
    
    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()