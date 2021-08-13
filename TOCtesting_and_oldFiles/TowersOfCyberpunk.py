import pygame
import os

pygame.font.init()
winSizeWidth, winSizeHeight = 1200, 800
win = pygame.display.set_mode((winSizeWidth, winSizeHeight))
pygame.display.set_caption("Towers of Cyberpunk")
fps = 10
velocity = 10
backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))
diskOneL = pygame.image.load(os.path.join("Assets", "Blue Disk.png"))
diskTwoM = pygame.image.load(os.path.join("Assets", "Red Disk.png"))
diskThreeS = pygame.image.load(os.path.join("Assets", "Green Disk.png"))
diskWidthS, diskHeightS = 200, 50
diskWidthM, diskHeightM = 250, 50
diskWidthL, diskHeightL = 300, 50
diskOne = pygame.transform.scale(diskOneL, (diskWidthL, diskHeightL))
diskTwo = pygame.transform.scale(diskTwoM, (diskWidthM, diskHeightM))
diskThree = pygame.transform.scale(diskThreeS, (diskWidthS, diskHeightS))
moveCount = 0
allowedMove = True

#checking if disk bigger, just check if the x coords are the same and the y value is larger/less than the placed disk

def moveDisks(keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider):
    global moveCount
    global allowedMove
    ticks = 50
    if selectedDisk == diskThreeMove:
        if keyPressed[pygame.K_w]:
            selectedDisk.y = 166
        elif keyPressed[pygame.K_a] and selectedDisk.x == 500 and selectedDisk.y == 166:
            selectedDisk.x = 125
        elif keyPressed[pygame.K_a] and selectedDisk.x == 870 and selectedDisk.y == 166:
            selectedDisk.x = 500
        elif keyPressed[pygame.K_d] and selectedDisk.x == 125 and selectedDisk.y == 166: 
            selectedDisk.x = 500
        elif keyPressed[pygame.K_d] and selectedDisk.x == 500 and selectedDisk.y == 166: 
            selectedDisk.x = 870 
        elif keyPressed[pygame.K_RETURN] and selectedDisk.y < 666:            
            while True:
                ticks -= 1
                selectedDisk.y += velocity
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                if ticks == 0 or pygame.Rect.colliderect(diskTwoMove, selectedDisk) or pygame.Rect.colliderect(diskOneMove, selectedDisk):
                    break
            if pygame.Rect.colliderect(selectedDisk, groundCollider):
                moveCount += 1
            if pygame.Rect.colliderect(selectedDisk, diskTwoMove):
                moveCount += 1
                selectedDisk.y = diskTwoMove.y - 50
            if pygame.Rect.colliderect(selectedDisk, diskOneMove):
                moveCount += 1
                selectedDisk.y = diskOneMove.y - 48
                
    if selectedDisk == diskTwoMove:
        if keyPressed[pygame.K_w]:
            selectedDisk.y = 166
        elif keyPressed[pygame.K_a] and selectedDisk.x == 470 and selectedDisk.y == 166:
            selectedDisk.x = 96
        elif keyPressed[pygame.K_a] and selectedDisk.x == 840 and selectedDisk.y == 166:
            selectedDisk.x = 470
        elif keyPressed[pygame.K_d] and selectedDisk.x == 96 and selectedDisk.y == 166: 
            selectedDisk.x = 470
        elif keyPressed[pygame.K_d] and selectedDisk.x == 470 and selectedDisk.y == 166: 
            selectedDisk.x = 840  
        elif keyPressed[pygame.K_RETURN] and selectedDisk.y < 666:            
            while True:
                ticks -= 1
                selectedDisk.y += velocity
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                if ticks == 0 or pygame.Rect.colliderect(diskOneMove, selectedDisk) or pygame.Rect.colliderect(diskThreeMove, selectedDisk):
                    break
            if pygame.Rect.colliderect(selectedDisk, groundCollider):
                moveCount += 1
            if pygame.Rect.colliderect(diskThreeMove, selectedDisk):
                selectedDisk.y = 166
                allowedMove = False
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                pygame.time.wait(1500)
                allowedMove = True
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
            if pygame.Rect.colliderect(selectedDisk, diskOneMove):
                moveCount += 1
                selectedDisk.y = diskOneMove.y - 48
            
    if selectedDisk == diskOneMove:
        if keyPressed[pygame.K_w]: 
            selectedDisk.y = 166
        elif keyPressed[pygame.K_a] and selectedDisk.x == 445 and selectedDisk.y == 166:
            selectedDisk.x = 70
        elif keyPressed[pygame.K_a] and selectedDisk.x == 815 and selectedDisk.y == 166:
            selectedDisk.x = 445
        elif keyPressed[pygame.K_d] and selectedDisk.x == 70 and selectedDisk.y == 166: 
            selectedDisk.x = 445
        elif keyPressed[pygame.K_d] and selectedDisk.x == 445 and selectedDisk.y == 166: 
            selectedDisk.x = 815
        elif keyPressed[pygame.K_RETURN] and selectedDisk.y < 666:            
            while True:
                ticks -= 1
                selectedDisk.y += velocity
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                if ticks == 0 or pygame.Rect.colliderect(diskTwoMove, selectedDisk) or pygame.Rect.colliderect(diskThreeMove, selectedDisk):
                    break
            if pygame.Rect.colliderect(selectedDisk, groundCollider):
                moveCount += 1
            if pygame.Rect.colliderect(diskTwoMove, selectedDisk) or pygame.Rect.colliderect(diskThreeMove, selectedDisk):
                selectedDisk.y = 166
                allowedMove = False
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
                pygame.time.wait(1500)
                allowedMove = True
                drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)

                
                
                
def drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider):
    win.blit(backroundImage, (0, 0))
    win.blit(towersImage, (0, 0))
    win.blit(diskOne, (diskOneMove.x, diskOneMove.y))
    win.blit(diskTwo, (diskTwoMove.x, diskTwoMove.y))
    win.blit(diskThree, (diskThreeMove.x, diskThreeMove.y))
    textFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
    moveAllowedFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 90)
    moveCountText = textFont.render(f"Move Count: {moveCount}", True, "white")
    allowedMoveText = moveAllowedFont.render(f"Move Not Allowed!", True, "white")
    if selectedDisk == diskThreeMove:
        selectedDiskText = textFont.render(f"Selected Disk: Green Disk", True, "white")
    if selectedDisk == diskTwoMove:
        selectedDiskText = textFont.render(f"Selected Disk: Red Disk", True, "white")
    if selectedDisk == diskOneMove:
        selectedDiskText = textFont.render(f"Selected Disk: Blue Disk", True, "white")
    if selectedDisk == None:
        selectedDiskText = textFont.render(f"No Disk Selected", True, "white")
    if allowedMove == False:
        win.blit(allowedMoveText, (175, 200))
    if allowedMove == True:
        win.blit(allowedMoveText, (2000, 2000))
    win.blit(moveCountText, (0, 0))
    win.blit(selectedDiskText, (0, 40))
    '''
    pygame.draw.rect(win, "red", diskThreeMove, 1)
    pygame.draw.rect(win, "red", diskOneMove, 1)
    pygame.draw.rect(win, "red", diskTwoMove, 1)
    pygame.draw.rect(win, "red", groundCollider, 1)
    '''
    pygame.display.update()

def main():
    diskOneMove = diskOne.get_rect(topleft=(70, 666))
    diskTwoMove = diskTwo.get_rect(topleft=(96, 618))
    diskThreeMove = diskThree.get_rect(topleft=(125, 568))
    groundCollider = pygame.Rect(0, 715, 1200, 90)
    clock = pygame.time.Clock()
    running = True
    selectedDisk = None
    while running: 
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if pygame.Rect.collidepoint(diskOneMove, pygame.mouse.get_pos()):
                    selectedDisk = diskOneMove
                if pygame.Rect.collidepoint(diskTwoMove, pygame.mouse.get_pos()):
                    selectedDisk = diskTwoMove
                if pygame.Rect.collidepoint(diskThreeMove, pygame.mouse.get_pos()):
                    selectedDisk = diskThreeMove
        '''
        if pygame.Rect.colliderect(diskOneMove, groundCollider):
            print("Collision Detected")
        '''
        drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk, groundCollider)
        keyPressed = pygame.key.get_pressed()
        moveDisks(keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove, groundCollider)
    
    
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()