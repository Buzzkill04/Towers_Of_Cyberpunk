import os
import pygame
import json
from pygame import mixer



class TOCsaving:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        #File name
        self.__fileName = "scoresTOC.json"
        #Fonts
        self.paragraphText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
        #star assets
        self.goldStar = pygame.image.load(os.path.join("Assets", "goldStar.png"))
        self.silverStar = pygame.image.load(os.path.join("Assets", "silverStar.png"))
        #Creates variables that store sounds
        self.clickSound = mixer.Sound(os.path.join("Assets", "click.wav")) 
        #star dimensions
        self.starHeight, self.starWidth = 50, 50
        #scaling the stars to proper dimernsions
        self.goldStar = pygame.transform.scale(self.goldStar, (self.starHeight, self.starWidth))
        self.silverStar = pygame.transform.scale(self.silverStar, (self.starHeight, self.starWidth))
        #retrieve scores from file
        self.getScoresFromFile()
        
    def getScoresFromFile(self):
        try:
            #Trys to open the json files content
            with open(self.__fileName, 'r') as f:
                self.__scoresTOC = json.load(f)
        #If no file exists, a new dictionary to store scores is created
        except FileNotFoundError:
            self.__scoresTOC = {}
        
    def storeScoresToFile(self):
        with open(self.__fileName, 'w') as f:
            #Dumps the new dictonary into the json file
            json.dump(self.__scoresTOC, f)
 
    def insertScore(self, playerName, threeDisksWin, fourDisksWin, fiveDisksWin, moveCount):
        #Deciding which gamemode to save score under
        if threeDisksWin == True:
            nextScore = str(1)
        elif fourDisksWin == True:
            nextScore = str(2)
        elif fiveDisksWin == True:
            nextScore = str(3)
        # existing player scores exists
        if playerName in self.__scoresTOC:
            scoreList = self.__scoresTOC[playerName]
            #if the username already has scores for that gamemode
            if nextScore in scoreList:
                #if the recorded score is less than the current score
                if moveCount < scoreList[nextScore]:
                    #change the existing score to the new score
                    scoreList[nextScore] = moveCount
            else:
                #If the username doesnt have a score for that gamemode, creates a new key with that score
                scoreList[nextScore] = moveCount
        #New player
        else: 
            #creates the dictionary to store scores
            scoreList = {}
            #Create a key for that gamemode with the users score
            scoreList[nextScore] = moveCount
        #add the score list dictionary to the scores file under the key playerName
        self.__scoresTOC[playerName] = scoreList

    def getHallOfFameScores(self, win):
        #int for spacing scores
        #formula for spacing the users is rectXValue * i. i starting at 1.25 in my case this will increment the spaces by 50 pixels
        i = 1.25
        #If there is no scores print "NO SCORES"
        if self.__scoresTOC == {}:
            noScoresText = win.blit(self.paragraphText.render(F"NO SCORES", True, (255, 255, 255)), (400, 400))
        else:
            #For each username in the file
            for userName in self.__scoresTOC:
                #list to store the scores for that player
                scores = []
                #prints the users name
                playerText = win.blit(self.paragraphText.render(f"{userName}", True, (255, 255, 255)), (100, (200 * i)))
                #for easier indexing into the players score dict
                keyList = self.__scoresTOC[userName] 
                #Loops through every key in under the players name              
                for scoreKey in keyList:
                    #appends the value of the key to the scores list
                    scores.append(keyList[scoreKey])
                    #conditions that blit different sentances to avoid index errors
                    if len(scores) == 1:
                        scoreText = win.blit(self.paragraphText.render(f"GM 1: {scores[0]}", True, (255, 255, 255)), (350, (200 * i)))
                        #determining which scores get a gold star, if it doesnt get a gold star it gets a silver one 
                        if scores[0] == 7:
                            win.blit(self.goldStar,(50, (190 * i)))
                        else:
                            win.blit(self.silverStar, (50, (190 * i)))
                    elif len(scores) == 2:
                        scoreText = win.blit(self.paragraphText.render(f"GM 1: {scores[0]}, GM 2: {scores[1]}", True, (255, 255, 255)), (350, (200 * i)))
                        if scores[0] == 7 or scores[1] == 15:
                            win.blit(self.goldStar,(50, (190 * i)))
                        else:
                            win.blit(self.silverStar, (50, (190 * i)))
                    elif len(scores) == 3:
                        scoreText = win.blit(self.paragraphText.render(f"GM 1: {scores[0]}, GM 2: {scores[1]}, GM 3: {scores[2]}", True, (255, 255, 255)), (350, (200 * i)))
                        if scores[0] == 7 or scores[1] == 15 or scores[2] == 31:
                            win.blit(self.goldStar,(50, (190 * i)))
                        else:
                            win.blit(self.silverStar, (50, (190 * i)))
                #increments i to evenly space each user out
                i += 0.25