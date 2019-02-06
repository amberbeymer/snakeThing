"""
Hello my name is Amber Beymer and this is my version of the snake game. It's inspired by the spongebob episode with
the Alaskan Bullworm. The code itself was mostly derived from "thenewboston"'s pygame tutorial on youtube. Subscribe to my dude.
"""

import pygame
import time
import random 

pygame.init() #initializes pygame module

white = (255,255,255) 
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
mint = (208, 249, 194) 
grey = (8, 6, 79) 
purple = (230, 193, 255) #1. snake color to purple

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))  #800 pixels wide, 600 tall
pygame.display.set_caption('Alaskan BullWorm') #2. changed name of game


img = pygame.image.load('wormhead.png')  #3. changed head of worm

pineapple_img = pygame.image.load('patty.png')   #4. changed apples to krabby patty (used to be pineapple variable)


clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20     #20x20 image for snake head
FPS = 25 

direction = "right"

smallfont = pygame.font.SysFont("arial", 25)
medfont = pygame.font.SysFont("arial", 50)    
largefont = pygame.font.SysFont("arial", 80)


def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            gameDisplay.fill(mint)
            message_to_screen("Paused",     #5. different colored screens for menus
                                black,
                                -100,
                                size = "large")

            message_to_screen("Press escape to continue or Q to quit.",
                              black,
                              25)
            pygame.display.update()
            clock.tick(5)
            
    

def score(score):
    text = smallfont.render("Score: "+ str(score), True, white)
    gameDisplay.blit(text, [0,0])


def randAppleGen(): 
    randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10.0


    return randAppleX, randAppleY




def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    quit()


        
        gameDisplay.fill(mint)
        message_to_screen("Alaskan Bullworm Game",
                          green,
                          -100,
                          "large")

        message_to_screen("The Objective of the game is to eat krabby patties",
                          grey,
                          -30,)
        
        message_to_screen("The more krabby patties you eat, the longer you get.",
                          grey,
                          10,)
        
        message_to_screen("Don't move off the screen!",
                          grey,
                          50,)
        
        message_to_screen("Press C to play, escape to pause, or Q to rage quit.",
                          grey,
                          180,)


        pygame.display.update()
        clock.tick(25)  #fps
                          

        
def snake(block_size,snakeList):   

    if direction =="right":
        head = pygame.transform.rotate(img, 270)

    if direction =="left":
        head = pygame.transform.rotate(img, 90)       

    if direction =="up":
        head = img
        
    if direction =="down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, purple, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color) 
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width /2), (display_height /2) + y_displace 
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(mint)
            message_to_screen("Game over :(",
                              red,
                              y_displace=-50,
                              size = "large")
            message_to_screen("Press C to play again or Q to rage quit",
                              grey,
                              50,
                              size = "small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size 
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size 
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size 
                    lead_x_change = 0

                elif event.key == pygame.K_ESCAPE:
                    pause()
            
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            


                  

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        
        gameDisplay.fill(grey)   


        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(pineapple_img, (randAppleX, randAppleY)) 


        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len (snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

    

        
        snake(block_size, snakeList)
        

        
        snake(block_size,snakeList)

        score(snakeLength-1)
        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y  > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

                
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            
            
            
        clock.tick(FPS) 
        

    pygame.quit()
    quit()
game_intro()
gameLoop()
