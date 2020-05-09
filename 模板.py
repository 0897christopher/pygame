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
pygame.init() 
(width, height) = ( 900 , 600 )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("解藥")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(YELLOW)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
            
    clock.tick(90)
    pygame.display.flip()
pygame.quit()