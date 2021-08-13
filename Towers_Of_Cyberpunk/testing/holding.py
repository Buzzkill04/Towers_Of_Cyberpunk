import pygame
import os

class threeDisks:
    def __init__(self):
        pygame.font.init()
        self.winSizeWidth, self.winSizeHeight = 1200, 800
        self.win = pygame.display.set_mode((self.winSizeWidth, self.winSizeHeight))
        pygame.display.set_caption("Towers of Cyberpunk")
        self.fps = 10
        self.velocity = 10
        self.backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
        self.towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))
        self.diskOneL = pygame.image.load(os.path.join("Assets", "Blue Disk.png"))
        self.diskTwoM = pygame.image.load(os.path.join("Assets", "Red Disk.png"))
        self.diskThreeS = pygame.image.load(os.path.join("Assets", "Green Disk.png"))
        self.diskWidthS, self.diskHeightS = 200, 50
        self.diskWidthM, self.diskHeightM = 250, 50
        self.diskWidthL, self.diskHeightL = 300, 50
        self.diskOne = pygame.transform.scale(self.diskOneL, (self.diskWidthL, self.diskHeightL))
        self.diskTwo = pygame.transform.scale(self.diskTwoM, (self.diskWidthM, self.diskHeightM))
        self.diskThree = pygame.transform.scale(self.diskThreeS, (self.diskWidthS, self.diskHeightS))
        self.moveCount = 0
        self.allowedMove = True
        self.diskOneFlying = False
        self.diskTwoFlying = False
        self.diskThreeFlying = False
        self.main()

    def allowMoveScript(self, diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider):
        self.allowedMove = False
        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
        pygame.time.wait(1500)
        self.allowedMove = True
        self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)

    def moveDiskThree(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        ticks = 50
        if self.selectedDisk == self.diskThreeMove:
            if self.keyPressed[pygame.K_w]:
                self.diskThreeFlying = True
                if self.diskTwoFlying == False and self.diskOneFlying == False:
                    self.selectedDisk.y = 166
                if self.diskTwoFlying == True or self.diskOneFlying == True and self.diskThreeFlying == True:
                    self.diskThreeFlying = False
                    self.allowedMove = False
                    self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                    pygame.time.wait(1500)
                    self.allowedMove = True
                    self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 500 and selectedDisk.y == 166:
                self.selectedDisk.x = 125
            elif self.keyPressed[pygame.K_a] and selectedDisk.x == 870 and selectedDisk.y == 166:
                self.selectedDisk.x = 500
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 125 and selectedDisk.y == 166: 
                self.selectedDisk.x = 500
            elif self.keyPressed[pygame.K_d] and selectedDisk.x == 500 and selectedDisk.y == 166: 
                self.selectedDisk.x = 870 
            elif self.keyPressed[pygame.K_s] and selectedDisk.y < 666:            
                self.diskThreeFlying = False
                while True:
                    ticks -= 1
                    self.selectedDisk.y += self.velocity
                    self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                    if ticks == 0 or pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskOneMove, self.selectedDisk):
                        break
                if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                    self.moveCount += 1
                if pygame.Rect.colliderect(self.selectedDisk, self.diskTwoMove):
                    self.moveCount += 1
                    self.selectedDisk.y = self.diskTwoMove.y - 50
                if pygame.Rect.colliderect(self.selectedDisk, self.diskOneMove):
                    self.moveCount += 1
                    self.selectedDisk.y = self.diskOneMove.y - 48
                    
    def moveDiskTwo(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        self.ticks = 50
        if self.selectedDisk == self.diskTwoMove:
            if self.keyPressed[pygame.K_w]:
                self.diskTwoFlying = True            
                if (self.diskThreeMove.x == 125 and self.diskTwoMove.x == 96) \
                    or (self.diskThreeMove.x == 500 and self.diskTwoMove.x == 470) \
                        or (self.diskThreeMove.x == 870 and self.diskTwoMove.x == 840) \
                            and self.diskThreeMove.y < self.diskTwoMove.y:
                    self.diskTwoFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                if self.diskOneFlying == False and self.diskThreeFlying == False and self.diskTwoFlying == True:
                    self.selectedDisk.y = 166
                if self.diskOneFlying == True or self.diskThreeFlying == True and self.diskTwoFlying == True:
                    self.diskTwoFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 470 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 96
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 840 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 470
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 96 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 470
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 470 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 840  
            elif self.keyPressed[pygame.K_s] and self.selectedDisk.y < 666:            
                self.diskTwoFlying = False
                while True:
                    self.ticks -= 1
                    self.selectedDisk.y += self.velocity
                    self.drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                    if self.ticks == 0 or pygame.Rect.colliderect(self.diskOneMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                        break
                if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                    self.moveCount += 1
                if pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                    self.selectedDisk.y = 166
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                if pygame.Rect.colliderect(self.selectedDisk, self.diskOneMove):
                    self.moveCount += 1
                    self.selectedDisk.y = self.diskOneMove.y - 48
                    
    def moveDiskOne(self, keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
        self.ticks = 50
        if self.selectedDisk == self.diskOneMove:
            if self.keyPressed[pygame.K_w]: 
                self.diskOneFlying = True
                if (self.diskOneMove.x == 70 and (self.diskThreeMove.x == 125 or self.diskTwoMove.x == 96)) \
                    or (self.diskOneMove.x == 445 and (self.diskThreeMove.x == 500 or self.diskTwoMove.x == 470)) \
                        or (self.diskOneMove.x == 815 and (self.diskThreeMove.x == 870 or self.diskTwoMove.x == 840)) \
                            and self.diskThreeMove.y < self.diskOneMove.y or self.diskTwoMove.y < diskOneMove.y:
                    self.diskOneFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)     
                if self.diskTwoFlying == False and self.diskThreeFlying == False and self.diskOneFlying == True:
                    self.selectedDisk.y = 166
                if self.diskTwoFlying == True or self.diskThreeFlying == True and self.diskOneFlying == True:
                    self.diskOneFlying = False
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 445 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 70
            elif self.keyPressed[pygame.K_a] and self.selectedDisk.x == 815 and self.selectedDisk.y == 166:
                self.selectedDisk.x = 445
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 70 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 445
            elif self.keyPressed[pygame.K_d] and self.selectedDisk.x == 445 and self.selectedDisk.y == 166: 
                self.selectedDisk.x = 815
            elif self.keyPressed[pygame.K_s] and self.selectedDisk.y < 666:            
                self.diskOneFlying = False
                while True:
                    self.ticks -= 1
                    self.selectedDisk.y += self.velocity
                    self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                    if self.ticks == 0 or pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                        break
                if pygame.Rect.colliderect(self.selectedDisk, self.groundCollider):
                    self.moveCount += 1
                if pygame.Rect.colliderect(self.diskTwoMove, self.selectedDisk) or pygame.Rect.colliderect(self.diskThreeMove, self.selectedDisk):
                    self.selectedDisk.y = 166
                    self.allowMoveScript(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
                    
                    
                    
    def drawWindow(self, diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider):
        self.win.blit(self.backroundImage, (0, 0))
        self.win.blit(self.towersImage, (0, 0))
        self.win.blit(self.diskOne, (diskOneMove.x, diskOneMove.y))
        self.win.blit(self.diskTwo, (diskTwoMove.x, diskTwoMove.y))
        self.win.blit(self.diskThree, (diskThreeMove.x, diskThreeMove.y))
        self.textFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
        self.moveAllowedFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
        self.moveCountText = self.textFont.render(f"Move Count: {self.moveCount}", True, (255, 255, 255))
        self.allowedMoveText = self.moveAllowedFont.render(f"Move Not Allowed!", True, (255, 255, 255))
        if self.selectedDisk == self.diskThreeMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Green Disk", True, (255, 255, 255))
        if self.selectedDisk == self.diskTwoMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Red Disk", True, (255, 255, 255))
        if self.selectedDisk == self.diskOneMove:
            self.selectedDiskText = self.textFont.render(f"Selected Disk: Blue Disk", True, (255, 255, 255))
        if self.selectedDisk == None:
            self.selectedDiskText = self.textFont.render(f"No Disk Selected", True, (255, 255, 255))
        if self.allowedMove == False:
            self.win.blit(self.allowedMoveText, (175, 200))
        if self.allowedMove == True:
            self.win.blit(self.allowedMoveText, (2000, 2000))
        self.win.blit(self.moveCountText, (0, 0))
        self.win.blit(self.selectedDiskText, (0, 40))
        '''
        pygame.draw.rect(win, "red", diskThreeMove, 1)
        pygame.draw.rect(win, "red", diskOneMove, 1)
        pygame.draw.rect(win, "red", diskTwoMove, 1)
        pygame.draw.rect(win, "red", groundCollider, 1)
        '''
        pygame.display.update()

    def main(self):
        self.diskOneMove = self.diskOne.get_rect(topleft=(70, 666))
        self.diskTwoMove = self.diskTwo.get_rect(topleft=(96, 618))
        self.diskThreeMove = self.diskThree.get_rect(topleft=(125, 568))
        self.groundCollider = pygame.Rect(0, 715, 1200, 90)
        self.clock = pygame.time.Clock()
        self.running = True
        self.selectedDisk = None
        while self.running: 
            self.clock.tick(self.fps)       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pygame.Rect.collidepoint(self.diskOneMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskOneMove
                    if pygame.Rect.collidepoint(self.diskTwoMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskTwoMove
                    if pygame.Rect.collidepoint(self.diskThreeMove, pygame.mouse.get_pos()):
                        self.selectedDisk = self.diskThreeMove
            self.drawWindow(self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.selectedDisk, self.groundCollider)
            self.keyPressed = pygame.key.get_pressed()
            self.moveDiskThree(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
            self.moveDiskTwo(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
            self.moveDiskOne(self.keyPressed, self.selectedDisk, self.diskOneMove, self.diskTwoMove, self.diskThreeMove, self.groundCollider)
        pygame.quit()
        
        
        
if __name__ == "__main__":
    threeDisks()
