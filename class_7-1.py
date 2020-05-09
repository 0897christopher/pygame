# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:27:28 2020

@author: 88690
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:21:58 2020

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



class Player ( pygame.sprite.Sprite ):
    def __init__ ( self , imagePath , w , h ):
        super( Player , self ).__init__()
        self.pygame = pygame
        self.image = pygame.image.load( imagePath ).convert()
        self.image = pygame.transform.scale( self.image , ( w , h ))
        #self.image = pygame.Surface(( 150 , 150 ))
        #self.image.fill( PINK )
        self.rect = self.image.get_rect()
        
        
    def getRect( self ):
        return self.rect
        
    def set_rect( self , x , y ):
        self.rect.x = x
        self.rect.y = y


pygame.init() 
(width, height) = ( 1300 , 900 )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("解藥")

player = Player( "91707475_519799302242864_2230823908015188391_n.jpg" , 700 , 670 )
#player1 = Player("走跳菲比.jpg")

playerList = pygame.sprite.Group()
player1List = pygame.sprite.Group()

for d in range(200):
    player1 = Player("走跳菲比.jpg" , 50 , 50 )
    player1.set_rect( random.randrange( 0 , 1300 ) , random.randrange( 0 , 900 ))
    player1List.add( player1 )
    

clock = pygame.time.Clock()
running = True

icon = pygame.image.load( "after effects.png" ).convert() 

pygame.display.set_icon( icon )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.set_rect( 100 , 10 )
    #player.rect.x = 200
    player1.set_rect( 1000 , 10 )
    #player.rect.y = 200
    screen.blit( player.image , player.rect )
    screen.blit( player1.image , player1.rect )
    
    player1List.draw( screen )
    print( player.getRect() )
    
    collide = pygame.sprite.spritecollide( player , player1List , False )
    if len( collide ):
        print( "collide : " + str(len(collide)))
    
    
             
    clock.tick(90)
    pygame.display.flip()
pygame.quit()