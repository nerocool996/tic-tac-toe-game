#-------------------------------------------------------------------------------
# Name:        Tic-Tac-Toe game
# Purpose:
#
# Author:      Nerocool996
#
# Created:     12-11-2015
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from sys    import exit

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Tic tac toe")
choice = 1 #Decides's weather it's x's turn or o's turn
board = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0]] #Board with X,Y cordinates and the value, 1 = X and 2 = O, 0=Nil
winscreen = pygame.Surface((256,256)) #winscreen surface
marqspeed=0 #speed of the textt in winscreen
clock = pygame.time.Clock()
time_passed = clock.tick()

def drawX(center):
    """
    Takes in the center,which is a list of size 2.
    """
    #impimented by drawing the diagonal of a rectandgle
    lengthX = width/3-1.5*width/10
    heightY = height/3-1.5*height/10
    corneraX = center[0]-lengthX*0.5
    corneraY = center[1]-heightY*0.5
    cornerbX = center[0]+lengthX*0.5
    cornerbY = center[1]+heightY*0.5
    pygame.draw.aaline(screen, (0, 0, 0), (corneraX, corneraY), (cornerbX, cornerbY), 10)
    corneraX = center[0]-lengthX*0.5
    corneraY = center[1]+heightY*0.5
    cornerbX = center[0]+lengthX*0.5
    cornerbY = center[1]-heightY*0.5
    pygame.draw.aaline(screen, (0, 0, 0), (corneraX, corneraY), (cornerbX, cornerbY), 10)

def animateX(pos):
    """
    Animates drawing of X
    """
    center = [(width/3)*(pos[0]+1)-width/6, (height/3)*(pos[1]+1)-height/6]
    lengthX = (width)/3-1.5*(width)/10
    heightY = height/3-1.5*(height)/10
    corneraX = center[0]-lengthX*0.5
    corneraY = center[1]-heightY*0.5
    cornerbX = center[0]+lengthX*0.5
    cornerbY = center[1]+heightY*0.5
    slope = (corneraY-cornerbY)/(corneraX-cornerbX)
    k = 0.1
    total_time = 0
    while True:
        time_passed = clock.tick()
        total_time += time_passed
        if total_time>200:
            k = k+1.0
            pygame.draw.aaline(screen, (0, 0, 0), (corneraX, corneraY), (cornerbX -((100-k)/100)*abs(corneraX-cornerbX), cornerbY - ((100-k)/100)*abs(corneraY-cornerbY)))
            pygame.display.update()
            pygame.draw.aaline(screen, (255, 255, 255), (corneraX, corneraY), (cornerbX -((100-k)/100)*abs(corneraX-cornerbX), cornerbY - ((100-k)/100)*abs(corneraY-cornerbY)))
        if k>= 100:
            break
    corneraX = center[0]-lengthX*0.5
    corneraY = center[1]+heightY*0.5
    cornerbX = center[0]+lengthX*0.5
    cornerbY = center[1]-heightY*0.5
    k = 0.1
    total_time = 0
    while True:
        time_passed = clock.tick()
        total_time += time_passed
        if total_time>200:
            k = k+1.0
            pygame.draw.aaline(screen, (0, 0, 0), (corneraX, corneraY), (cornerbX -((100-k)/100)*abs(corneraX-cornerbX), cornerbY + ((100-k)/100)*abs(corneraY-cornerbY)))
            pygame.display.update()
            pygame.draw.aaline(screen, (255, 255, 255), (corneraX, corneraY), (cornerbX -((100-k)/100)*abs(corneraX-cornerbX), cornerbY + ((100-k)/100)*abs(corneraY-cornerbY)))
        if k >= 100:
            break

def drawO(center):
    """
    Draws a circle taking center as an argument. Where center is list with 2 element, x and y cordinate
    """
    if height > width:
        radius = width/3-2*width/10
    else:
        radius = height/3-2*height/10
    pygame.draw.circle(screen,(0,0,0),center,radius,5)

def animateO(pos):
    """
    Animates the circle, while creating the
    """
    if height > width:
        radius = width/3-2*width/10
    else:
        radius = height/3-2*height/10
    center = [(width/3)*(pos[0]+1)-width/6, (height/3)*(pos[1]+1)-height/6]
    print radius
    i = 1
    total_time = 0
    while True:
        time_passed = clock.tick()
        total_time += time_passed
        if total_time>200:
            i += 1
            pygame.draw.circle(screen,(0,0,0),center,int((i/100.0)*radius)+5,5)
            pygame.display.update()
            pygame.draw.circle(screen,(255,255,255),center,int((i/100.0)*radius)+5,5)
        if i >= 100:
            break


def checkWinCondition(board):
    """
    Takes in board as cordinate in which board is a list with nine elements
    Returns either 0 for incompleate game, 1 if cross is the winner, 2 if circle is the winner
    """
    def linear():

        for i in range(3):
            bslice = board[i*3:i*3+3]
            if bslice[0][2] == bslice[1][2] and bslice[2][2] == bslice[1][2] and bslice[2][2] == bslice[0][2] and board[0][2] != 0:
                return bslice[0][2]
        for i in range(3):
            bslice = [board[i],board[i+3],board[i+6]]
            if bslice[0][2] == bslice[1][2] and bslice[2][2] == bslice[1][2] and bslice[2][2] == bslice[0][2] and board[0][2] != 0:
                return bslice[0][2]
        return 0

    def diagonal():

        if board[0][2] == board[4][2] == board[8][2] and board[0][2] != 0:
            return board[0][2]
        if board[2][2] == board[4][2] == board[6][2] and board[2][2] != 0:
            return board[2][2]
        return 0
    if linear() != 0 :
        return linear()
    elif diagonal() != 0:
        return diagonal()
    else:
        return 0


def changeTurn(choice):
    """
    Changes the turn of the current game
    """
    if choice==1:
        return 2
    if choice==2:
        return 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if(checkWinCondition(board) == 0):
                if x < width/3 and y < height/3:
                    if board[0][2] == 0:
                        board[0][2] = choice
                        if choice == 2:
                            animateO(board[0])
                        elif choice == 1:
                            animateX(board[0])
                        choice = changeTurn(choice)
                elif x < (width/3) and y < (height/3)*2:
                 if board[1][2] == 0:
                     board[1][2] = choice
                     if choice == 2:
                         animateO(board[1])
                     elif choice == 1:
                         animateX(board[0])
                     choice = changeTurn(choice)
                elif x < (width/3) and y<(height/3)*3:
                    if board[2][2] == 0:
                        board[2][2] = choice
                        if choice == 2:
                            animateO(board[2])
                        elif choice == 1:
                            animateX(board[2])
                        choice = changeTurn(choice)
                elif x < (width/3)*2 and y < (height/3):
                    if board[3][2] == 0:
                        board[3][2] = choice
                        if choice == 2:
                            animateO(board[3])
                        elif choice == 1:
                            animateX(board[3])
                        choice = changeTurn(choice)
                elif x<(width/3)*2 and y<(height/3)*2:
                        if board[4][2] == 0:
                            board[4][2] = choice
                            if choice == 2:
                                animateO(board[4])
                            elif choice == 1:
                                animateX(board[4])
                        choice = changeTurn(choice)
                elif x < (width/3)*2 and y < (height/3)*3:
                    if board[5][2] == 0:
                        board[5][2] = choice
                        if choice == 2:
                            animateO(board[5])
                        elif choice == 1:
                            animateX(board[5])
                        choice = changeTurn(choice)
                elif x < (width/3)*3 and y < (height/3):
                    if board[6][2] == 0:
                        board[6][2] = choice
                        if choice == 2:
                            animateO(board[6])
                        elif choice == 1:
                            animateX(board[6])
                        choice = changeTurn(choice)
                elif x < (width/3)*3 and y < (height/3)*2:
                    if board[7][2] == 0:
                        board[7][2] = choice
                        if choice == 2:
                            animateO(board[7])
                        elif choice == 1:
                            animateX(board[7])
                        choice = changeTurn(choice)
                elif x < (width/3)*3 and y < (height/3)*3:
                    if board[8][2] == 0:
                        board[8][2] = choice
                        if choice == 2:
                            animateO(board[8])
                        elif choice == 1:
                            animateX(board[8])
                        choice = changeTurn(choice)
    screen.fill((255, 255, 255))
    #Draws's horizontal and verticle line's on the board
    for x in range(2):
        pygame.draw.line(screen, (0, 0, 0), (width/3*(x+1), 0), ((width/3)*(x+1), height))
        pygame.draw.line(screen, (0, 0, 0), (0, (height/3)*(x+1)), (width, (height/3)*(x+1)))
    #Draw's respective circle or cross on the board
    for i in board:
        if i[2] == 1:
            drawX([(width/3)*(i[0]+1)-width/6, (height/3)*(i[1]+1)-height/6])
        elif i[2] == 2:
            drawO([(width/3)*(i[0]+1)-width/6, (height/3)*(i[1]+1)-height/6])
    #Checks and deploy's the winscreen
    if (checkWinCondition(board) != 0):
        winscreen.fill((0,0,0))
        if checkWinCondition(board) == 1:
            font = pygame.font.SysFont("arial",	30)
            text_surface = font.render("Cross Wins",	True,	(255, 255, 255))
            if marqspeed<winscreen.get_width():
                marqspeed = marqspeed+0.255
            else:
                marqspeed = 0
            winscreen.blit(text_surface,(marqspeed,winscreen.get_height()/2-text_surface.get_height()/2))
            winscreen.blit(text_surface,(marqspeed-winscreen.get_width(),256/2-text_surface.get_height()/2))
        else :
            font	=	pygame.font.SysFont("arial",	30)
            text_surface	=	font.render("Circle Wins",	True,	(255,	255,	255))
            if marqspeed<winscreen.get_width():
                marqspeed = marqspeed+0.255
            else:
                marqspeed = 0
            winscreen.blit(text_surface,(marqspeed,winscreen.get_height()/2-text_surface.get_height()/2))
            winscreen.blit(text_surface,(marqspeed-winscreen.get_width(),256/2-text_surface.get_height()/2))
        screen.blit(winscreen,(width/2-(winscreen.get_width()/2),height/2-(winscreen.get_height()/2)))
    pygame.display.update()
