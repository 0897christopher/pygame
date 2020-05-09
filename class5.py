# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:01:51 2020

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
pygame.display.set_caption("wanna cry")

num = 50
rectList = []
for a in range(num):
    x = random.randrange( 50 , 850 )
    y = random.randrange( 50 , 550 )
    pos2 = []
    pos2.append(x)
    pos2.append(y)
    pos2.append(False)
    rectList.append(pos2)



clock = pygame.time.Clock()
running = True
point = 0
font = pygame.font.Font("hakidame.TTF" , 40 )
textGo = font.render( str(0) , True , RED )

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pos = pygame.mouse.get_pos()        
   
    for a in range(num): 
        if ((abs(rectList[a][0] - pos[0]) < 40) and (abs(rectList[a][1] - pos[1]) < 40)) and rectList[a][2] == False:
            rectList[a][2] = True 
            point = point + 10 
            print(str(point))

 
    for a in range(num):
        if rectList[a][2] == False : 
            pygame.draw.rect( screen , BLACK , [ rectList[a][0] , rectList[a][1] , 10 , 10 ])
   
    textPoint = font.render( str(point) , True , RED )      
    screen.blit( textPoint , (20 , 20) )
    
    
    
    pygame.draw.rect( screen , ORANGE , [ pos[0]-10 , pos[1]-10 , 50 , 50 ] )
    
        
            
    clock.tick(90)
    pygame.display.flip()
pygame.quit()