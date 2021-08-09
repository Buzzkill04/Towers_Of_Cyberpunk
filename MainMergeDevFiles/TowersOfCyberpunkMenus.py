import pygame
import os
from TOCsaving import TOCsaving

class TOCmenus:
    def __init__(self):
        pygame.font.init()
        pygame.init()
        self.fps = 10
        self.threeDisksWin = False
        self.fourDisksWin = False
        self.fiveDisksWin = False
        self.moveCount = 0
        self.playerName = "test"
        self.saving = TOCsaving()
        self.endSurfaceSizeWidth, self.endSurfaceSizeHeight = 1200, 800
        self.endScreenText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 60)
        self.endScreenTextOne = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
        self.backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
        self.towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))

    
    def drawWindow(self):
        pygame.display.update()
        
    def endScreenMenu(self, win):
        self.running = True
        while self.running:
            self.drawWindow()
            self.finishScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.finishScreen.set_alpha(150)
            self.finishScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.towersImage, (0, 0))
            win.blit(self.finishScreen, (0, 0))
            win.blit(self.endScreenTextOne.render(f"You Win!", True, (255, 255, 255)), (380, 100))
            self.menuText = win.blit(self.endScreenText.render(f"Menu", True, (255, 255, 255)), (850, 400))
            self.playAgainText = win.blit(self.endScreenText.render(f"Play Again", True, (255, 255, 255)), (100, 400))
            self.quitText = win.blit(self.endScreenText.render(f"Quit", True, (255, 255, 255)), (525, 600))
            pygame.draw.rect(win, "white", self.playAgainText, 2)
            pygame.draw.rect(win, "white", self.menuText, 2) 
            pygame.draw.rect(win, "white", self.quitText, 2) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if pygame.Rect.collidepoint(self.menuText, pygame.mouse.get_pos()):
                        print("works")
                        self.threeDisksWin = False
                        self.fourDisksWin = False
                        self.fiveDisksWin = False
                    if pygame.Rect.collidepoint(self.playAgainText, pygame.mouse.get_pos()):
                        print("works")
                        self.threeDisksWin = False
                        self.fourDisksWin = False
                        self.fiveDisksWin = False
                    if pygame.Rect.collidepoint(self.quitText, pygame.mouse.get_pos()):
                        self.saving.insertScore(self.playerName, self.threeDisksWin, self.fourDisksWin, self.fiveDisksWin, self.moveCount)
                        self.saving.storeScoresToFile()
                        self.running = False
        pygame.quit()



if __name__ == "__main__":
    TOCmenus()
