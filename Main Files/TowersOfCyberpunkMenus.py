import pygame
import os

class TOCmenus:
    def __init__(self):
        pygame.font.init()
        pygame.init()
        self.fps = 10
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
            pygame.draw.rect(win, "white", self.playAgainText, 2)
            pygame.draw.rect(win, "white", self.menuText, 2) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if pygame.Rect.collidepoint(self.menuText, pygame.mouse.get_pos()):
                        print("works")
                    if pygame.Rect.collidepoint(self.playAgainText, pygame.mouse.get_pos()):
                        print("works")
        pygame.quit()

