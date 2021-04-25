import time
import pygame
from pygame.locals import *
import sys
from setting import Settings

def check_event(screen, gameSetting, xlim, ylim):
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
           return check_key_down(event)
        elif event.type ==  MOUSEBUTTONDOWN:
            if xlim[0] < x < xlim[1] and ylim[0] < y < ylim[1]:
                print("click down")
                return "Click Down"
        
    return ''        

def check_key_down(event):
    key_num = event.key
    s = str(chr(key_num))
    return s

def print_text(screen, gameSetting, textString, size = 'Normal', place = (0, 0)):
    #screen.fill(gameSetting.bgColor)
    #print(textString)
    if size == 'Normal':
        text = gameSetting.myFont.render(textString, True, (0, 0, 0))
    if size == 'Small':
        text = gameSetting.mySmallFont.render(textString, True, (0, 0, 0))
    screen.blit(text, place)
    #pygame.display.update()

def set_button(screen, gameSetting, place, size, color, textString):
    screen.set_clip(place + size)
    screen.fill(color)
    text = gameSetting.mySmallFont.render(textString, True, (0, 0, 0))
    screen.blit(text, place)
    #x, y = pygame.mouse.get_pos()
    #if place[0] < x < place[0] + size[0] and place[1] < y < place[1] + size[1] and event.type == MOUSEBUTTONDOWN:
        #return True
    screen.set_clip()
    #pygame.display.update()
