import pygame
import os
import sys
import TOCsaving
from pygame import mixer


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
        #Creates variables that store sounds
        self.clickSound = mixer.Sound(os.path.join("Assets", "click.wav"))
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
                        self.clickSound.play()
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
                        self.clickSound.play()
                        self.saving.insertScore(self.playerName, self.threeDisksWin, self.fourDisksWin, self.fiveDisksWin, self.moveCount)
                        self.saving.storeScoresToFile()
                        self.running = False
        sys.exit()

    def mainMenu(self, win, diskThreeGM, diskFourGM, diskFiveGM):
        self.running = True
        while self.running:
            #refreshes the window and updates any changes
            self.drawWindow()
            #sets the alpha and greyness of the screen
            self.mainMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.mainMenuScreen.set_alpha(150)
            self.mainMenuScreen.fill((105, 105, 105))
            #blits the backround and title
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.mainMenuScreen, (0, 0))
            win.blit(self.mainMenuText.render(f"Towers", True, self.white), (360, 50))
            win.blit(self.mainMenuText.render(f"Of", True, self.white), (540, 141))
            win.blit(self.mainMenuText.render(f"Cyberpunk", True, self.white), (510, 232))
            #blits the text for the buttons
            self.threeDisksText = win.blit(self.mainMenuDisksText.render(f"Play Three Disks", True, self.white), (50, 400))
            self.fiveDisksText = win.blit(self.mainMenuDisksText.render(f"Play Five Disks", True, self.white), (400, 460))
            self.fourDisksText = win.blit(self.mainMenuDisksText.render(f"Play Four Disks", True, self.white), (730, 400))
            self.hallOfFameText = win.blit(self.mainMenuDisksText.render(f"Hall Of Fame", True, self.white), (440, 550))
            self.helpText = win.blit(self.mainMenuDisksText.render(f"How To Play", True, self.white), (450, 650))
            #draws squares around the button texts
            pygame.draw.rect(win, "white", self.threeDisksText, 2) 
            pygame.draw.rect(win, "white", self.fourDisksText, 2)
            pygame.draw.rect(win, "white", self.fiveDisksText, 2) 
            pygame.draw.rect(win, "white", self.hallOfFameText, 2)
            pygame.draw.rect(win, "white", self.helpText, 2)
            #event loop
            for event in pygame.event.get():
                #if the x button is pressed exit the while loop
                if event.type == pygame.QUIT:
                    self.running = False
                #if pygame detects the mouse button being released
                if event.type == pygame.MOUSEBUTTONUP:
                    #on mousebutton up checks if the position is colliding with one of the buttons
                    if pygame.Rect.collidepoint(self.threeDisksText, pygame.mouse.get_pos()):
                        #if it does collide run the appropriate function in this case the three disks gamemode
                        self.clickSound.play()
                        diskThreeGM()
                    if pygame.Rect.collidepoint(self.fourDisksText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        diskFourGM()
                    if pygame.Rect.collidepoint(self.fiveDisksText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        diskFiveGM()
                    if pygame.Rect.collidepoint(self.helpText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        self.helpMenu(win, diskThreeGM, diskFourGM, diskFiveGM)
                    if pygame.Rect.collidepoint(self.hallOfFameText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        self.hallOfFame(win, diskThreeGM, diskFourGM, diskFiveGM)
        sys.exit()
        
    def askName(self, win):
        self.running = True
        while self.running:
            #updates the winodw 
            self.drawWindow()
            #sets the alpha and grey colour of the menu
            self.askNameMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.askNameMenuScreen.set_alpha(150)
            self.askNameMenuScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.askNameMenuScreen,(0, 0))
            #blits where the players name will appear with Player Name: next to it
            self.playerNameText = win.blit(self.endScreenText.render(f"Player Name: {self.playerName}", True, self.white), (125, 400))
            self.pressEnterToContinue = win.blit(self.endScreenText.render(f"Press ENTER to continue", True, self.white), (120, 500))
            #draws a square around the player name
            pygame.draw.rect(win, "white", self.playerNameText, 2)
            #event loop
            for event in pygame.event.get():
                #if the player presses the x it closes the application
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                #if the player presses a key
                if event.type == pygame.KEYDOWN:
                    #if the player pressed backspace it deletes the last character in the player name string
                    if event.key == pygame.K_BACKSPACE:
                        self.playerName = self.playerName[:-1]
                    #if the player presses enter stop the while loop and continue
                    elif event.key == pygame.K_RETURN:
                        self.running = False
                    #add the letter they pressed to the playerName string
                    else:
                        self.playerName += event.unicode
          
           
    def helpMenu(self, win, diskThreeGM, diskFourGM, diskFiveGM):
        self.running = True
        while self.running:
            #refreshes window
            self.drawWindow()
            #sets alpha and grey colour to screen
            self.helpMenuScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.helpMenuScreen.set_alpha(150)
            self.helpMenuScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.helpMenuScreen,(0, 0))
            #Blits the title and the paragraph on how to play
            self.helpText = win.blit(self.mainMenuText.render(f"How To Play", True, self.white), (350, 50))
            self.helpParagraph = win.blit(self.paragraphText.render(f"Towers of Hanoi (Towers Of Cyberpunk) is a game where", True, self.white), (30, 200))
            self.helpParagraph1 = win.blit(self.paragraphText.render(f"players are supposed to move the disks from the left", True, self.white), (30, 235))
            self.helpParagraph2 = win.blit(self.paragraphText.render(f"hand pole to the right hand pole in the minimum amount of moves.", True, self.white), (30, 270))  
            self.helpParagraph3 = win.blit(self.paragraphText.render(f"The minimum amount of moves can be calulated with the formula", True, self.white), (30, 305))  
            self.helpParagraph4 = win.blit(self.paragraphText.render(f"2x + 1 where x is the amount of disks.", True, self.white), (30, 340))  
            self.backText = win.blit(self.mainMenuDisksText.render(f"Back", True, self.white), (550, 650))
            #draws a square around the the back button
            pygame.draw.rect(win, "white", self.backText, 2)
            #event loop
            for event in pygame.event.get():
                #if the user presses the x quits the application
                if event.type == pygame.QUIT:
                    self.running = False
                #on mouse button up checks if it collides with the back button
                if event.type == pygame.MOUSEBUTTONUP:
                    #if it does runs the main menu script
                    if pygame.Rect.collidepoint(self.backText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        self.mainMenu(win, diskThreeGM, diskFourGM, diskFiveGM)
        sys.exit()
        
    def hallOfFame(self, win, diskThreeGM, diskFourGM, diskFiveGM):
        self.running = True
        while self.running:
            #refreshes the window
            self.drawWindow()
            #sets the alpha and grey screen
            self.hallOfFameScreen = pygame.Surface((self.endSurfaceSizeWidth, self.endSurfaceSizeHeight))
            self.hallOfFameScreen.set_alpha(150)
            self.hallOfFameScreen.fill((105, 105, 105))
            win.blit(self.backroundImage, (0, 0))
            win.blit(self.hallOfFameScreen,(0, 0))
            #blits the title and back button
            self.hallOfFameText = win.blit(self.mainMenuText.render(f"Hall Of Fame", True, self.white), (300, 50))
            self.backText = win.blit(self.mainMenuDisksText.render(f"Back", True, self.white), (550, 750))
            #draws a rect around the title and back button 
            pygame.draw.rect(win, "white", self.backText, 2)
            pygame.draw.rect(win, "white", self.hallOfFameText, 2)
            #runs the script to show the scores on the window
            self.saving.getHallOfFameScores(win)
            #event loop
            for event in pygame.event.get():
                #if the user presses the x quit the application
                if event.type == pygame.QUIT:
                    self.running = False
                #check if the mouseclick collides wiht the back button
                if event.type == pygame.MOUSEBUTTONUP:
                    #if it does run the main menu script
                    if pygame.Rect.collidepoint(self.backText, pygame.mouse.get_pos()):
                        self.clickSound.play()
                        self.mainMenu(win, diskThreeGM, diskFourGM, diskFiveGM)
        sys.exit()

if __name__ == "__main__":
    TOCmenus()
