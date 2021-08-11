import os
import pygame
import json



class TOCsaving:
    def __init__(self):
        self.__fileName = "scoresTOC.json"
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

