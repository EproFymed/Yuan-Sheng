import pygame
import time
import Game as g
def start_game(screen, gameSetting, person):
    #g.print_text(screen, gameSetting, "welcome to Yuan-Sheng World")   
    #time.sleep(3)
    get_name(screen, gameSetting, person)


def get_name(screen, gameSetting, person):
    string = ""
    reinput = ""#预处理器
    while True:
        reinput = g.check_event(screen, gameSetting, (100, 140), (50, 75))
        #string += g.check_event(screen, gameSetting, (100, 140), (50, 75))
        if reinput == "Click Down":
            break
        else:
            string += reinput
        #else:
        #   break
        #print(string)
        g.print_text(screen, gameSetting, "Please name yourself:_______")
        #pygame.display.update()
        g.print_text(screen, gameSetting, string, place = (300, 0))
        #pygame.display.update()
        g.set_button(screen, gameSetting, (100, 50), (40, 25), (255, 0, 0), "OK")
        #screen.set_clip(300, 0, 100, 20) # message box's location
        #screen.fill((47, 79, 79))
        pygame.display.update()
        #screen.set_clip()
       
