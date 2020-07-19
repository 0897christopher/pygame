# -*- coding: utf-8 -*-
"""

Created on Sat Jun  6 14:52:31 2020

@author: 88690
"""
#client=客戶端
import paho.mqtt.client as mqtt
import pygame
import time

t = time.localtime()

MAXmsg = 16
SUBSCRIBE_USER = "christopher0202"
PUBLISH_USER = "Phoebe12345"

msgSend = ""
msgStr = ""
msgPos = 0

msgDICT = {}
msgSendDict = {}
msgSendPos = 0

result = time.strftime( "%m/%d %H:%M:%S", t )

def on_connect( client , userdata , flags , rc ):    
    print( "偶連接到惹" )   
    client.subscribe( SUBSCRIBE_USER )    
    
def on_message( client , userdata , msg ):
    print( msg.topic + " " + msg.payload.decode("utf-8") )
    
    global msgStr
    t = time.localtime()
    result = time.strftime("%m/%d %H:%M:%S", t)
    msgStr = msgStr + msg.payload.decode("utf-8")+ result  + "\n"
    msgDICT[result] = msg.payload.decode("utf=8")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect( "mqtt.eclipse.org" , 1883 , 65535)
client.loop_start()

WHITE = (255, 255, 255)
GREEN = ( 0, 255 , 0 )
RED = ( 255, 0 , 0 )
BLUE = ( 177, 241, 228 )
YELLOW = ( 255, 255, 0 )
BLACK = ( 0 , 0 , 0 )
ORANGE = ( 255 , 140 , 0 )
PINK = ( 255 , 20 , 147 )
BACKGROUND =( 234, 241, 248 )
ANOTHER_YELLOW = (0, 48, 101) 
LEFT_BUTTON = 1
RIGHT_BUTTON = 3

pygame.init() 
(width, height) = ( 1450 , 750 )
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font( "NotoSansCJKtc-Bold.otf" , 25 )
font2 = pygame.font.Font( "NotoSansCJKtc-Bold.otf" , 30 )
pygame.display.set_caption("解藥")
shift = False

Screen = 1
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client.loop_stop()
            running = False
        if event.type == pygame.MOUSEWHEEL:
            print(event.y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                client.publish( PUBLISH_USER , msgSend )
                t = time.localtime()
                result = time.strftime("%m/%d %H:%M:%S", t)
                msgSendDict[result] = msgSend
                msgSend = ""
                continue
            if event.key == pygame.K_BACKSPACE:
                msgSend = msgSend[ 0:len( msgSend ) - 1 ]
                continue
            if event.key >= 32 and event.key < 127:
                if shift :
                    event.key = event.key - 32
                print( chr(event.key) )
                msgSend = msgSend + chr( event.key ) 
            if event.key == pygame.K_LEFT :
                Screen = 1
            if event.key == pygame.K_RIGHT :
                Screen = 2
    
    key_pressed = pygame.key.get_pressed()
    if key_pressed[ pygame.K_LSHIFT ]:
        shift = True
    
    else:
        shift = False
        
        
        
        
    if key_pressed[ pygame.K_UP ]:
        if Screen == 2:
            msgSendPos = msgSendPos - 1
        else:
            msgPos = msgPos - 1
            
            
    if key_pressed[ pygame.K_DOWN ]:
        if Screen == 2:
            msgSendPos = msgSendPos + 1 
        else:
            msgPos = msgPos + 1            
        
    if Screen == 2:        
        pygame.draw.rect( screen , ANOTHER_YELLOW , [ 725 , 3 , 723 , 695 ] , 5 )
        pygame.draw.rect( screen , (255, 252, 179) , [ 728 , 8 , 717 , 685 ] , 0 )
    if Screen == 1:
        pygame.draw.rect( screen , ANOTHER_YELLOW , [ 1 , 3 , 725 , 695 ] , 5 )    
        pygame.draw.rect( screen , (255, 252, 179) , [ 4 , 8 , 717 , 685 ] , 0 )    

    pygame.draw.rect( screen , WHITE , [ 0 , 700 , 1450 , 50 ] , 0 )
    text = font.render( msgSend , False , ( 90, 90, 233 ))
    textRect = text.get_rect()        
    textRect.x = 10
    textRect.y = 705
    screen.blit( text , textRect )
    key_list = list(msgDICT.keys())
    val_list = list(msgDICT.values())
    x = 8
    y = 5
    startIndex = msgPos
    if msgPos >= len(key_list) - MAXmsg:
        msgPos = len(key_list) -MAXmsg
    if msgPos < 0:
        msgPos = 0
    cnt = 0
    for i in range(len(key_list)):
        if i < startIndex:
            continue
        if cnt >= MAXmsg:
            break
        msgStr = val_list[i] +  "   " + key_list[i]
        
        text = font.render( msgStr , True ,  ( 51, 51, 255 ) )
        textRect = text.get_rect()        
        textRect.y = y
        textRect.x = x
      
        screen.blit( text , textRect )        
        y = y + 42
        cnt = cnt + 1     
    
        
    key_list = list(msgSendDict.keys())
    val_list = list(msgSendDict.values())
    x = 733
    y = 5
    startIndex2 = msgSendPos
    if msgSendPos >= len(key_list) - MAXmsg:
        msgSendPos = len(key_list) -MAXmsg
    if msgSendPos < 0:
        msgSendPos = 0
    cnt = 0
    for i in range(len(key_list)):
        if i < startIndex2:
            continue
        if cnt >= MAXmsg:
            break
        msgStr = val_list[i] +  "   " + key_list[i]
        
        text = font.render( msgStr , True , ( 0, 210, 0 ))
        textRect = text.get_rect()        
        textRect.y = y
        textRect.x = x
        screen.blit( text , textRect )        
        y = y + 42
        cnt = cnt + 1
        
    clock.tick(90)
    pygame.display.flip()
pygame.quit()
