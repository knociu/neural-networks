import pygame as pg
import numpy as np
from adaline import *

def clearGrid():
    for i in L:
        pg.draw.rect(window, WHITE, (i[0], i[1], rectSize, rectSize))
        checkSquare[L.index(i)] = 0

def printGrid():
    print(checkSquare)

def printNumber(inputNumber):
    for idx, val in enumerate(L):
        if number[inputNumber][idx//max_X][idx%max_X] == 1.0:
            pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
            checkSquare[L.index(val)] = 1

def negate():
    for idx, val in enumerate(L):
        if checkSquare[idx] == 1:
            pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
            checkSquare[idx] = 0
        else:
            pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
            checkSquare[idx] = 1

def verticalFlip():
    previous = checkSquare.copy()
    for idx, val in enumerate(L):

        lastSquare = (idx//max_X+1)*max_X
        
        if idx%max_X < (max_X//2):
            if previous[lastSquare - idx%max_X - 1] == 1:
                pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 1
            else:
                pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 0
        elif idx%max_X > (max_X//2):
            if previous[(lastSquare - idx) % max_X - 1 + (idx//max_X)*max_X] == 1:
                pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 1
            else:
                pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 0

def horizontalFlip():
    previous = checkSquare.copy()
    for idx, val in enumerate(L):

        lastSquare = (idx//max_X+1)*max_X
        
        if idx//max_X < (max_X//2):
            if previous[len(L) - (lastSquare - idx) - (idx//max_X)*max_X] == 1:
                pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 1
            else:
                pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 0
        elif idx//max_X > (max_X//2):
            if previous[((max_X - idx//max_X - 1) * max_X) + idx%max_X] == 1:
                pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 1
            else:
                pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
                checkSquare[idx] = 0

def random():
    for idx, val in enumerate(L):
        if np.random.randint(100) <= 5 and checkSquare[idx] == 0:
            pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
            checkSquare[idx] = 1

def moveGrid(move):
    previous = checkSquare.copy()
    for idx, val in enumerate(L):
        if move == "up":
            if idx//max_X == (max_X - 1):
                if previous[idx%max_X] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
            else:
                if previous[idx+max_X] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
        elif move == "down":
            if idx//max_X == 0:
                if previous[len(previous) - max_X + idx] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
            else:
                if previous[idx-max_X] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
        elif move == "right":
            if idx%max_X == 0:
                if previous[idx + (max_X - 1)] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
            else:
                if previous[idx - 1] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
        elif move == "left":
            if idx%max_X == (max_X - 1):
                if previous[idx - (max_X - 1)] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)
            else:
                if previous[idx + 1] == 1:
                    colorRed(val)
                else:
                    colorWhite(val)


def colorRed(val):
    pg.draw.rect(window, RED, (val[0], val[1], rectSize, rectSize))
    checkSquare[L.index(val)] = 1

def colorWhite(val):
    pg.draw.rect(window, WHITE, (val[0], val[1], rectSize, rectSize))
    checkSquare[L.index(val)] = 0

def learn():
    for i in range(10):
        labels = np.zeros(10)
        labels[i] = 1
        adalines[i].train(training_inputs, labels, i)

number = [[] for _ in range(10) ]
number[0] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[1] = [
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,1.0,1.0,0.0,0.0,0.0],
    [0.0,1.0,0.0,1.0,0.0,0.0,0.0],
    [1.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[2] = [
    [0.0,1.0,1.0,1.0,0.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,1.0,0.0,0.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[3] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [0.0,0.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[4] = [
    [1.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [1.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[5] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[6] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[7] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,1.0,0.0,0.0,0.0],
    [0.0,0.0,1.0,0.0,0.0,0.0,0.0],
    [0.0,1.0,0.0,0.0,0.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[8] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]
number[9] = [
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [1.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,1.0,0.0,0.0],
    [1.0,1.0,1.0,1.0,1.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  ]






pg.init()
myfont = pg.font.SysFont('Arial', 30)

#Init window
window = pg.display.set_mode((800, 600))
surface = pg.display.get_surface()

#Variables
row = 0
max_Y = max_X = 7
rectSize = 50
arrows = ["<<","\/","/\\",">>"]
functions = ["NEG", "HOR", "VERT", "RAND"]
L = []
numberButtons = []
arrowButtons = []
funcButtons = []

#Color defines
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Creating grid
for i in range(max_Y):
    y = 10 + (i * rectSize) + ((i + 1) * 10)
    for j in range(max_X):
        x = 10 + (j * rectSize) + ((j + 1) * 10)
        L.append(pg.draw.rect(window, WHITE, (x,y,rectSize,rectSize)))
    if i < 2:
        for g in range(5):
            numberPadX = x + 100 + (60*g)
            numberButtons.append(pg.draw.rect(window, WHITE, (x + 80 + (60*g), y, rectSize, rectSize)))
            numText = myfont.render(str(g+row), False, BLACK)
            window.blit(numText, (numberPadX, y + 8))
        row += 5
    elif i >= 2 and i < 6:
        arrowButtons.append(pg.draw.rect(window, WHITE, (x + 80, y, 5*rectSize-80, rectSize)))
        numText = myfont.render(arrows[i%4], False, BLACK)

        funcButtons.append(pg.draw.rect(window, WHITE, (x + 60 + 4*rectSize, y, 2*rectSize+10, rectSize)))
        funcText = myfont.render(functions[i%4], False, BLACK)

        window.blit(numText, (x + 145, y + 8))
        window.blit(funcText, (x + 75 + 4*rectSize, y + 8))
checkSquare = [0] * len(L)

lastX = 10 + (max_X * rectSize) + ((max_X + 1) * 10)

#Definition for button to clear array and grid
clearButton = pg.draw.rect(window, WHITE, (20, lastX, 170, 50))
clearText = myfont.render('CLEAR', False, BLACK)
window.blit(clearText, (50, lastX + 5))

#Definition for button to learn number
learnButton = pg.draw.rect(window, WHITE, (200, lastX, 170, 50))
learnText = myfont.render('LEARN', False, BLACK)
window.blit(learnText, (245, lastX + 5))

#Change row
lastX += 60

#Definition for button to check array and grid
checkButton = pg.draw.rect(window, WHITE, (20, lastX, 350, 50))
checkText = myfont.render('CHECK', False, BLACK)
window.blit(checkText, (140, lastX + 5))


training_inputs = [ np.ravel(n) for n in number ]
adalines = []
for _ in range(10):
    adalines.append(Adaline(7*7))
learn()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            for i in L:
                if i.collidepoint(pos): 
                    if(checkSquare[L.index(i)] == 0):
                        pg.draw.rect(window, RED, (i[0],i[1],rectSize,rectSize))
                        checkSquare[L.index(i)] = 1
                    elif(checkSquare[L.index(i)] == 1):
                        pg.draw.rect(window, WHITE, (i[0],i[1],rectSize,rectSize))
                        checkSquare[L.index(i)] = 0

            #Clear grid
            if clearButton.collidepoint(pos):
                clearGrid()

            #Teach perceptrons
            if learnButton.collidepoint(pos):
                learn()
            
            #Check if drawn figure is number
            if checkButton.collidepoint(pos):
                print("----")
                maxPrediction = 0
                guessedNumber = 0
                for a in adalines:
                    print(adalines.index(a), ": ", a.predict(checkSquare))
                    if a.predict(checkSquare) > maxPrediction:
                        maxPrediction = a.predict(checkSquare)
                        guessedNumber = adalines.index(a)
                print("GUESS: ", guessedNumber)

            #Drawing numbers
            for i in numberButtons:
                if i.collidepoint(pos):
                    printNumber(numberButtons.index(i))

            #Arrows
            for i in arrowButtons:
                if i.collidepoint(pos) and arrowButtons.index(i) == 0:
                    moveGrid("up")
                elif i.collidepoint(pos) and arrowButtons.index(i) == 1:
                    moveGrid("right")
                elif i.collidepoint(pos) and arrowButtons.index(i) == 2:
                    moveGrid("left")
                elif i.collidepoint(pos) and arrowButtons.index(i) == 3:
                    moveGrid("down")
            #Functions
            for i in funcButtons:
                if i.collidepoint(pos) and funcButtons.index(i) == 0:
                    verticalFlip()
                elif i.collidepoint(pos) and funcButtons.index(i) == 1:
                    random()
                elif i.collidepoint(pos) and funcButtons.index(i) == 2:
                    negate()
                elif i.collidepoint(pos) and funcButtons.index(i) == 3:
                    horizontalFlip()
    pg.display.update()
pg.quit()