import pygame
import os
import sys
import TOCsaving


class TOCmenus:
    def __init__(self):
        #Initalise modules
        pygame.font.init()
        pygame.init()
        #fps rate
        self.fps = 10
        #conditional bools
        self.threeDisksWin = False
        self.fourDisksWin = False
        self.fiveDisksWin = False
        self.goToMainMenu = False
        #Movecount for storing in json file
        self.moveCount = 0
        #Instatiating classes
        self.saving = TOCsaving.TOCsaving()
        #color
        self.white = (255, 255, 255)
        #tuple of screensize and width
        self.endSurfaceSizeWidth, self.endSurfaceSizeHeight = 1200, 800
        self.win = pygame.display.set_mode((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
        #Images
        self.endScreenText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 60)
        self.endScreenTextOne = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
        self.mainMenuText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
        self.mainMenuDisksText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 45)
        self.paragraphText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
        self.backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
        self.towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))
        #Player name
        self.playerName = ""

    def drawWindow(self):
        #Updates the window
        pygame.display.update()
        
    def endScreenMenu(self, win, currentGM):
        self.running = True
        #Main loop
        while self.running:
            #Draws the window and blits disks
            self.drawWindow()
            self.finishScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.finishScreen.set_alpha(150)
            self.finishScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.towersImage, (0, 0))
            win.blit(self.finishScreen, (0, 0))
            #Blits text buttons
            win.blit(self.endScreenTextOne.render(f"You Win!", True, self.white), (380, 100))
            #self.menuText = win.blit(self.endScreenText.render(f"Menu", True, self.white), (200, 400))
            self.playAgainText = win.blit(self.endScreenText.render(f"Play Again", True, (255, 255, 255)), (200, 400))
            self.quitText = win.blit(self.endScreenText.render(f"Quit", True, self.white), (850, 400))
            pygame.draw.rect(win, "white", self.playAgainText, 2)
            #pygame.draw.rect(win, "white", self.menuText, 2) 
            pygame.draw.rect(win, "white", self.quitText, 2) 
            #Event checker
            for event in pygame.event.get():
                #If the press the exit button
                if event.type == pygame.QUIT:
                    self.running = False
                #If they let go of left click
                if event.type == pygame.MOUSEBUTTONUP:
                    #Checks if the position of the mouse at time of click is colliding with one of the buttons
                    if pygame.Rect.collidepoint(self.playAgainText, pygame.mouse.get_pos()):
                        #Saves the players score into JSON file
                        self.saving.insertScore(self.playerName, self.threeDisksWin, self.fourDisksWin, self.fiveDisksWin, self.moveCount)
                        self.saving.storeScoresToFile()
                        self.threeDisksWin = False
                        self.fourDisksWin = False
                        self.fiveDisksWin = False
                        #This button replays the gamemode just played
                        currentGM()
                    if pygame.Rect.collidepoint(self.quitText, pygame.mouse.get_pos()):
                        #This button quits the game
                        #Saves the players score into JSON file
                        self.saving.insertScore(self.playerName, self.threeDisksWin, self.fourDisksWin, self.fiveDisksWin, self.moveCount)
                        self.saving.storeScoresToFile()
                        self.running = False
        sys.exit()

    def mainMenu(self, win, diskThreeGM, diskFourGM, diskFiveGM):
        self.running = True
        #self.mainWin = pygame.display.set_mode((self.winSizeWidth, self.winSizeHeight)) - For main function
        while self.running:
            self.drawWindow()
            self.mainMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.mainMenuScreen.set_alpha(150)
            self.mainMenuScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.mainMenuScreen, (0, 0))
            win.blit(self.mainMenuText.render(f"Towers", True, self.white), (360, 50))
            win.blit(self.mainMenuText.render(f"Of", True, self.white), (540, 141))
            win.blit(self.mainMenuText.render(f"Cyberpunk", True, self.white), (510, 232))
            self.threeDisksText = win.blit(self.mainMenuDisksText.render(f"Play Three Disks", True, self.white), (50, 400))
            self.fiveDisksText = win.blit(self.mainMenuDisksText.render(f"Play Five Disks", True, self.white), (400, 460))
            self.fourDisksText = win.blit(self.mainMenuDisksText.render(f"Play Four Disks", True, self.white), (730, 400))
            self.hallOfFame = win.blit(self.mainMenuDisksText.render(f"Hall Of Fame", True, self.white), (440, 550))
            self.helpText = win.blit(self.mainMenuDisksText.render(f"How To Play", True, self.white), (450, 650))
            pygame.draw.rect(win, "white", self.threeDisksText, 2) 
            pygame.draw.rect(win, "white", self.fourDisksText, 2)
            pygame.draw.rect(win, "white", self.fiveDisksText, 2) 
            pygame.draw.rect(win, "white", self.hallOfFame, 2)
            pygame.draw.rect(win, "white", self.helpText, 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if pygame.Rect.collidepoint(self.threeDisksText, pygame.mouse.get_pos()):
                        diskThreeGM()
                    if pygame.Rect.collidepoint(self.fourDisksText, pygame.mouse.get_pos()):
                        diskFourGM()
                    if pygame.Rect.collidepoint(self.fiveDisksText, pygame.mouse.get_pos()):
                        diskFiveGM()
                    if pygame.Rect.collidepoint(self.helpText, pygame.mouse.get_pos()):
                        self.helpMenu(win, diskThreeGM, diskFourGM, diskFiveGM)
                    if pygame.Rect.collidepoint(self.hallOfFame, pygame.mouse.get_pos()):
                        pass
        sys.exit()
        
    def askName(self, win):
        self.running = True
        while self.running:
            self.drawWindow()
            self.askNameMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.askNameMenuScreen.set_alpha(150)
            self.askNameMenuScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.askNameMenuScreen,(0, 0))
            self.playerNameText = win.blit(self.endScreenText.render(f"Player Name: {self.playerName}", True, self.white), (125, 400))
            pygame.draw.rect(win, "white", self.playerNameText, 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.playerName = self.playerName[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.running = False
                    else:
                        self.playerName += event.unicode

                
           
    def helpMenu(self, win, diskThreeGM, diskFourGM, diskFiveGM):
        self.running = True
        while self.running:
            self.drawWindow()
            self.helpMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.helpMenuScreen.set_alpha(150)
            self.helpMenuScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.helpMenuScreen,(0, 0))
            self.helpText = win.blit(self.mainMenuText.render(f"How To Play", True, self.white), (350, 50))
            self.helpParagraph = win.blit(self.paragraphText.render(f"Towers of Hanoi (Towers Of Cyberpunk) is a game where", True, self.white), (30, 200))
            self.helpParagraph1 = win.blit(self.paragraphText.render(f"players are supposed to move the disks from the left", True, self.white), (30, 235))
            self.helpParagraph2 = win.blit(self.paragraphText.render(f"hand pole to the right hand pole in the minimum amount of moves.", True, self.white), (30, 270))  
            self.helpParagraph3 = win.blit(self.paragraphText.render(f"The minimum amount of moves can be calulated with the formula", True, self.white), (30, 305))  
            self.helpParagraph4 = win.blit(self.paragraphText.render(f"2x + 1 where x is the amount of disks.", True, self.white), (30, 340))  
            self.backText = win.blit(self.mainMenuDisksText.render(f"Back", True, self.white), (550, 650))
            pygame.draw.rect(win, "white", self.backText, 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if pygame.Rect.collidepoint(self.backText, pygame.mouse.get_pos()):
                        self.mainMenu(win, diskThreeGM, diskFourGM, diskFiveGM)
        sys.exit()


if __name__ == "__main__":
    TOCmenus()
