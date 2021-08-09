import pygame
import os
from TowersOfCyberpunkMenus import TOCmenus
from TOCsaving import TOCsaving

class fourDisks:
    def __init__(self):
        #This is the init method of the class, initialises all variables needed.
        #Initialises pygames font module
        pygame.font.init()
        #sets a tuple of the screen size
        self.winSizeWidth, self.winSizeHeight = 1200, 800
        #creates the display
        self.win = pygame.display.set_mode((self.winSizeWidth, self.winSizeHeight))
        #sets the caption of the display
        pygame.display.set_caption("Towers of Cyberpunk")
        #display FPS and disk velocity
        self.fps = 10
        self.velocity = 10
        #Images of disks, background and poles
        self.backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
        self.towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))
        self.diskOneL = pygame.image.load(os.path.join("Assets", "Blue Disk.png"))
        self.diskTwoM = pygame.image.load(os.path.join("Assets", "Red Disk.png"))
        self.diskThreeS = pygame.image.load(os.path.join("Assets", "Green Disk.png"))
        self.diskFourXS = pygame.image.load(os.path.join("Assets", "orangeDisk.png"))
        #disk widths, heights
        self.diskWidthS, self.diskHeightS = 200, 50
        self.diskWidthM, self.diskHeightM = 250, 50
        self.diskWidthL, self.diskHeightL = 300, 50
        self.diskWidthXS, self.diskHeightXS = 150, 50
        #sets the image of the disks to the width and height
        self.diskOne = pygame.transform.scale(self.diskOneL, (self.diskWidthL, self.diskHeightL))
        self.diskTwo = pygame.transform.scale(self.diskTwoM, (self.diskWidthM, self.diskHeightM))
        self.diskThree = pygame.transform.scale(self.diskThreeS, (self.diskWidthS, self.diskHeightS))
        self.diskFour = pygame.transform.scale(self.diskFourXS, (self.diskWidthXS, self.diskHeightXS))
        #refering to imported classes
        self.menus = TOCmenus()
        self.saving = TOCsaving()
        #move Count variable
        self.moveCount = 0
        #Allowed move and flying disk bools
        self.allowedMove = True
        self.diskOneFlying = False
        self.diskTwoFlying = False
        self.diskThreeFlying = False
        self.diskFourFlying = False
        self.fourPlayerWin = False
        #calling main
        self.main()

    def allowMoveScript(self, diskOneMove, diskTwoMove, diskThreeMove, diskFourMove, selectedDisk, groundCollider):
        #This method simply blits the "Move Not Allowed" text when the user performs a move they are not allowed to move.
        #It Changes the status of the allowedMove Bool, this blits the "Move Not Allowed" text, the game waits for 1500ms then the Bool is reset and the text dissapears.
        self.allowedMove = False
        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
        pygame.time.wait(1500)
        self.allowedMove = True
        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
        
    def detectWin(self, diskOneMove, diskTwoMove, diskThreeMove):
        #This method just detects when the three disks have reached a certain position once it does it sets the playerWin Bool to True
        if (self.diskOneMove.x == 815 and self.diskOneMove.y == 666) \
            and (self.diskTwoMove.x == 840 and self.diskTwoMove.y == 618) \
                and (self.diskThreeMove.x == 870 and self.diskThreeMove.y == 568) \
                    and (self.diskFourMove.x == 893 and self.diskFourMove.y == 519):
                    self.menus.moveCount = self.moveCount  
                    self.menus.fourDisksWin = True
                    self.fourPlayerWin = True               
  
    def moveDiskFour(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, diskFourMove, groundCollider):
        self.ticks = 50
        #This methods handles the movement of the fourth orange disk.
        if self.selectedDisk == self.diskFourMove:
            #First three if statements are checks to see if the move trying to be performed is valid and allowed, if not the allowMoveScript method is called
            if self.keyPressed[pygame.K_w]:
                self.diskFourFlying = True
                if self.diskThreeFlying == False and self.diskTwoFlying == False and self.diskOneFlying == False and self.diskFourFlying == True:
                    self.selectedDisk.y = 166
                if self.diskTwoFlying == True or self.diskOneFlying == True or self.diskThreeFlying == True and self.diskFourFlying == True:
                    self.diskFourFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
            #These elif statements handle the moving of the disks checks if the correct key is pressed and, if it is and the move is allowed the disk will move
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 520 and selectedDisk.y == 166:
                self.selectedDisk.x = 148
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 893 and selectedDisk.y == 166:
                self.selectedDisk.x = 520
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 148 and selectedDisk.y == 166: 
                self.selectedDisk.x = 520
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 520 and selectedDisk.y == 166: 
                self.selectedDisk.x = 893
            elif self.keyPressed[pygame.K_s] and selectedDisk.y < 666: 
                #This elif statement handles the "falling" of the disk            
                if self.diskFourFlying == False:
                    pass
                else:
                    self.diskFourFlying = False
                    while True:
                        self.ticks -= 1
                        self.selectedDisk.y += self.velocity
                        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                        if self.ticks == 0 or pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskOneMove, self.selectedDisk) \
                            or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                            break
                    #The next 3 if statements are the colliders when dropping on collide it adds 1 to the movecount
                    #It determines the y value of the dropping disk by taking away the thickness of the dropping disk 
                    #From the y value of the disk it collides with
                    if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                        self.moveCount += 1
                        self.selectedDisk.y += 1
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskTwoMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskTwoMove.y - 50
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskOneMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskOneMove.y - 48
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskThreeMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskThreeMove.y - 49
                            
        
    def moveDiskThree(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        #This methods handles the movement of the third green disk.
        self.ticks = 50
        if self.selectedDisk == self.diskThreeMove:
            #First three if statements are checks to see if the move trying to be performed is valid and allowed, if not the allowMoveScript method is called
            if self.keyPressed[pygame.K_w]:
                self.diskThreeFlying = True
                #This if statement checks if there is a disk above the currently selected disk
                if ((self.diskFourMove.x == 148) and self.diskThreeMove.x == 125) \
                    or ((self.diskFourMove.x == 520) and self.diskThreeMove.x == 500) \
                        or ((self.diskFourMove.x == 893) and self.diskThreeMove.x == 870) \
                            and (self.diskFourMove.y < self.diskThreeMove.y):
                    self.diskThreeFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                if self.diskTwoFlying == False and self.diskOneFlying == False and self.diskFourFlying == False and self.diskThreeFlying == True:
                    self.selectedDisk.y = 166
                if self.diskTwoFlying == True or self.diskOneFlying == True or self.diskFourFlying == True and self.diskThreeFlying == True:
                    self.diskThreeFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
            #These elif statements handle the moving of the disks checks if the correct key is pressed and, if it is and the move is allowed the disk will move
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 500 and selectedDisk.y == 166:
                self.selectedDisk.x = 125
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 870 and selectedDisk.y == 166:
                self.selectedDisk.x = 500
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 125 and selectedDisk.y == 166: 
                self.selectedDisk.x = 500
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 500 and selectedDisk.y == 166: 
                self.selectedDisk.x = 870 
            elif self.keyPressed[pygame.K_s] and selectedDisk.y < 666:  
                #This elif statement handles the "falling" of the disk          
                if self.diskThreeFlying == False:
                    pass
                else:
                    self.diskThreeFlying = False
                    #This loop handles the dropping of the disk
                    while True:
                        #This loop only runs 50 times, each loop takes 1 away from the ticks variable, after 50 loops ticks = 0 and the loop breaks
                        self.ticks -= 1
                        self.selectedDisk.y += self.velocity
                        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                        if self.ticks == 0 or pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskOneMove, self.selectedDisk):
                            break
                    #The next 3 if statements are the colliders when dropping on collide it adds 1 to the movecount
                    #It determines the y value of the dropping disk by taking away the thickness of the dropping disk 
                    #From the y value of the disk it collides with
                    if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                        self.moveCount += 1
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskFourMove):
                        self.diskThreeFlying = True
                        self.selectedDisk.y = 166
                        self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskTwoMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskTwoMove.y - 50
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskOneMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskOneMove.y - 48
                    
    def moveDiskTwo(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        #This methods handles the movement of the second red disk.
        self.ticks = 50
        if self.selectedDisk == self.diskTwoMove:
            #First three if statements are checks to see if the move trying to be performed is valid and allowed, if not the allowMoveScript method is called
            if self.keyPressed[pygame.K_w]:
                self.diskTwoFlying = True  
                #This if statement checks if there is a disk above the currently selected disk          
                if ((self.diskThreeMove.x == 125 or self.diskFourMove.x == 148) and self.diskTwoMove.x == 96)  \
                    or ((self.diskThreeMove.x == 500 or self.diskFourMove.x == 520) and self.diskTwoMove.x == 470) \
                        or ((self.diskThreeMove.x == 870 or self.diskFourMove.x == 893) and self.diskTwoMove.x == 840) \
                            and (self.diskThreeMove.y < self.diskTwoMove.y or self.diskFourMove.y < self.diskTwoMove.y):
                    self.diskTwoFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                if self.diskOneFlying == False and self.diskThreeFlying == False and self.diskFourFlying == False and self.diskTwoFlying == True:
                    self.selectedDisk.y = 166
                if self.diskOneFlying == True or self.diskThreeFlying == True and self.diskTwoFlying == True:
                    self.diskTwoFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
            #These elif statements handle the moving of the disks checks if the correct key is pressed and, if it is and the move is allowed the disk will move
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 470 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 96
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 840 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 470
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 96 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 470
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 470 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 840  
            elif self.keyPressed[pygame.K_s] and self.selectedDisk.y < 666:            
                #This elif statement handles the "falling" of the disk      
                if self.diskTwoFlying == False:
                    pass
                else:
                    self.diskTwoFlying = False
                    #This loop handles the dropping of the disk
                    while True:
                        #This loop only runs 50 times, each loop takes 1 away from the ticks variable, after 50 loops ticks = 0 and the loop breaks
                        self.ticks -= 1
                        self.selectedDisk.y += self.velocity
                        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                        if self.ticks == 0 or pygame.Rect.colliderect(self.diskOneMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                            break
                    #The next 3 if statements are the colliders when dropping on collide it adds 1 to the movecount
                    #It determines the y value of the dropping disk by taking away the thickness of the dropping disk 
                    #From the y value of the disk it collides with
                    if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                        self.moveCount += 1
                    if pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskFourMove, self.selectedDisk):
                        self.diskTwoFlying = True
                        self.selectedDisk.y = 166
                        self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                    if pygame.Rect.colliderect(self.selectedDisk, self.diskOneMove):
                        self.moveCount += 1
                        self.selectedDisk.y = self.diskOneMove.y - 48
                        
    def moveDiskOne(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        #This methods handles the movement of the first blue disk.
        self.ticks = 50
        if self.selectedDisk == self.diskOneMove:
            #First three if statements are checks to see if the move trying to be performed is valid and allowed, if not the allowMoveScript method is called
            if self.keyPressed[pygame.K_w]: 
                self.diskOneFlying = True
                #This if statement checks if there is a disk above the currently selected disk 
                if (self.diskOneMove.x == 70 and (self.diskThreeMove.x == 125 or self.diskTwoMove.x == 96 or self.diskFourMove.x == 148)) \
                    or (self.diskOneMove.x == 445 and (self.diskThreeMove.x == 500 or self.diskTwoMove.x == 470 or self.diskFourMove.x == 520)) \
                        or (self.diskOneMove.x == 815 and (self.diskThreeMove.x == 870 or self.diskTwoMove.x == 840 or self.diskFourMove.x == 870)) \
                            and (self.diskThreeMove.y < self.diskOneMove.y or self.diskTwoMove.y < diskOneMove.y or self.diskFourMove.y < diskOneMove.y):
                    self.diskOneFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)     
                if self.diskTwoFlying == False and self.diskThreeFlying == False and self.diskFourFlying == False and self.diskOneFlying == True:
                    self.selectedDisk.y = 166
                if self.diskTwoFlying == True or self.diskThreeFlying == True or self.diskFourFlying == True and self.diskOneFlying == True:
                    self.diskOneFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
            #These elif statements handle the moving of the disks checks if the correct key is pressed and, if it is and the move is allowed the disk will move
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 445 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 70
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 815 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 445
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 70 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 445
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 445 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 815
            elif self.keyPressed[pygame.K_s] and self.selectedDisk.y < 666:    
                #This elif statement handles the "falling" of the disk         
                if self.diskOneFlying == False:
                    pass
                else:
                    self.diskOneFlying = False
                    #This loop handles the dropping of the disk
                    while True:
                        #This loop only runs 50 times, each loop takes 1 away from the ticks variable, after 50 loops ticks = 0 and the loop breaks
                        self.ticks -= 1
                        self.selectedDisk.y += self.velocity
                        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                        if self.ticks == 0 or pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                            break
                    #The next 3 if statements are the colliders when dropping on collide it adds 1 to the movecount
                    #It determines the y value of the dropping disk by taking away the thickness of the dropping disk 
                    #From the y value of the disk it collides with
                    if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                        self.moveCount += 1
                    if pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk) \
                        or pygame.Rect.colliderect(self.diskFourMove, self.selectedDisk):
                        self.diskOneFlying = True
                        self.selectedDisk.y = 166
                        self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
                    
                         
    def drawWindow(self, diskOneMove, diskTwoMove, diskThreeMove, diskFourMove, selectedDisk, groundCollider):
        #This method draws the window, this includes the backround, poles, disks and text.
        self.win.blit(self.backroundImage, (0, 0))
        self.win.blit(self.towersImage, (0, 0))
        self.win.blit(self.diskOne, (diskOneMove.x, diskOneMove.y))
        self.win.blit(self.diskTwo, (diskTwoMove.x, diskTwoMove.y))
        self.win.blit(self.diskThree, (diskThreeMove.x, diskThreeMove.y))
        self.win.blit(self.diskFour, (diskFourMove.x, diskFourMove.y))
        self.textFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
        self.moveAllowedFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
        self.endScreenText = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 60)
        self.moveCountText = self.textFont.render(f"Move Count: {self.moveCount}", True, (255, 255, 255))
        self.allowedMoveText = self.moveAllowedFont.render(f"Move Not Allowed!", True, (255, 255, 255))
        if self.selectedDisk == self.diskThreeMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Green Disk", True, (255, 255, 255))
        if self.selectedDisk == self.diskTwoMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Red Disk", True, (255, 255, 255))
        if self.selectedDisk == self.diskOneMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Blue Disk", True, (255, 255, 255))
        if self.selectedDisk == self.diskFourMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Orange Disk", True, (255, 255, 255))
        if self.selectedDisk == None:
            self.selectedDiskText = self.textFont.render(f"No Disk Selected", True, (255, 255, 255))
        if self.allowedMove == False:
            self.win.blit(self.allowedMoveText, (175, 200))
        if self.allowedMove == True:
            self.win.blit(self.allowedMoveText, (2000, 2000))
        if self.fourPlayerWin == True:
            self.diskOneMove.x = 70
            self.diskTwoMove.x = 96
            self.diskThreeMove.x = 125
            self.diskFourMove.x = 148
            self.fourPlayerWin = False
            self.menus.endScreenMenu(self.win)
        self.win.blit(self.moveCountText, (0, 0))
        self.win.blit(self.selectedDiskText, (0, 40))
        '''
        pygame.draw.rect(self.win, "red", diskFourMove, 1)
        pygame.draw.rect(self.win, "red", diskThreeMove, 1)
        pygame.draw.rect(self.win, "red", diskOneMove, 1)
        pygame.draw.rect(self.win, "red", diskTwoMove, 1)
        pygame.draw.rect(self.win, "red", groundCollider, 1)
        '''
        pygame.display.update()

    def main(self):
        #This is the main method of the program, the first four lines of this loop creates the disk Rects and the ground collider Rects.
        self.diskOneMove = self.diskOne.get_rect(topleft=(70, 666))
        self.diskTwoMove = self.diskTwo.get_rect(topleft=(96, 618))
        self.diskThreeMove = self.diskThree.get_rect(topleft=(125, 568))
        self.diskFourMove = self.diskFour.get_rect(topleft=(148, 519))
        self.groundCollider = pygame.Rect(0, 715, 1200, 90)
        self.clock = pygame.time.Clock()
        self.running = True
        self.selectedDisk = None
        while self.running: 
            #This is the main game loop of the program
            self.clock.tick(self.fps) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #This detects if the X button has been pressed, quitting the program
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    #This detects when the mouse button has been clicked and is moving back up.
                    #When this occurs if the mouse pos is inside the Rect of a disk the selectedDisk variable becomes the disk that has been clicked.
                    if pygame.Rect.collidepoint(self.diskOneMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskOneMove
                    if pygame.Rect.collidepoint(self.diskTwoMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskTwoMove
                    if pygame.Rect.collidepoint(self.diskThreeMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskThreeMove
                    if pygame.Rect.collidepoint(self.diskFourMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskFourMove
            #The next six lines call all the necessary methods for the program to run.
            self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.selectedDisk, self.groundCollider)
            self.keyPressed = pygame.key.get_pressed()
            self.moveDiskFour(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.diskFourMove, self.groundCollider)
            self.moveDiskThree(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
            self.moveDiskTwo(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
            self.moveDiskOne(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
            self.detectWin(self.diskOneMove, self.diskTwoMove, self.diskThreeMove)
        pygame.quit()
        
        
        
if __name__ == "__main__":
    fourDisks()
