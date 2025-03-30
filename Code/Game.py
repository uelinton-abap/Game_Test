import pygame

from Code.Const import WIN_WIDTH, WIN_HWIGHT
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HWIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


