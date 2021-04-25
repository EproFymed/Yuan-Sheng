import pygame
pygame.font.init()
class Settings():
    def __init__(self):
        self.screenHeight = 480
        self.screenWidth = 640
        self.bgColor = (230, 230, 230)
        self.caption = "Yuan-Sheng-test"
        self.myFont = pygame.font.SysFont("Chilanka", 30)
        self.mySmallFont = pygame.font.SysFont("Chilanka", 20)