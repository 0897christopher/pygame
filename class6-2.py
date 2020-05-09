# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:20:38 2020

@author: 88690
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:01:51 2020

@author: 88690
"""

import pygame
import math
import random

class target():
    def __init__( self , x , y , status , shape ):
        self.x = x
        self.y = y
        self.status = status
        self.shape = shape
    
    def setPos( self , x , y ):
        self.x = x
        self.y = y
        
    def setColor( self , color ):
        self.color = color
        
    def draw ( self , screen , w , h , color ):
        pygame.draw.rect( screen , color , [ self.x , self.y , w , h ])        
        

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

num = 500
rectList = []
for a in range(num):
    x = random.randrange( 50 , 850 )
    y = random.randrange( 50 , 550 )
    b = target( x , y , False , 0 )
    
    color = ( random.randrange( 0 , 255 ) , random.randrange( 0 , 255 ) , random.randrange( 0 , 255 ) )
    b.setColor(color)
    
    rectList.append(b)



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
        if ((abs(rectList[a].x - pos[0]) < 40) and (abs(rectList[a].y - pos[1]) < 40)) and rectList[a].status == False:
            rectList[a].status = True 
            point = point + 10 
            print(str(point))

 
    for a in range(num):
        if rectList[a].status == False : 
            rectList[a].draw( screen , 100 , 100 , rectList[a].color )
            #pygame.draw.rect( screen , rectList[a].color , [ rectList[a].x , rectList[a].y , 10 , 10 ])
   
    textPoint = font.render( str(point) , True , RED )      
    screen.blit( textPoint , (20 , 20) )
    
    
    
    pygame.draw.rect( screen , ORANGE , [ pos[0]-10 , pos[1]-10 , 50 , 50 ] )
    
        
            
    clock.tick(90)
    pygame.display.flip()
pygame.quit()