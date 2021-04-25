import pygame
import sys
import time
from setting import Settings
from person import Person
import Game as g
import Start

    
def run_game():
    gameSetting = Settings()
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((gameSetting.screenWidth, gameSetting.screenHeight))
    pygame.display.set_caption(gameSetting.caption)
    screen.fill(gameSetting.bgColor)
    person = Person()
    #text = person.name
    #g.print_text(screen, gameSetting, person, text)
    Start.start_game(screen, gameSetting, person)
    while True:
        g.check_event(screen, gameSetting, (0, 0), (0, 0))
        screen.fill(gameSetting.bgColor)
        pygame.display.update()



run_game()