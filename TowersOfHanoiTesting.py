import pygame
import os

pygame.font.init()
winSizeWidth, winSizeHeight = 1200, 800
win = pygame.display.set_mode((winSizeWidth, winSizeHeight))
pygame.display.set_caption("Towers of Cyberpunk")
fps = 10
velocity = 30
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

#checking if disk bigger, just check if the x coords are the same and the y value is larger/less than the placed disk

def moveDisks(keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove):
    global moveCount
    if selectedDisk == diskThreeMove:
        if keyPressed[pygame.K_w] and selectedDisk.y > 175:
            selectedDisk.y -= velocity
        elif keyPressed[pygame.K_a] and selectedDisk.x == 500 and selectedDisk.y in (164, 172):
            selectedDisk.x = 125
        elif keyPressed[pygame.K_a] and selectedDisk.x == 870 and selectedDisk.y in (164, 172):
            selectedDisk.x = 500
        #elif keyPressed[pygame.K_d] and selectedDisk.x == 125 and selectedDisk.y not in (667, 619, 569): 
            #selectedDisk.x = 500
        elif keyPressed[pygame.K_d] and selectedDisk.x == 125 and selectedDisk.y in (164, 172): 
            selectedDisk.x = 500
        elif keyPressed[pygame.K_d] and selectedDisk.x == 500 and selectedDisk.y in (164, 172): 
            selectedDisk.x = 870 
        elif keyPressed[pygame.K_s] and selectedDisk.y != 312 and selectedDisk.y in (164, 172): 
            selectedDisk.y = 667
            moveCount += 1
            #add dropping disk
    if selectedDisk == diskTwoMove:
        if keyPressed[pygame.K_w] and selectedDisk.y > 175:
            selectedDisk.y -= velocity
        elif keyPressed[pygame.K_a] and selectedDisk.x == 470 and selectedDisk.y in (169, 157):
            selectedDisk.x = 96
        elif keyPressed[pygame.K_a] and selectedDisk.x == 840 and selectedDisk.y in (169, 157):
            selectedDisk.x = 470
        elif keyPressed[pygame.K_d] and selectedDisk.x == 96 and selectedDisk.y in (169, 157): 
            selectedDisk.x = 470
        elif keyPressed[pygame.K_d] and selectedDisk.x == 470 and selectedDisk.y in (169, 157): 
            selectedDisk.x = 840  
        elif keyPressed[pygame.K_s] and selectedDisk.y != 312 and selectedDisk.y in (169, 157): 
            selectedDisk.y = 667
            moveCount += 1
            #add dropping disk
    if selectedDisk == diskOneMove:
        if keyPressed[pygame.K_w] and selectedDisk.y > 175:
            selectedDisk.y -= velocity
        elif keyPressed[pygame.K_a] and selectedDisk.x == 445 and selectedDisk.y == 157:
            selectedDisk.x = 70
        elif keyPressed[pygame.K_a] and selectedDisk.x == 815 and selectedDisk.y == 157:
            selectedDisk.x = 445
        elif keyPressed[pygame.K_d] and selectedDisk.x == 70 and selectedDisk.y == 157: 
            selectedDisk.x = 445
        elif keyPressed[pygame.K_d] and selectedDisk.x == 445 and selectedDisk.y == 157: 
            selectedDisk.x = 815
        elif keyPressed[pygame.K_s] and selectedDisk.y != 312 and selectedDisk.y == 157: 
            selectedDisk.y = 667
            moveCount += 1
            #add dropping disks
    
    #do if selected disk == red disk etc etc, do new set of moves to line up with poles
    #   for red disk x and y values need changing elif keyPressed[pygame.K_d] and selectedDisk.x in (-20, -70, -100) and selectedDisk.y not in (172, 242, 312): 
    #   selectedDisk.x = 350
    #                  ^^^^^^^ - This is what needs changing for disks

def drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk):
    win.blit(backroundImage, (0, 0))
    win.blit(towersImage, (0, 0))
    win.blit(diskOne, (diskOneMove.x, diskOneMove.y))
    win.blit(diskTwo, (diskTwoMove.x, diskTwoMove.y))
    win.blit(diskThree, (diskThreeMove.x, diskThreeMove.y))
    textFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
    moveCountText = textFont.render(f"Move Count: {moveCount}", True, "white")
    if selectedDisk == diskThreeMove:
        selectedDiskText = textFont.render(f"Selected Disk: Green Disk", True, "white")
    if selectedDisk == diskTwoMove:
        selectedDiskText = textFont.render(f"Selected Disk: Red Disk", True, "white")
    if selectedDisk == diskOneMove:
        selectedDiskText = textFont.render(f"Selected Disk: Blue Disk", True, "white")
    if selectedDisk == None:
        selectedDiskText = textFont.render(f"No Disk Selected", True, "white")
    win.blit(moveCountText, (0, 0))
    win.blit(selectedDiskText, (0, 40))
    #pygame.draw.rect(win, "red", diskThreeMove, 1)
    #pygame.draw.rect(win, "red", diskOneMove, 1)
    #pygame.draw.rect(win, "red", diskTwoMove, 1)
    pygame.display.update()

def main():
    diskOneMove = diskOne.get_rect(topleft=(70, 667))
    diskTwoMove = diskTwo.get_rect(topleft=(96, 619))
    diskThreeMove = diskThree.get_rect(topleft=(125, 569))
    #diskOneMove = pygame.Rect(-100, 312, 508, 406)
    #diskTwoMove = pygame.Rect(-70, 242, 450, 406)
    #diskThreeMove = pygame.Rect(-20, 172, 352, 406)
    clock = pygame.time.Clock()
    running = True
    selectedDisk = None
    while running: 
        clock.tick(fps)
        print(diskOneMove.y)
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
        if pygame.Rect.colliderect(diskThreeMove, diskTwoMove):
            print("Collision Detected")
        drawWindow(diskOneMove, diskTwoMove, diskThreeMove, selectedDisk)
        keyPressed = pygame.key.get_pressed()
        moveDisks(keyPressed, selectedDisk, diskOneMove, diskTwoMove, diskThreeMove)
    
    
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()