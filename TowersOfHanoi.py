import pygame
import os

pygame.font.init()
winSizeWidth, winSizeHeight = 1200, 800
win = pygame.display.set_mode((winSizeWidth, winSizeHeight))
pygame.display.set_caption("Towers of Cyberpunk")
fps = 10
backroundImage = pygame.image.load(os.path.join("Assets", "scrollingimage.gif"))
towersImage = pygame.image.load(os.path.join("Assets", "3towers.png"))
diskOneL = pygame.image.load(os.path.join("Assets", "Blue Disk.png"))
diskTwoM = pygame.image.load(os.path.join("Assets", "Red Disk.png"))
diskThreeS = pygame.image.load(os.path.join("Assets", "Green Disk.png"))
diskOneSizeL = 3
diskTwoSizeM = 2
diskThreeSizeS = 1
diskWidth, diskHeight = 600, 600
diskOne = pygame.transform.scale(diskOneL, (diskWidth, diskHeight))
diskTwo = pygame.transform.scale(diskTwoM, (diskWidth, diskHeight))
diskThree = pygame.transform.scale(diskThreeS, (diskWidth, diskHeight))
moveCount = 0



def moveDisks(keyPressed, diskOneMove, diskTwoMove, diskThreeMove):
    global moveCount
    if keyPressed[pygame.K_w]:
        diskThreeMove.y = -175
    elif keyPressed[pygame.K_a] and diskThreeMove.x == 350 and diskThreeMove.y not in (172, 242, 312):
        diskThreeMove.x = -20
    elif keyPressed[pygame.K_a] and diskThreeMove.x == 726 and diskThreeMove.y not in (172, 242, 312):
        diskThreeMove.x = 350
    elif keyPressed[pygame.K_d] and diskThreeMove.x == -20 and diskThreeMove.y not in (172, 242, 312): 
        diskThreeMove.x = 350
    elif keyPressed[pygame.K_d] and diskThreeMove.x == 350 and diskThreeMove.y not in (172, 242, 312): 
        diskThreeMove.x = 726  
    elif keyPressed[pygame.K_s] and diskThreeMove.y != 312 and diskThreeMove.y not in (172, 242, 312): 
        diskThreeMove.y = 312
        moveCount += 1
    

def drawWindow(diskOneMove, diskTwoMove, diskThreeMove):
    win.blit(backroundImage, [0, 0])
    win.blit(towersImage, [0, 0])
    win.blit(diskOne, (diskOneMove.x, diskOneMove.y))
    win.blit(diskTwo, (diskTwoMove.x, diskTwoMove.y))
    win.blit(diskThree, (diskThreeMove.x, diskThreeMove.y))
    moveCountFont = pygame.font.Font("C:\WINDOWS\Fonts\OCRAEXT.TTF", 30)
    moveCountText = moveCountFont.render(f"Move Count: {moveCount}", True, "white")
    win.blit(moveCountText, [0, 0])
    pygame.display.update()

def main():
    diskOneMove = pygame.Rect(-100, 312, diskWidth, diskHeight)
    diskTwoMove = pygame.Rect(-70, 242, diskWidth, diskHeight)
    diskThreeMove = pygame.Rect(-20, 172, diskWidth, diskHeight)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                selectedDisk = [diskOneMove, diskTwoMove, diskThreeMove, pygame.Rect.collidepoint(mousePos)]
        drawWindow(diskOneMove, diskTwoMove, diskThreeMove)
        keyPressed = pygame.key.get_pressed()
        moveDisks(keyPressed, diskOneMove, diskTwoMove, diskThreeMove)
    
    
    pygame.quit()
    
    
    
if __name__ == "__main__":
    main()