import pygame
import os
from TOCmenus import TOCmenus
from TOCsaving import TOCsaving
from threeDisksTOC import threeDisks
from fourDisksTOC import fourDisks
from fiveDisksTOC import fiveDisks
from pygame import mixer


class towersOfCyberpunk:
    def __init__(self):
        pygame.init()
        mixer.music.load(os.path.join("Assets","FREE Blade Runner Type Music Fallen.mp3"))
        mixer.music.play(-1)
        self.winSizeWidth, self.winSizeHeight = 1200, 800
        self.win = pygame.display.set_mode((self.winSizeWidth, self.winSizeHeight))
        pygame.display.set_caption("Towers of Cyberpunk")
        self.saving = TOCsaving()
        self.menus = TOCmenus()
        self.menus.mainMenu(self.win, threeDisks, fourDisks, fiveDisks)
        
        
if __name__ == '__main__':
    towersOfCyberpunk()
    