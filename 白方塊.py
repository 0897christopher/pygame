# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:27:28 2020

@author: 88690
"""

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
pygame.display.set_caption("中毒")

clock = pygame.time.Clock()
running = True
moving = False
xDiff = 0
xDir = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            moving = True
            xDiff = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT_BUTTON:
            moving = True
            xDiff = 1
    if moving == True :
        xDiff = xDiff + xDir
        if xDiff > 30:
            xDir = -1
        if xDiff <= -30:
            xDir = 1
            
    #做事情    
    #pygame.draw.rect(screen, WHITE, [150, 100, 150, 100])  
    
    pygame.draw.circle( screen, YELLOW , ( 450 , 300 ) , 300 )
    
    pygame.draw.circle( screen, BLACK , ( 350 + xDiff , 200 ) , 70 )
    pygame.draw.circle( screen, BLACK , ( 550 + xDiff , 200 ) , 70 )
    
    #pygame.draw.lines( screen, RED , False , [( 250 , 100 ) , ( 1 , 100 ) , ( 256 , 50 ) , ( 50 , 10 ) , ( 41 , 17 ) , ( 96 , 87 )] , 5 )
    pygame.draw.polygon( screen, RED , [( 550 , 430+ xDiff ) , ( 350 , 430 ) , ( 450 , 500+ xDiff )])
    
    pygame.draw.ellipse(screen, PINK, [ 230 + xDiff , 300 + xDiff , 100 , 70 ])
    pygame.draw.ellipse(screen, PINK, [ 570 + xDiff , 300 + xDiff , 100 , 70 ])
    
    pygame.draw.arc(screen, ORANGE, [ 400, 220, 100, 140+ xDiff] , ( math.pi / 180 ) * 180 , ( math.pi / 180 ) * 360 , 7 )        
    clock.tick(90)
    pygame.display.flip()
pygame.quit()
  