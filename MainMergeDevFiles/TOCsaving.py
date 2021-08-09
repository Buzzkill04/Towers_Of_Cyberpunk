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
            #self.__fileName = open("scoresTOC.json")
            #self.__fileName.close()
            #json.load(f)
        #If no file exists, a new dictionary to store scores is created
        except FileNotFoundError:
            self.__scoresTOC = {}
        
    def storeScoresToFile(self):
        with open(self.__fileName, 'w') as f:
            #Dumps the new dictonary into the json file
            json.dump(self.__scoresTOC, f)
 
    def insertScore(self, playerName, threeDisksWin, fourDisksWin, fiveDisksWin, moveCount):
        # existing player scores exists
        if threeDisksWin == True:
            nextScore = str(1)
        elif fourDisksWin == True:
            nextScore = str(2)
        elif fiveDisksWin == True:
            nextScore = str(3)
            
        if playerName in self.__scoresTOC:
            scoreList = self.__scoresTOC[playerName]
            if nextScore in scoreList:
                if moveCount < scoreList[nextScore]:
                    scoreList[nextScore] = moveCount
            else:
                scoreList[nextScore] = moveCount
        #New player
        else: 
            scoreList = {}
            scoreList[nextScore] = moveCount
        self.__scoresTOC[playerName] = scoreList

