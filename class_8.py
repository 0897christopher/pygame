# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:08:00 2020

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

class block( pygame.sprite.Sprite ):
    def __init__ ( self , w , h ):
        super( block , self ).__init__()
        self.pygame = pygame
        self.w = w
        self.h = h
        #self.image = pygame.transform.scale( self.image , ( w , h ))
        self.image = pygame.Surface(( 100 , 60 ))
        self.color = ( random.randint( 60 , 255 ) , random.randint( 60 , 255 ) , random.randint( 60 , 255 ))
        self.image.fill( self.color )
        self.rect = self.image.get_rect()
        
        
    def getRect( self ):
        return self.rect
        
    def set_rect( self , x , y ):
        self.rect.x = x
        self.rect.y = y
        
    def draw ( self , screen ):
        screen.blit( self.image , self.rect )

class player( pygame.sprite.Sprite ):
    def __init__ ( self , w , h , imagePath ):
        super( player , self ).__init__()
        self.pygame = pygame
        self.w = w
        self.h = h
        self.image = pygame.image.load( imagePath ).convert()
        self.image = pygame.transform.scale( self.image , ( w , h ))
        #self.image = pygame.Surface(( 100 , 60 ))
        #self.color = ( random.randint( 60 , 255 ) , random.randint( 60 , 255 ) , random.randint( 60 , 255 ))
        #self.image.fill( self.color )
        self.rect = self.image.get_rect()
        self.image.set_colorkey( BLACK )

        
        
    def getRect( self ):
        return self.rect
        
    def set_rect( self , x , y ):
        self.rect.x = x
        self.rect.y = y
        
    def draw ( self , screen ):
        screen.blit( self.image , self.rect )
        
class ball( pygame.sprite.Sprite ):
    def __init__ ( self , w , h , imagePath ):
        super( ball , self ).__init__()
        self.pygame = pygame
        self.w = w
        self.h = h
        self.image = pygame.image.load( imagePath ).convert()
        self.image = pygame.transform.scale( self.image , ( w , h ))
        #self.image = pygame.Surface(( 100 , 60 ))
        #self.color = ( random.randint( 60 , 255 ) , random.randint( 60 , 255 ) , random.randint( 60 , 255 ))
        #self.image.fill( self.color )
        self.image.set_colorkey( WHITE )
        self.rect = self.image.get_rect()
        
        
    def getRect( self ):
        return self.rect
        
    def set_rect( self , x , y ):
        self.rect.x = x
        self.rect.y = y
        
    def draw ( self , screen ):
        screen.blit( self.image , self.rect )

LEFT_BUTTON = 1
RIGHT_BUTTON = 3
pygame.init() 
(width, height) = ( 900 , 800 )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("武漢肺炎")



clock = pygame.time.Clock()


blockList = pygame.sprite.Group()
player = player( 200 , 70 , "圖片1.png" )
ball = ball( 50 , 50 , "59355e3479426.png" )

ballXV = random.randrange( 1 , 5 )
ballYV = random.randrange( 1 , 5 )


for i in range( 8 ):
    for a in range( 5 ):
        target = block( 80 , 40 )
        target.set_rect( 11 * ( i + 1 ) + 100 * i , 70 * a + 10 )
        blockList.add( target )
    
    

running = True

while running:
    screen.fill( WHITE )
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            ( x , y ) = pygame.mouse.get_pos()
            
        if event.type == pygame.QUIT:
            running = False
    blockList.draw( screen )
    player.draw( screen )
    if x > 740:
        x = 740
    if x < 40:
        x = 40
    player.set_rect( x - 40 , 650 )
    ball.draw( screen )
    ball.set_rect( ball.rect.x + ballXV , ball.rect.y + ballYV )

        
    clock.tick(90)
    pygame.display.flip()
pygame.quit()