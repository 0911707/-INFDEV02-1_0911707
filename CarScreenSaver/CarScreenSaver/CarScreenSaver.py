import sys, pygame
import pygame.locals
import random

pygame.init()

clock = pygame.time.Clock()
xSize = int(input("how wide do you want your screensaver? "))
ySize = int(input("how high do you want your screensaver? "))
size = (xSize, ySize)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)

done = False

class Empty:
    def __init__(self):
        self.IsEmpty = True

Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail


l = Empty



class Car:
    def __init__(self,img,posX,posY,vel):
        self.Sprite = pygame.image.load(img).convert()
        self.PosX = posX
        self.PosY = posY
        self.Velocity = vel

cnt = int(input("how many cars do you want? ")

if cnt > 25:
    cnt = 25
    
for i in range(0, cnt):
    l = Node(Car("C:\\Users\\Julian\\Desktop\\TopKekCar.png", random.randint(0,xSize), 0, random.randint(1,5)), l)



while not done:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                
    x = l
    while not(x.IsEmpty):
        screen.blit(x.Value.Sprite, (x.Value.PosX, x.Value.PosY))
        x.Value.PosY += x.Value.Velocity
        
        if x.Value.PosY > 500 and not x.IsEmpty:
            x.Value.PosX = random.randint(0,xSize)
            x.Value.PosY = 0
            x.Value.Velocity = random.randint(1,5)
        x = x.Tail

    clock.tick(60)
    pygame.display.update()
pygame.quit()
