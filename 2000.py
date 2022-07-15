################################################################################
## Krishna Dave, kdave
## Section FF 
## Term Project
# Mentor: Chaya Wurman
################################################################################

'''

References: 
mode-demo.py, Class Notes

*****************************************************************
Cropping Images Using PIL 
*****************************************************************
https://pillow.readthedocs.io/en/3.0.0/reference/ImageColor.html
http://matthiaseisen.com/pp/patterns/p0202/

****************************************************************
PIL Handbook
****************************************************************
http://effbot.org/imagingbook/pil-index.htm

****************************************************************
Thresholding and Color Detection:
****************************************************************
http://vkedco.blogspot.com/2012/08/edge-detection-with-python-pil.html
https://www.youtube.com/watch?v=jdgTNRDt7Ik
http://stackoverflow.com/questions/9319767/image-outline-using-python-pil

*******************************************************************
'''

import math
import random
from tkinter import *
import PIL
from PIL import ImageTk, Image, ImageDraw, ImageFont
from PIL import Image, ImageFilter
import os
import time 


####################################
# init
####################################
def init(data, canvas):
    data.mode = "intro"
    data.prevmode = "intro"
    ############################################################################
    # Intro Screen 
    loadBackground(data, canvas)
    ############################################################################
    # Animation
    loadAnim1(data, canvas)
    loadAnim2(data,canvas)
    loadAnim3(data, canvas)
    loadAnim4(data, canvas)
    data.Anim1X1, data.Anim1Y1 = 100, 110
    data.Anim2X1, data.Anim2Y1 = 110, data.height-100
    data.Anim3X1, data.Anim3Y1 = data.width-110, 110
    data.Anim4X1, data.Anim4Y1 =data.width-100, data.height-100

    data.Anim1dx, data.Anim4dx, data.Anim3dy, data.Anim2dy = 8, 8, 8, 8
    ############################################################################
    # Help 
    data.helpRadius = 25
    data.margin = 50
    data.helpCx = data.width - data.margin
    data.helpCy = data.height - data.margin
    loadInstructions(data, canvas)
    # Buttons: Build and Solve 
    data.introBuildX1 = data.width/2-170
    data.introBuildX2 = data.width/2-30
    data.introBuildY1 = data.height/2+50
    data.introBuildY2 = data.height/2+100

    data.introSolveX1 = data.width/2+30
    data.introSolveX2 = data.width/2+170
    data.introSolveY1 = data.height/2+50
    data.introSolveY2 = data.height/2+100
    ############################################################################
    # Constructor
    loadConBackground(data, canvas)
    data.step = 150
    data.easyX1 = data.width/3 - 50 
    data.easyX2 = data.width/3 + 50 
    data.easyY1 = data.height/2 - 25 + 100
    data.easyY2 = data.height/2 + 25 + 100
     
    data.hardX1 = data.width *2/3 - 50
    data.hardX2 = data.width *2/3 + 50
    data.hardY1 = data.height/2 - 25 + 100
    data.hardY2 = data.height/2 + 25 + 100

    data.medX1 = data.width/2 - 50 
    data.medX2 = data.width/2 + 50 
    data.medY1 = data.height/2 - 25 + 100
    data.medY2 = data.height/2 + 25 + 100

    data.nextX1, data.nextY1 = data.width/2 - 50, data.height - 90
    data.nextX2, data.nextY2 = data.width/2 + 50, data.height-50
    data.level = 0
    data.photo = 0
    # The resized image on the left of the screen
    data.finalImg = None 
    # The puzzle cut into pieces
    data.finalPuzzle = None 
    loadImg1(data, canvas)
    loadImg2(data, canvas)
    loadImg3(data, canvas)
    data.img1X1, data.img1X2 = 70, 170+70
    data.img1Y1, data.img1Y2 = 70, 70+106

    data.img2X1, data.img2X2 = 270, 270+170
    data.img2Y1, data.img2Y2 = 70, 70+119

    data.img3X1, data.img3X2 = 470, 470+170
    data.img3Y1, data.img3Y2 = 70, 70+127
    data.countPressed = 0
    data.buttonX1, data.buttonY1 = data.width/2+90, 240
    data.buttonX2, data.buttonY2 = data.width/2 + 180, 280

    ##########################################################################
    # Grid
    data.gridX1 = data.nextX1+30
    data.gridY1 = data.nextY1
    data.gridX2 = data.nextX2 + 30
    data.gridY2 = data.nextY2

    loadgrid1(data, canvas)
    loadgrid2(data, canvas)
    loadgrid3(data, canvas)

    data.gridSelectP1 = False
    data.gridSelectP2 = False
    data.gridSolved = False

    data.hintTimerCounter = 10
    data.hintDelayCounter = 0
    data.gridHint = False 
    data.gridHintOnce = 0 

    ###########################################################################
    # Puzzle 
    loadPuzzle1(data, canvas)
    loadPuzzle2(data, canvas)
    loadPuzzle3(data, canvas)
    data.piecesMade = False
    data.definedPiece = []
    data.dashboardX0 = 250
    data.dashboardY0 = 50
    data.selectBool = False
    data.pieceSelected = None  

    data.timer = 0

    # After the game is won
    data.solvedX1 = data.width/2 - 60
    data.solvedY1 = data.height/2+150
    data.solvedX2 = data.width/2 + 60
    data.solvedY2 = data.height/2+185

    # Hint Box
    data.hintX1 = 30
    data.hintY1 = 190
    data.hintX2 = 100
    data.hintY2 = 220
    data.hintPiece = None 
    data.hintColor = "red"

    ############################################################################
    # Solver 
    data.solved = False  
    data.solverFinal = None 
    data.solverShuffled = None 
    data.finalX1, data.finalY1 =  data.width/2 , 250
    data.finalX2, data.finalY2 =  data.width/2 + 110, 290

    data.shuffledX1, data.shuffledY1 = data.width/2, 310
    data.shuffledX2, data.shuffledY2 = data.width/2 + 110, 350

    ############################################################################
    # FINAL 
    data.numbering = False 
    data.shuffNumbering = False 
    data.shuffDisplay = True 

####################################
# mode dispatcher
####################################

def mousePressed(event, data, canvas):
    if (data.mode == "intro"): introMousePressed(event, data)
    elif (data.mode == "constructor"):   
            constructorMousePressed(event, data, canvas)
    elif (data.mode == "puzzle"):   puzzleMousePressed(event, data, canvas)
    elif (data.mode == "grid"):   gridMousePressed(event, data, canvas)
    elif (data.mode == "solver"):    solverMousePressed(event, data, canvas)
    elif (data.mode == "final"):     finalMousePressed(event, data, canvas)
    elif (data.mode == "help"):       helpMousePressed(event, data)


def keyPressed(event, data):
    if (data.mode == "intro"): introKeyPressed(event, data)
    elif (data.mode == "constructor"):   constructorKeyPressed(event, data)
    elif(data.mode == "puzzle"): puzzleKeyPressed(event, data)
    elif(data.mode == "grid"): gridKeyPressed(event, data)
    elif (data.mode == "solver"):       solverKeyPressed(event, data) 
    elif (data.mode == "final"):       finalKeyPressed(event, data) 
    elif (data.mode == "help"):       helpKeyPressed(event, data)

def mouseMotion(canvas, event, data):
    if (data.mode == "puzzle"): puzzleMouseMotion(canvas, event, data)

def mouseRelease(canvas, event, data):
    if (data.mode == "puzzle"): puzzleMouseRelease(canvas, event, data)

def timerFired(data):
    if (data.mode == "intro"): introTimerFired(data)
    elif (data.mode == "constructor"):   constructorTimerFired(data)
    elif (data.mode == "puzzle"):   puzzleTimerFired(data)
    elif (data.mode == "grid"):   gridTimerFired(data)
    elif (data.mode == "solver"):       solverTimerFired(data)
    elif (data.mode == "final"):       finalTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "intro"): introRedrawAll(canvas, data)
    elif (data.mode == "constructor"):   constructorRedrawAll(canvas, data)
    elif (data.mode == "puzzle"):   puzzleRedrawAll(canvas, data)
    elif (data.mode == "grid"):   gridRedrawAll(canvas, data)
    elif (data.mode == "solver"):       solverRedrawAll(canvas, data)
    elif (data.mode == "final"):       finalRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)

####################################
# intro mode
####################################

# Loading the Animations
def loadBackground(data, canvas):
    filename = "background1.gif"
    data.background = PhotoImage(file = filename, master=canvas)

def loadAnim1(data, canvas):
    filename = "introAnim1.gif"
    data.Anim1 = PhotoImage(file = filename, master=canvas)

def loadAnim2(data, canvas):
    filename = "introAnim1.gif"
    data.Anim2 = PhotoImage(file = filename, master=canvas)

def loadAnim3(data, canvas):
    filename = "introAnim1.gif"
    data.Anim3 = PhotoImage(file = filename, master=canvas)

def loadAnim4(data, canvas):
    filename = "introAnim1.gif"
    data.Anim4 = PhotoImage(file = filename, master=canvas)

def getDistance(x1, x2, y1, y2):
    distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return distance

def introMousePressed(event, data):
    # If the mouse was pressed on buttons
    if (data.introBuildX1<event.x<data.introBuildX2 and 
                data.introBuildY1<event.y<data.introBuildY2): 
        data.mode = "constructor"
    elif (data.introSolveX1 <event.x< data.introSolveX2 and 
                data.introSolveY1 <event.y< data.introSolveY2): 
        data.mode = "solver"
    elif (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        data.mode = "help"

def introKeyPressed(event, data):
    pass

def introTimerFired(data):
    # Dictates the direction of the animations
    sign = sign2 = sign3 = sign4 = -1
    if data.Anim1X1+ 100 >= data.width or data.Anim1X1 - 90 <= 0:
        data.Anim1dx *= sign
    data.Anim1X1 += data.Anim1dx
    if data.Anim2Y1 + 70 >= data.height or data.Anim2Y1 - 100 <= 0:
        data.Anim2dy *= sign2
    data.Anim2Y1 += data.Anim2dy
    if data.Anim3Y1 + 70 >= data.height or data.Anim3Y1 - 100 <= 0:
        data.Anim3dy *= sign3
    data.Anim3Y1 += data.Anim3dy
    if data.Anim4X1+ 100 >= data.width or data.Anim4X1 - 90 <= 0:
        data.Anim4dx *= sign4
    data.Anim4X1 += data.Anim4dx

# Draws the Constructor (Helper Function)
def drawConstructor(canvas, data):
    canvas.create_rectangle(data.introBuildX1, data.introBuildY1,
        data.introBuildX2, data.introBuildY2, fill = "orange", 
        outline = "brown", width = 3)

    canvas.create_text(data.width/2-140, data.height/2+60, anchor = NW,
                       text="Build", font="courier 20 bold")

# Draws the Solver (Helper Function)
def drawSolver(canvas, data):
    canvas.create_rectangle(data.introSolveX1, data.introSolveY1, 
    data.introSolveX2, data.introSolveY2, fill = "orange", 
    outline = "brown", width = 3)

    canvas.create_text(data.width/2+60, data.height/2+60, anchor = NW,
                       text="Solve", font="courier 20 bold")

# Draws the Helper (Helper Function)
def drawHelper(canvas, data):
    canvas.create_oval(data.helpCx-data.helpRadius, data.helpCy-data.helpRadius,
    data.helpCx+data.helpRadius, data.helpCy+data.helpRadius, fill = "red", 
                    outline = "Black", width = 2)

    canvas.create_text(data.helpCx, data.helpCy, text = "Help", 
            font = "Arial 15")

# Draws the Animations (Helper Function)
def drawAnimations(canvas, data):
    canvas.create_image(data.Anim1X1, data.Anim1Y1, image = data.Anim1)
    canvas.create_image(data.Anim2X1, data.Anim2Y1, image = data.Anim2)
    canvas.create_image(data.Anim3X1, data.Anim3Y1, image = data.Anim3)
    canvas.create_image(data.Anim4X1, data.Anim4Y1, image = data.Anim4)

def introRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    drawAnimations(canvas, data)
    canvas.create_text(data.width/2, data.height/2-20,
        text="Puzzle Mania", fill = "brown", font="courier 35 bold")
    #### Buttons #####
    # Constructor
    drawConstructor(canvas, data) 
    # Solve
    drawSolver(canvas, data)
    # Help Sign
    drawHelper(canvas, data)

####################################
# Help mode
####################################

def loadInstructions(data, canvas):
    filename = "instr.gif"
    data.instr = PhotoImage(file = filename, master = canvas)

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if (event.keysym == "space"):
        data.mode = "intro"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    canvas.create_text(data.width/2, 70, fill = "white",
                       text="Instructions",
                     font="courier 25 bold")
    canvas.create_image(data.width/2, data.height/2+20, image = data.instr)

####################################
# constructor mode
####################################
from tkinter import filedialog

def loadConBackground(data, canvas):
    filename = "background1.gif"
    data.conBack = PhotoImage(file = filename, master=canvas) 

# Draws an outline for a selection (Helper Function)
def drawOutline(x1, y1, x2, y2, canvas):
    canvas.create_rectangle(x1, y1, x2, y2, fill = None, outline = "red", 
            width = 3) 

# Draws an outline around the level selected (Helper Function)
def drawLevelOutline(data, canvas): 
    if data.level == 1:
        drawOutline(data.easyX1, data.easyY1, data.easyX2, data.easyY2, canvas)
    elif data.level == 2:
        drawOutline(data.medX1, data.medY1, data.medX2, data.medY2, canvas)
    elif data.level == 3:
        drawOutline(data.hardX1, data.hardY1, data.hardX2, data.hardY2, canvas)

# Draws an outline around the picture from the picture library selected 
def drawPhotoOutline(data, canvas):
    if data.photo == 1: 
        drawOutline(data.img1X1, data.img1Y1, data.img1X2, data.img1Y2, canvas)

    elif data.photo == 2:
        drawOutline(data.img2X1, data.img2Y1, data.img2X2, data.img2Y2, canvas)

    elif data.photo == 3:
        drawOutline(data.img3X1, data.img3Y1, data.img3X2, data.img3Y2, canvas)

# Draws the back button
def drawBack(canvas, data):
    canvas.create_oval(data.helpCx-data.helpRadius, data.helpCy-data.helpRadius,
    data.helpCx+data.helpRadius, data.helpCy+data.helpRadius, fill = "red", 
                    outline = "Black", width = 2)

    canvas.create_text(data.helpCx, data.helpCy, text = "Back", 
            font = "Arial 15")

# Checks the level selected
def checkLevelSelect(event, data, canvas):
    if (data.easyX1 < event.x < data.easyX2 and 
                data.easyY1 <event.y < data.easyY2):
        data.step = 150
        data.level = 1

    elif (data.medX1 < event.x < data.medX2 and 
            data.medY1 <event.y < data.medY2):
        data.step = 100
        data.level = 2

    elif (data.hardX1 < event.x < data.hardX2 and 
            data.hardY1 <event.y < data.hardY2):
        data.step = 80
        data.level = 3

# Checks the photo selected
def checkPhotoSelect(event, data, canvas):
    if (data.img1X1 < event.x < data.img1X2 and 
        data.img1Y1 <event.y < data.img1Y2):
        data.photo = 1
        data.finalImg = data.img1

    elif (data.img2X1 < event.x < data.img2X2 and 
        data.img2Y1 <event.y < data.img2Y2):
        data.photo = 2
        data.finalImg = data.img2

    elif (data.img3X1 < event.x < data.img3X2 and 
        data.img3Y1 <event.y < data.img3Y2):
        data.photo = 3
        data.finalImg = data.img3

# Draw the next button 
def drawButton(canvas, data):
    canvas.create_rectangle(data.buttonX1, data.buttonY1, data.buttonX2+10, 
            data.buttonY2, fill = "orange", outline = "brown", width = 3)
    canvas.create_text(data.buttonX1+10, data.buttonY1+10, anchor = NW, 
                    text="Upload!", font="courier 15 bold")

def checkButtonPressed(event, data, canvas):
    if (data.buttonX1 < event.x < data.buttonX2 and 
        data.buttonY1 < event.y < data.buttonY2):
        data.countPressed += 1
    if data.countPressed == 1: 
        uploadImage(data, canvas)

def constructorMousePressed(event, data, canvas):
    checkLevelSelect(event, data, canvas)
    checkPhotoSelect(event, data, canvas)
    if data.countPressed == 0:
        checkButtonPressed(event, data, canvas)
    if (data.nextX1-60 < event.x < data.nextX2-60 and
            data.nextY1 < event.y < data.nextY2):
        data.mode ="puzzle"  
    elif (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        init(data, canvas)
        data.mode = "intro"
    elif data.gridX1 < event.x < data.gridX2 and data.gridY1 <event.y<data.gridY2:
        data.mode = "grid"

# Loading the images in the picture library 
def loadImg1(data, canvas):
    filename = "puzzle1_170.gif"
    data.img1 = PhotoImage(file = filename, master=canvas) 

def loadImg2(data, canvas):
    filename = "puzzle2_170.gif"
    data.img2 = PhotoImage(file = filename, master=canvas) 

def loadImg3(data, canvas):
    filename = "puzzle3_170.gif"
    data.img3 = PhotoImage(file = filename, master=canvas)

def loadFinalImage(filename, data, canvas):
    filename = "background1.gif"
    data.conBack = PhotoImage(file = filename, master=canvas) 

# Function to pop the file explorer
def uploadImage(data, canvas):
    filename = filedialog.askopenfilename(
         initialdir = "/", 
        title = "Select an Image...", filetypes = 
        (("*.png", "*.gif"), ("all files", "*.*")))
    #size_170 = (300, 300)
    #img = Image.open(filename)
    #img.thumbnail(size_170)
    #img.save(filename)
    data.finalImg = PhotoImage(file = filename, master=canvas)

# Draws the picture library 
def drawImages(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.conBack)
    canvas.create_image(70, 70, anchor = NW, image = data.img1)
    canvas.create_image(270, 70, anchor = NW, image = data.img2)
    canvas.create_image(470, 70, anchor = NW, image = data.img3)
    canvas.create_text(data.width/2 , 40,
                       text="Pick a Picture.", font="Arial 17 bold")
    canvas.create_text(data.width/2-80 , 260,
                 text="Or upload your own picture:", font="Arial 17 bold")

def constructorKeyPressed(event, data):
    pass

def constructorTimerFired(data):
    pass

# Draws levels 
def drawLevels(canvas, data):
    canvas.create_rectangle(data.easyX1, data.easyY1, 
        data.easyX2, data.easyY2, fill = "orange", 
        outline = "brown", width = 3)
    canvas.create_rectangle(data.medX1, data.medY1, 
        data.medX2, data.medY2, fill = "orange", 
        outline = "brown", width = 3)
    canvas.create_rectangle(data.hardX1, data.hardY1, 
        data.hardX2, data.hardY2, fill = "orange", 
        outline = "brown", width = 3) 
    canvas.create_text(data.width/2 , data.height/2+40,
                       text="Pick a level.", font="Arial 17 bold")
    canvas.create_text(data.easyX1+20, data.easyY1 + 15, anchor = NW, 
                            text="Easy", font="courier 18 bold")
    canvas.create_text(data.medX1+7, data.medY1 + 15, anchor = NW, 
                            text="Medium", font="courier 18 bold")
    canvas.create_text(data.hardX1+20, data.hardY1 + 15, anchor = NW, 
                            text="Hard", font="courier 18 bold")

def drawNext(canvas, data):
    data.gridX1 = data.nextX1 + 60
    data.gridY1 = data.nextY1
    data.gridX2 = data.nextX2 + 60
    data.gridY2 = data.nextY2

    canvas.create_rectangle(data.nextX1-60, data.nextY1, 
        data.nextX2-60, data.nextY2, fill = "green", outline = "black", 
                width = 3)
    canvas.create_text(data.width/2-100, data.height-85, anchor = NW, 
                            text = "Puzzle", font = "courier 18 bold")
    canvas.create_rectangle(data.gridX1, data.gridY1, 
        data.gridX2, data.gridY2, fill = "green", outline = "black", 
                width = 3)
    canvas.create_text(data.gridX1 + 18, data.gridY1 + 5, anchor = NW, 
                            text = "Grid", font = "courier 18 bold")
    
def constructorRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.conBack)
    # Images 
    drawImages(canvas, data)
    drawPhotoOutline(data, canvas)
    # Levels 
    drawLevels(canvas, data)
    drawLevelOutline(data, canvas)
    # Upload Button: 
    drawButton(canvas, data)
    # Go back option
    drawBack(canvas, data)
    # Next 
    drawNext(canvas, data)

####################################
# grid mode
####################################

def gridMousePressed(event, data, canvas):
    if (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        init(data, canvas)
        data.mode = "constructor"
    if (data.solvedX1 < event.x< data.solvedX2 and
             data.solvedY1 <event.y < data.solvedY2):
        init(data, canvas)
        data.mode = "constructor"

    # Checks for mouse pressed on the hint button 
    if (data.gridHintX1 < event.x < data.gridHintX2 and 
        data.gridHintY1 < event.y < data.gridHintY2): 
        if data.gridHintOnce == 0:
            data.gridHint = True 
            data.gridHintOnce += 1 

    # After winning the game, checks for mouse pressed on the solve more 
    # option and changes the mode
    if data.solved == True:
        if (data.solvedX1 < event.x < data.solvedX2 and data.solvedY1 <
                event.y < data.solvedY2):
            init(data, canvas) 
            data.mode = "constructor"

    # During the game, checks for mousepressed on the first piece
    if data.gridSelectP1 == False: 
        for piece in data.definedPiece:
            if piece.containsPoint(event.x, event.y):
                print("HI!")
                if piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1:
                    data.gridPiece1 = piece
                    data.gridSelectP1 = True
                    print(data.gridSelectP1)

    # During the game, checks for mousepressed on the second piece  
    if (data.gridSelectP1 == True and data.gridSelectP2 == False):
        print("Hey")
        for piece in data.definedPiece:
            if piece.containsPoint(event.x, event.y):
                if ((piece != data.gridPiece1) and 
                        (piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1)):
                    data.gridPiece2 = piece
                    data.gridSelectP2 = True
                    print(data.gridPiece1.dimension, data.gridPiece2.dimension)

# helper functions for redrawall 
def makeOutline1(data, canvas):
    curr = data.gridPiece1
    canvas.create_rectangle(curr.cx1+1, curr.cy1+1, curr.cx2-1, curr.cy2-1, 
                         fill = None, outline = "red", width = 2)

def makeOutline2(data, canvas):
    curr = data.gridPiece2
    canvas.create_rectangle(curr.cx1, curr.cy1, curr.cx2, curr.cy2, 
                         fill = None, outline = "red", width = 2)

# Changes the position of the pieces based on the rules of each level
def makeMove(data, canvas):
    if data.level == 1 or data.level == 2: 
        p1 = data.gridPiece1
        p2 = data.gridPiece2
        tempX1, tempX2, tempY1, tempY2 = p1.cx1, p1.cx2, p1.cy1, p1.cy2
        p1.cx1, p1.cx2, p1.cy1, p1.cy2 = p2.cx1, p2.cx2, p2.cy1, p2.cy2
        p2.cx1, p2.cx2, p2.cy1, p2.cy2 = tempX1, tempX2, tempY1, tempY2
        data.gridSelectP1 = False
        data.gridSelectP2 = False
    elif data.level == 3:
        p1 = data.gridPiece1
        p2 = data.gridPiece2
        h = data.gridPieceHeight 
        w = data.gridPieceWidth 
        data.gridError = False
        if ((p1.cx1 + w != p2.cx1 and p1.cx1 - w != p2.cx1 and p1.cx1 != p2.cx1) or
            (p1.cy1 + h != p2.cy1 and p1.cy1 - h != p2.cy1 and p1.cy1 != p2.cy1)):
            data.gridError = True
            showErrorScreen(data, canvas)
            data.gridSelectP1 = False
            data.gridSelectP2 = False
            return 
        else: 
            p1 = data.gridPiece1
            p2 = data.gridPiece2
            tempX1, tempX2, tempY1, tempY2 = p1.cx1, p1.cx2, p1.cy1, p1.cy2
            p1.cx1, p1.cx2, p1.cy1, p1.cy2 = p2.cx1, p2.cx2, p2.cy1, p2.cy2
            p2.cx1, p2.cx2, p2.cy1, p2.cy2 = tempX1, tempX2, tempY1, tempY2
            data.gridSelectP1 = False
            data.gridSelectP2 = False

def showErrorScreen(data, canvas):
    canvas.create_text(data.width/2, data.height/2, 
        text = "Not a valid move!", 
        fill = "brown", font = "Arial 35 bold")

def gridKeyPressed(event, data):
    pass   

def gridTimerFired(data):
    # The timerFired loops through every 100 milliseconds or .1 second
    # So, every 10 loops of 10 milliseconds will be a second
    # Therefore, timerDelayCounter is set up such that it will 
    # decrement timerCounter by -1 every 10 milliseconds
    if data.gridHint:
        data.hintDelayCounter += 1
        if (data.hintDelayCounter%4 == 0):
            if data.hintColor == "red":
                data.hintColor = "yellow" 
            else: data.hintColor = "red"

        if (data.hintDelayCounter%10 == 0):
            data.hintTimerCounter -= 1
        if data.hintTimerCounter <= 0: data.gridHint = False 

    if data.gridSolved == False: 
        data.timer += 100

# Crops the grid pieces according to the piece size and level selected
def makeGridPieces(data, canvas):
    data.piecesMade = True
    data.puzzleWidth = data.puzzle.width()
    data.puzzleHeight = data.puzzle.height()
    if data.level == 1:
        stepHor, stepVer = 140, 140
        data.gridPieceHeight = 140
        data.gridPieceWidth =  140
    else:
        stepHor, stepVer = 70, 70  
        data.gridPieceHeight = 70
        data.gridPieceWidth = 70
    # A 2D list containing tuples with the coordinate points of the pieces 
    data.allPieces = []
    # Creates a new folder to store the images 
    newpath = "C:/Users/krishna/Desktop/112/TermProject/puzzlePieces"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    height = data.puzzleHeight
    width = data.puzzleWidth
    for y in range(0, height, stepVer):
        heights = []
        for x in range(0, width, stepHor):
            heights.append((x, y, x+stepHor, y+stepVer))
        data.allPieces.append(heights) 

    rows, cols = len(data.allPieces), len(data.allPieces[0])
    picNum = 1

    # Storing the dimensions of each piece in the start Positions list
    startPositions = []
    for row in range(rows):
        for col in range(cols):
            x1, y1, x2, y2 = data.allPieces[row][col]
            startPositions.append( (x1+150, y1+150) )

    # Saving the cropped pieces
    for row in range(rows):
        for col in range(cols):
            x1, y1, x2, y2 = data.allPieces[row][col]
            finalPosition = (x1+150, y1+150, x2+150, y2+150)
            randIndex = random.randint(0, len(startPositions)-1)
            randPos = startPositions.pop(randIndex)
            x = randPos[0]
            y = randPos[1]
            currPosition = (x, y)
            img = Image.open(data.puzzleName)
            pieceImg = img.crop(data.allPieces[row][col])
            picName = "C:/Users/krishna/Desktop/112/TermProject/puzzlePieces/img%d.gif"% picNum
            pieceImg.save(picName)
            pieceImport = PhotoImage(file = picName, master=canvas)
            picNum += 1
            data.definedPiece.append(piece(pieceImport, data.allPieces[row][col], finalPosition, currPosition))

# Helper Functions for the redrawall
def drawPieces(data, canvas):
    for piece in data.definedPiece:
        piece.draw(canvas)

def drawDashboard(canvas, data):
    canvas.create_text(270, 90, anchor = NW, text = "Dashboard", 
                  fill = "white", font = "Arial 25 bold")
    imgWidth = data.puzzle.width()
    imgHeight = data.puzzle.height()
    data.dashboardX0 = 150
    data.dashboardY0 = 150
    canvas.create_rectangle(data.dashboardX0, data.dashboardY0,
        data.dashboardX0+imgWidth, data.dashboardY0+imgHeight, 
                    fill = None, outline = "white", width = 7)

def checkgridImage(data, canvas):
    if data.finalImg == data.img1:
        data.puzzleName = "puzzle1_x2.gif"
        data.puzzle = data.grid1

    elif data.finalImg == data.img2:
        data.puzzleName = "puzzle2_x2.gif"
        data.puzzle = data.grid2

    elif data.finalImg == data.img3:
        data.puzzleName = "puzzle3_x2.gif"
        data.puzzle = data.grid3
    else:
        data.puzzle = data.finalImg

# loading images for the grid
def loadgrid1(data, canvas):
    filename = "grid1.gif"
    data.grid1 = PhotoImage(file = filename, master=canvas)
def loadgrid2(data, canvas):
    filename = "grid2.gif"
    data.grid2 = PhotoImage(file = filename, master=canvas)
def loadgrid3(data, canvas):
    filename = "grid3.gif"
    data.grid3 = PhotoImage(file = filename, master=canvas)

def checkForWinGrid(canvas, data):
    for piece in data.definedPiece:
        if piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1:
            return  
    textmsg = random.choice(["Good job!"])
    data.gridSolved = True  
    canvas.create_text(data.width/2, data.height/2+90, text = textmsg, 
        font="courier 40 bold", fill = "yellow")
    gameTime = "Time: " + str(str(time.strftime("%M:%S", 
                                time.gmtime(data.timer//1000))))
    canvas.create_text(data.width/2, data.height/2+130, text = gameTime, 
        font = "courier 16 bold", fill = "yellow")
    canvas.create_rectangle(data.solvedX1, data.solvedY1, 
                data.solvedX2, data.solvedY2, fill = "green", 
                width = 2)
    canvas.create_text(data.width/2 - 53, data.height/2+155, 
        text = "Solve more!", anchor = NW, 
        font="courier 13 bold", fill = "black")

def drawGridHint(canvas, data):
    data.gridHintX1 = data.width/2 - 40
    data.gridHintY1 = data.height - 100
    data.gridHintX2 = data.width/2 + 40
    data.gridHintY2 = data.height - 60
    canvas.create_rectangle(data.gridHintX1, data.gridHintY1, data.gridHintX2, 
                data.gridHintY2, fill = "green", outline = "black", width = 2)
    if data.gridHintOnce == 0:
        textHint = "One"
    else: textHint = "Zero"
    canvas.create_text(data.gridHintX1-120, data.gridHintY1 - 40, 
            text = "Number of hints left: " + textHint, 
            anchor = NW, font = "courier 16 bold")
    canvas.create_text(data.gridHintX1+15, data.gridHintY1 + 10, 
            text = "Hint", anchor = NW,  font = "courier 15 bold")

def drawHintImage(canvas, data):
        canvas.create_image(150, 150, anchor = NW, image = data.puzzle)
        canvas.create_rectangle(data.dashboardX0, data.dashboardY0,
        data.dashboardX0+data.puzzle.width(), 
                data.dashboardY0+data.puzzle.height(), 
                    fill = None, outline = data.hintColor, width = 8)

def gridRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    checkgridImage(data, canvas)
    if data.piecesMade == False:
        makeGridPieces(data, canvas)

    drawPieces(data, canvas)
    drawBack(canvas, data)
    drawDashboard(canvas, data)
    drawTimer(data, canvas) 

    if data.gridSelectP1 == True: 
        makeOutline1(data, canvas)

    if data.gridSelectP2 == True:
        makeOutline2(data, canvas)
    if (data.gridSelectP2 and data.gridSelectP1):
        makeMove(data, canvas)
    # Draw Hint 
    if data.gridSolved == False:
            drawGridHint(canvas, data)
            if data.gridHint == True:
                drawHintImage(canvas, data)

    # Check for and draw the winning screen 
    checkForWinGrid(canvas, data)

####################################
# Puzzle mode
####################################

# Piece Class 
class piece(object):
    # Initializing the piece object with its dimensions, current
    # position and final position
    def __init__(self, image, dimensions, finalPos, currPos):
        self.image = image
        self.dimension = dimensions # (x1, y1, x2, y2)
        self.width = self.dimension[2] - self.dimension[0]
        self.height = self.dimension[3] - self.dimension[1]
        self.finalPos = finalPos
        self.fx1 = finalPos[0]
        self.fy1 = finalPos[1]
        self.fx2 = finalPos[2]
        self.fy2 = finalPos[3]

        self.currPos = currPos
        self.cx1 = currPos[0]
        self.cy1 = currPos[1]
        self.cx2 = self.cx1 + (self.width)
        self.cy2 = self.cy1 + (self.height)

    # Checks whether a point is contained in the dimensions of a piece
    def containsPoint(self, x, y):
        return (self.cx1 < x < self.cx2 and self.cy1 < y < self.cy2) 

    def changePos(self, dx, dy):
        self.cx1 = dx
        self.cy1 = dy
        self.cx2 = dx
        self.cy2 = dy

    # Draws the piece at the current position 
    def draw(self, canvas):
        canvas.create_image(self.cx1, self.cy1, anchor = NW, image = self.image)

# Checking the final image and setting final puzzle to be cut to the x2.5 image
def checkPuzzleImage(data, canvas):
    if data.finalImg == data.img1: 
        data.puzzleName = "puzzle1_x2.gif"
        data.puzzle = data.puzzle1

    elif data.finalImg == data.img2:
        data.puzzleName = "puzzle2_x2.gif"
        data.puzzle = data.puzzle2

    elif data.finalImg == data.img3:
        data.puzzleName = "puzzle3_x2.gif"
        data.puzzle = data.puzzle3
    else:
        data.puzzle = data.finalImg

# Loading the Puzzle Images
def loadPuzzle1(data, canvas):
    filename = "puzzle1_x2.gif"
    data.puzzle1 = PhotoImage(file = filename, master=canvas)

def loadPuzzle2(data, canvas):
    filename = "puzzle2_x2.gif"
    data.puzzle2 = PhotoImage(file = filename, master=canvas)

def loadPuzzle3(data, canvas):
    filename = "puzzle3_x2.gif"
    data.puzzle3 = PhotoImage(file = filename, master=canvas)

# Helper Functions for Redrawall
def displayDashboard(canvas, data):
    canvas.create_text(250, 20, anchor = NW, text = "Dashboard", 
                  fill = "white", font = "Arial 15 bold")
    imgWidth = data.finalImg.width()
    imgHeight = data.finalImg.height()
    data.dashboardX0 = 250
    data.dashboardY0 = 50
    canvas.create_rectangle(data.dashboardX0, data.dashboardY0,
        data.dashboardX0+imgWidth*2.5, data.dashboardY0+imgHeight*2.5, 
                    fill = None, outline = "white", width = 4)

def displayFinalPuzzle(canvas, data):
    canvas.create_text(30, 20, anchor = NW, text = "Final Image", 
                        font = "Arial 15 bold")
    canvas.create_image(30, 50, anchor = NW, image= data.finalImg)

def giveHint(data, canvas):
    for piece in data.definedPiece:
        if piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1:
            print("Hi")
            data.hintPiece = piece
            return 

def drawHintPiece(data, canvas):
    if  (data.hintPiece != None and (data.hintPiece.cx1 != data.hintPiece.fx1 or 
            data.hintPiece.cy1 != data.hintPiece.cy2)): 
        Piece = data.hintPiece
        canvas.create_rectangle(Piece.cx1, Piece.cy1, Piece.cx2, 
                Piece.cy2, fill = None, outline = "green", width = 3)
        canvas.create_rectangle(Piece.fx1, Piece.fy1, Piece.fx2, 
                Piece.fy2, fill = None, outline = "green", width = 3)

def puzzleMouseRelease(canvas, event, data):
    if data.selectBool == True:
        currPiece = data.pieceSelected
        if (currPiece.fx1 < event.x < currPiece.fx2 and
            currPiece.fy1 < event.y < currPiece.fy2):
            if currPiece == data.hintPiece: 
                data.hintPiece = None
            print("Hi")
            currPiece.cx1 = currPiece.fx1
            currPiece.cy1 = currPiece.fy1
            currPiece.cx2 = currPiece.cx1 + currPiece.width
            currPiece.cy2 = currPiece.cy1 + currPiece.height
        else: 
            currPiece.cx1 = event.x-20 
            currPiece.cy1 = event.y-20
            currPiece.cx2 = currPiece.cx1 + currPiece.width
            currPiece.cy2 = currPiece.cy1 + currPiece.height
        data.selectBool = False

def puzzleMouseMotion(canvas, event, data): 
    if data.selectBool == True: 
        currPiece = data.pieceSelected
        currPiece.cx1 = event.x-20 
        currPiece.cy1 = event.y-20
        currPiece.cx2 = currPiece.cx1 + currPiece.width
        currPiece.cy2 = currPiece.cy1 + currPiece.height

def puzzleMousePressed(event, data, canvas):
    if (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        init(data, canvas)
        data.mode = "constructor" 

    # Check for mouse press on hint button
    if (data.hintX1<event.x<data.hintX2 and data.hintY1<event.y<data.hintY2):
        giveHint(data, canvas)

    # After the puzzle is solved
    if data.solved == True:
        if (data.solvedX1 < event.x < data.solvedX2 and data.solvedY1 <
                event.y < data.solvedY2):
            init(data, canvas) 
            data.mode = "constructor"

    # Moving the pieces 
    '''
    if data.selectBool == True: 
        currPiece = data.pieceSelected 

        if (currPiece.fx1 < event.x < currPiece.fx2 and
            currPiece.fy1 < event.y < currPiece.fy2):
            if currPiece == data.hintPiece: 
                data.hintPiece = None
            currPiece.cx1 = currPiece.fx1
            currPiece.cy1 = currPiece.fy1
            currPiece.cx2 = currPiece.cx1 + currPiece.width
            currPiece.cy2 = currPiece.cy1 + currPiece.height
        
        else: 
            currPiece.cx1 = event.x-20 
            currPiece.cy1 = event.y-20
            currPiece.cx2 = currPiece.cx1 + currPiece.width
            currPiece.cy2 = currPiece.cy1 + currPiece.height
        data.selectBool = False 
    '''
    #else: 
    for piece in data.definedPiece:
                # Drag 
        if piece.containsPoint(event.x, event.y):
            if piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1:
                print(piece.dimension)
                data.selectBool = True
                data.pieceSelected = piece

def makePieces(data, canvas):
    data.piecesMade = True
    data.puzzleWidth = data.puzzle.width()
    data.puzzleHeight = data.puzzle.height()
    stepHor, stepVer = data.step, data.step
    # A 2D list containing tuples with the coordinate points of the pieces 
    data.allPieces = []
    # Creates a new folder to store the images 
    newpath = "C:/Users/krishna/Desktop/112/TermProject/puzzlePieces"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    height = data.puzzleHeight
    width = data.puzzleWidth
    for y in range(0, height, stepVer):
        heights = []
        for x in range(0, width, stepHor):
            if (y+stepVer > height and x+stepHor > width):
                heights.append((x, y, width, height))
            elif (y+stepVer > height):
                heights.append((x, y, x+stepHor, height))
            elif (x + stepHor > width):
                heights.append((x, y, width, y+stepVer))
            else:
                heights.append((x, y, x+stepHor, y+stepVer))
        data.allPieces.append(heights) 
    rows, cols = len(data.allPieces), len(data.allPieces[0])
    picNum = 1
    for row in range(rows):
        for col in range(cols):
            x1, y1, x2, y2 = data.allPieces[row][col]
            finalPosition = (x1+250, y1+50, x2+250, y2+50)
            x = random.randint(20, data.width-150)
            y = random.randint(380, data.height-150)
            currPosition = (x, y)
           # dashboardPos[picNum] = (x1, y1, x2, y2)
            img = Image.open(data.puzzleName)
            pieceImg = img.crop(data.allPieces[row][col])
            picName = "C:/Users/krishna/Desktop/112/TermProject/puzzlePieces/img%d.gif"% picNum
            pieceImg.save(picName)
            pieceImport = PhotoImage(file = picName, master=canvas)
            picNum += 1
            data.definedPiece.append(piece(pieceImport, data.allPieces[row][col], finalPosition, currPosition))

def drawPieces(data, canvas):
    for piece in data.definedPiece:
        piece.draw(canvas)

# Checks whether each piece's current position is the same as the final position
def checkForWin(canvas, data):
    for piece in data.definedPiece:
        if piece.cx1 != piece.fx1 or piece.cy1 != piece.fy1:
            return  
    textmsg = random.choice(["Good job!"])
    data.solved = True  
    canvas.create_text(data.width/2, data.height/2+85, text = textmsg, 
        font="courier 45 bold", fill = "brown")
    gameTime = "Time: " + str(str(time.strftime("%M:%S", time.gmtime(data.timer//1000))))
    canvas.create_text(data.width/2, data.height/2+130, text = gameTime, 
        font = "courier 15 bold")
    canvas.create_rectangle(data.solvedX1, data.solvedY1, 
                data.solvedX2, data.solvedY2, fill = "green", 
                width = 2)
    canvas.create_text(data.width/2 - 53, data.height/2+155, 
        text = "Solve more!", anchor = NW, 
        font="courier 13 bold", fill = "black")

def drawOutlineCurrPiece(canvas, data):
    if data.pieceSelected == None: 
        return 
    elif data.selectBool == True:
        curr = data.pieceSelected
        canvas.create_rectangle(curr.cx1, curr.cy1, curr.cx2, curr.cy2, 
            fill = None, outline = "red", width = 2)

def drawHint(canvas, data):
    canvas.create_rectangle(data.hintX1, data.hintY1, data.hintX2, 
        data.hintY2, fill = "green", outline = "black", width = 2)
    canvas.create_text(data.hintX1+10, data.hintY1+5, text="Hint", anchor = NW, 
                font = "courier 15 ", fill = "black")

def drawTimer(data, canvas):
    gameTime = "Time: " + str(str(time.strftime("%M:%S", time.gmtime(data.timer//1000))))
    canvas.create_text(data.width-30, 20, anchor = NE, text = gameTime, font = "Arial 13 bold", 
                    fill = "white")

def puzzleRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2+100, image=data.background)
    # Puzzle 
    checkPuzzleImage(data, canvas)
    if data.piecesMade == False:
        makePieces(data, canvas)
    drawPieces(data, canvas)
    # Display 
    displayFinalPuzzle(canvas, data)
    drawBack(canvas, data)
    displayDashboard(canvas, data) 
    drawOutlineCurrPiece(canvas, data)
    drawHint(canvas, data)
    drawHintPiece(data, canvas)
    drawTimer(data, canvas)
    checkForWin(canvas, data)

def puzzleKeyPressed(event, data): pass

def puzzleTimerFired(data): 
    if data.solved == False:
        data.timer += 100

####################################
# solver mode
####################################

def solverMousePressed(event, data, canvas):
    if (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        init(data, canvas)
        data.mode = "intro"
    elif (data.nextX1 < event.x < data.nextX2 and
            data.nextY1-60 < event.y < data.nextY2-60):
        data.mode ="final" 
    elif (data.finalX1 < event.x < data.finalX2 and 
        data.finalY1 < event.y < data.finalY2):
        uploadFinal(data, canvas)
    elif (data.shuffledX1 < event.x < data.shuffledX2 and
        data.shuffledY1 < event.y < data.shuffledY2):
        uploadShuffled(data, canvas)

def drawSolve(canvas, data):
    canvas.create_rectangle(data.nextX1, data.nextY1-60, 
        data.nextX2, data.nextY2-60, fill = "green", outline = "black", 
                width = 3)
    canvas.create_text(data.width/2-40, data.height-145, anchor = NW, 
                            text = "Solve!", font = "courier 18 bold")

def solverKeyPressed(event, data):
    data.mode = "constructor"

def solverTimerFired(data):
    pass

########################################
# Helper Functions for redrawall
########################################
def uploadFinal(data, canvas):
    filename = filedialog.askopenfilename(
         initialdir = "/", 
        title = "Select an Image...", filetypes = 
        (("*.png", "*.gif"), ("all files", "*.*")))
    #size_170 = (300, 300)
    #img = Image.open(filename)
    #img.thumbnail(size_170)
    #img.save(filename)
    data.solverFinal = PhotoImage(file = filename, master=canvas) 

def uploadShuffled(data, canvas):
    filename = filedialog.askopenfilename(
         initialdir = "/", 
        title = "Select an Image...", filetypes = 
        (("*.png", "*.gif"), ("all files", "*.*")))
    #size_170 = (300, 300)
    #img = Image.open(filename)
    #img.thumbnail(size_170)
    #img.save(filename)
    data.solverShuffled = PhotoImage(file = filename, master=canvas)  

def drawUploadTexts(canvas, data):
    canvas.create_text(data.width/2 , 60, fill = "dark green",
                       text="Puzzle Solver", font="courier 25 bold")
    msg = "Upload pictures of the unsolved puzzle pieces and the final image."
    canvas.create_text(data.width/2-300 , 100, fill = "black", anchor = NW, 
        text=msg, font="Arial 15 bold")
    canvas.create_text(data.width/2-50 , 260, anchor = NE, 
         text="Final Image:", font="Arial 16 bold")
    canvas.create_text(data.width/2-50 , 320, anchor = NE,
                 text="Unsolved Puzzle:", font="Arial 16 bold")

def drawUploadBoxes(canvas, data):
    canvas.create_rectangle(data.finalX1, data.finalY1, data.finalX2, 
            data.finalY2, fill = "orange", outline = "brown", width = 3)
    canvas.create_rectangle(data.shuffledX1, data.shuffledY1, data.shuffledX2, 
            data.shuffledY2, fill = "orange", outline = "brown", width = 3)   
    canvas.create_text(data.finalX1+23, data.finalY1+10, anchor = NW, 
                    text="Final", font="courier 15 bold")
    canvas.create_text(data.shuffledX1+8, data.shuffledY1+10, anchor = NW, 
                    text="Unsolved", font="courier 15 bold")

def solverRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    drawSolve(canvas, data)
    drawBack(canvas, data)
    drawUploadTexts(canvas, data)
    drawUploadBoxes(canvas, data)
   
####################################
# Final Mode 
####################################
# IMP: data.solverShuffled, data.solverFinal

def finalMousePressed(event, data, canvas):
    if (getDistance(event.x, data.helpCx, event.y, data.helpCy) 
                        <= data.helpRadius):
        init(data, canvas)
        data.mode = "intro"

def threshold(canvas, data):
    pass

def edgeDetection(canvas, data):
    pass

from PIL import Image, ImageFont, ImageDraw

# Crops the final image and places numbers on it
def finalPuzzleNumbering(canvas, data):
    data.numbering = True 
    final = "C:/Users/krishna/Desktop/112/TermProject/finalSea.gif"
    #shuffled = "C:/Users/krishna/Desktop/112/TermProject/shuff.jpg"

    data.solverFinal = PhotoImage(file = final, master=canvas)
    #data.solverShuffled = PhotoImage(file = shuffled, master=canvas)

    data.finalWidth = data.solverFinal.width()
    data.finalHeight = data.solverFinal.height()
    stepHor, stepVer = data.finalWidth//4, data.finalHeight//3
    # A 2D list containing tuples with the coordinate points of the pieces 
    data.finalPieces = []
    # Creates a new folder to store the images 
    newpath = "C:/Users/krishna/Desktop/112/TermProject/finalPieces"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    height = data.finalWidth
    width = data.finalHeight
    print(height, width)
    for y in range(0, height, stepVer):
        heights = []
        for x in range(0, width, stepHor):
            #if (y+stepVer > height and x+stepHor > width):
              #  heights.append((x, y, width, height))
            #elif (y+stepVer > height):
              #  heights.append((x, y, x+stepHor, height))
           # elif (x + stepHor > width):
             #   heights.append((x, y, width, y+stepVer))
            #else:
            heights.append((x, y, x+stepHor, y+stepVer))
        data.finalPieces.append(heights) 
    data.finalPieces.pop(-1)
    rows, cols = len(data.finalPieces), len(data.finalPieces[0])
    picNum = 1
    dashboardPos = {}
    for row in range(rows):
        for col in range(cols):
            x1, y1, x2, y2 = data.finalPieces[row][col]
            dashboardPos[picNum] = (x1, y1, x2, y2)
            img = Image.open("finalSea.jpg")
            pieceImg = img.crop(data.finalPieces[row][col])
            picName = "C:/Users/krishna/Desktop/112/TermProject/finalPieces/img%d.gif"% picNum
            pieceImg.save(picName)
            draw = ImageDraw.Draw(img)
            font_med = ImageFont.truetype("arial.ttf", 40)
            WHITE = 0, 0, 0
            draw.text((x1+100, y1+100), str(picNum), WHITE, font = font_med)
            img.save("finalSea.jpg")
            
            pieceImport = PhotoImage(file = picName, master=canvas)
            picNum += 1
            #data.definedPiece.append(piece(pieceImport, data.allPieces[row][col], finalPosition, currPosition))
    data.finalDashboard = dashboardPos

#def displayShuffled(data, canvas):
#    filename = "C:/Users/krishna/Desktop/112/TermProject/shuff.gif"
#    data.ShuffledFinal = PhotoImage(file = filename, master=canvas) 
#    canvas,create_image(data.width/2, data.height+200, image = data.ShuffledFinal)

# Crops the shuffled pieces and places numbers on it 
def shuffNumbering(canvas, data):
    data.shuffNumbering = True
    shuffled = "C:/Users/krishna/Desktop/112/TermProject/shuff.gif"

    data.solverShuffled = PhotoImage(file = shuffled, master=canvas)
    #data.solverShuffled = PhotoImage(file = shuffled, master=canvas)

    data.shuffWidth = data.solverShuffled.width()
    data.shuffHeight = data.solverShuffled.height()
    stepHor, stepVer = data.shuffWidth//5, data.shuffHeight//3
    # A 2D list containing tuples with the coordinate points of the pieces 
    data.shuffPieces = []
    # Creates a new folder to store the images 
    newpath = "C:/Users/krishna/Desktop/112/TermProject/shuffPieces"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    height = data.shuffWidth
    width = data.shuffHeight
    for y in range(0, height, stepVer):
        heights = []
        for x in range(0, width, stepHor):
            if (y+stepVer > height and x+stepHor > width):
                heights.append((x, y, width, height))
            elif (y+stepVer > height):
                heights.append((x, y, x+stepHor, height))
            elif (x + stepHor > width):
                heights.append((x, y, width, y+stepVer))
            else:
                heights.append((x, y, x+stepHor, y+stepVer))
        data.shuffPieces.append(heights) 
    data.shuffPieces.pop(-1)
    rows, cols = len(data.shuffPieces), len(data.shuffPieces[0])
    picNum = 1
    dashboardPos = {}
    for row in range(rows-1):
        for col in range(cols):
            x1, y1, x2, y2 = data.shuffPieces[row][col]
            dashboardPos[picNum] = (x1, y1, x2, y2)
            img = Image.open("shuff.jpg")
            #draw = ImageDraw.Draw(img)
           # font_med = ImageFont.truetype("arial.ttf", 40)
           # WHITE = 0, 0, 0
           # draw.text((x1+100, y1+100), str(picNum), WHITE, font = font_med)
            #img.save("finalSea.jpg")
            pieceImg = img.crop(data.finalPieces[row][col])
            picName = "C:/Users/krishna/Desktop/112/TermProject/shuffPieces/img%d.gif"% picNum
            pieceImg.save(picName)
            #pieceImport = PhotoImage(file = picName, master=canvas)
            picNum += 1
            #data.definedPiece.append(piece(pieceImport, data.allPieces[row][col], finalPosition, currPosition))
    data.shuffledDashboard = dashboardPos

################################################################################
### Color Detection in PIL
################################################################################

# Gets the main color for shuffled images (Finds the average pixel for all the
# pixels present)

def get_main_color_shuff():
    avg = {}
    picNum = 13
    for i in range(1, 13):
        #img = Image.open("C:/Users/krishna/Desktop/112/TermProject/shuffPieces/img%d.gif" % i) 
        # @ TODO What are these values in tuples?
        #colors = img.convert('RGB').getcolors()
        #img.getcolors(256) #put a higher value if there are many colors in your image
        pixels = img.load()
        #print(colors)
        total = 0
        summation = 0
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                #if c[1] != (0, 0, 0) and c[1] != (255, 255, 255) and c[0] > max_occurence:
                 #   (max_occurence, most_present) = c
                if sum(c[1]) < 700: 
                    summation += (c[1][0] + c[1][1] + c[1][2])
                    total += 3
            avg[i] = round(summation/total, 4) 

        except TypeError:
            raise Exception("Too many colors in the image")
    return avg 

# Color Detection Through The Seive Method 
# In this method, first all the pieces in shuffled pieces are matched with the
# pieces in final pieces list.
# The colors are compared and the difference in color is calculated 
# So, for the first seive, all the pieces that closely match (difference<1) 
# are matched and progressively the differences are increased until all pieces 
# are matched. 

def get_main_color_final():
    avg = {}
    picNum = 13
    for i in range(1, 13):
        img = Image.open("C:/Users/krishna/Desktop/112/TermProject/finalPieces/img%d.gif" % i) 
    
        colors = img.convert('RGB').getcolors()
        #img.getcolors(256) #put a higher value if there are many colors in your image
        pixels = img.load()
        #print(colors)
        total = 0
        summation = 0
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                #if c[1] != (0, 0, 0) and c[1] != (255, 255, 255) and c[0] > max_occurence:
                 #   (max_occurence, most_present) = c
                if sum(c[1]) < 700: 
                    summation += (c[1][0] + c[1][1] + c[1][2])
                    total += 3
            avg[i] = round(summation/total, 4) 

        except TypeError:
            raise Exception("Too many colors in the image")
    return avg

import copy

def compareColors():
    finalPiecesColors = get_main_color_final()
    shuffPiecesColors = get_main_color_shuff()

    print("Final: " , finalPiecesColors)
    print("Shuffled: ", shuffPiecesColors)
################################################################################
# Initial Sieve: Difference 1
################################################################################
    result = {}
    numSelected = set()
    for pic in shuffPiecesColors:
        #while (tempFinal != {}):
            for num in finalPiecesColors:
                if (abs(finalPiecesColors[num] - shuffPiecesColors[pic]) < 1):
                    if num not in numSelected:
                        result[pic] = num
                        numSelected.add(num)
                    #del tempFinal[num]
    tempVal = []
    for num in result:
        tempVal.append(result[num])
        del shuffPiecesColors[num]  

    for value in tempVal:
        del finalPiecesColors[value]
################################################################################
# First Sieve: Difference 2
################################################################################
    firstSieve = {}
    numSelect = set()
    for pic in shuffPiecesColors:
        #while (tempFinal != {}):
            for num in finalPiecesColors:
                if (abs(finalPiecesColors[num] - shuffPiecesColors[pic]) < 2):
                    if num not in numSelect:
                        firstSieve[pic] = num
                        numSelect.add(num)
    result.update(firstSieve)
    
    temVal = []
    for num in firstSieve:
        temVal.append(firstSieve[num])
        del shuffPiecesColors[num]  

    for value in temVal:
        del finalPiecesColors[value]
################################################################################
# Second Sieve: Difference 4
################################################################################
    secondSieve = {}
    numSel = set()
    for pic in shuffPiecesColors:
        #while (tempFinal != {}):
            for num in finalPiecesColors:
                if (abs(finalPiecesColors[num] - shuffPiecesColors[pic]) < 4):
                    if num not in numSel:
                        secondSieve[pic] = num
                        numSel.add(num)
    result.update(secondSieve)
    temp = []
    for num in secondSieve:
        temp.append(secondSieve[num])
        del shuffPiecesColors[num]  
    for value in temp:
        del finalPiecesColors[value]
################################################################################
# Third Sieve: Difference 6
################################################################################
    thirdSieve = {}
    nums = set()
    for pic in shuffPiecesColors:
        #while (tempFinal != {}):
            for num in finalPiecesColors:
                if (abs(finalPiecesColors[num] - shuffPiecesColors[pic]) < 6):
                    if num not in nums:
                        thirdSieve[pic] = num
                        nums.add(num)
    result.update(thirdSieve)
    temp = []
    for num in thirdSieve:
        temp.append(thirdSieve[num])
        del shuffPiecesColors[num]  
    for value in temp:
        del finalPiecesColors[value]

################################################################################
# Fourth Sieve: Difference 8
################################################################################
    fourthSieve = {}
    numbers = set()
    for pic in shuffPiecesColors:
        #while (tempFinal != {}):
            for num in finalPiecesColors:
                if (abs(finalPiecesColors[num] - shuffPiecesColors[pic]) < 8):
                    if num not in numbers:
                        fourthSieve[pic] = num
                        numbers.add(num)
    print(fourthSieve)
    result.update(fourthSieve)
    temp = []
    for num in fourthSieve:
        temp.append(fourthSieve[num])
        del shuffPiecesColors[num]  
    for value in temp:
        del finalPiecesColors[value]    
################################################################################
# last assignment
################################################################################
    for pic in shuffPiecesColors: 
        for num in finalPiecesColors:
            result[pic] = num 
    print(result)
    return result 

# The shuffled image is updated with the corresponding numbers from the
# final image
def updateShuffledImageNums(result):
    data.shuffDisplay = True 
    img = Image.open("C:/Users/krishna/Desktop/112/TermProject/shuff.jpg")
    width, height = img.size
    stepHor = width//4
    stepVer = height//3
    picNum = 1
    for i in range(0, width-stepHor, stepHor):
        for j in range(0, height-stepVer, stepVer):
            draw = ImageDraw.Draw(img)
            font_med = ImageFont.truetype("arial.ttf", 40)
            WHITE = 0, 0, 0
            draw.text((i+100, j+100), str(result[picNum]), WHITE, font = font_med)
            img.save("C:/Users/krishna/Desktop/112/TermProject/shuff.jpg")
            picNum += 1
    data.shuffFinal = img 

################################################################################
# Edge Detection (Thresholding using PIL)
################################################################################
def edgeDetection(image, canvas, data):
    image = Image.open('threshold.jpg').convert('RGB')
    image = image.filter(ImageFilter.FIND_EDGES)
    image.save('edgez.jpg') 

def placeNumbers(canvas, data):
    pass

def finalKeyPressed(event, data):
    data.mode = "constructor"

def finalTimerFired(data):
    pass

# Loads the Final Image
def loadFinal(data, canvas):
    size_170 = (170*2, 170*2)
    img = Image.open("finalSea.jpg")
    img.thumbnail(size_170)
    img.save("finalNums.gif")
    finalImage = "finalNums.gif"
    data.numImage = PhotoImage(file = finalImage, master=canvas) 

# Loads the Shuffled Image
def loadShuffled(data, canvas):
    size_170 = (170*2, 170*2)
    img = Image.open("shuff.jpg")
    img.thumbnail(size_170)
    img.save("shuffNums.gif")
    finalImage = "shuffNums.gif"
    data.numShuff = PhotoImage(file = finalImage, master=canvas) 

# Displays the shuffled image
def displayShuffled(data, canvas):
    #finalImage = "finalSea.gif"
    #Imag = PhotoImage(file = finalImage, master=canvas) 
    canvas.create_text(data.width/2, data.height/2+25, text = "Solved Shuffled Image", 
            font = "courier 16 bold", fill = "white")
    canvas.create_image(data.width/2, data.height/2+160, image=data.numShuff)

# Displays the final image
def drawFinalImage(canvas, data):
    #finalImage = "finalSea.gif"
    #Imag = PhotoImage(file = finalImage, master=canvas) 
    canvas.create_image(data.width/2, data.height/2-100, image=Imag)

def createFinalImage(canvas, data):
    canvas.create_image(data.width/2, data.height/2-130, image=data.numImage)
    canvas.create_text(data.width/2, 25, text = "Final Image", 
            font = "courier 16 bold", fill = "white")

def createSolvedPuzzle(canvas, data):
    pass

def finalRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image=data.background)
    drawBack(canvas, data)
    if data.numbering == False:
        finalPuzzleNumbering(canvas, data)
   # drawFinalImage(canvas, data)
    loadFinal(data, canvas)
    createFinalImage(canvas, data)
    createSolvedPuzzle(canvas, data)

    if data.shuffNumbering == False: 
        shuffNumbering(canvas, data)

    #colorDetection
    if data.shuffDisplay == False: 
        updateShuffledImageNums(compareColors())
    loadShuffled(data, canvas)
    displayShuffled(data, canvas)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data, canvas)
        redrawAllWrapper(canvas, data)
################################################################################
# Drag and Drop 
################################################################################
    # Mouse Motion    
    def mouseMotionWrapper(event, canvas, data):
        mouseMotion(canvas, event, data)
        redrawAllWrapper(canvas, data)
    
    # Mouse Release  
    def mouseReleaseWrapper(event, canvas, data):
        mouseRelease(canvas, event, data)
        redrawAllWrapper(canvas, data)

    # Mouse Double Click
    #def mouseDoubleClickWrapper(event, canvas, data):
    #    mouseDoubleClick(canvas, event, data)
    #    redrawAllWrapper(canvas, data)
################################################################################
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    init(data, canvas)
    # set up events
    root.bind("<Button-1>", lambda event:
                             mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                             keyPressedWrapper(event, canvas, data))
    root.bind("<B1-Motion>", lambda event: 
                             mouseMotionWrapper(event, canvas, data))
    root.bind("<ButtonRelease-1>", lambda event:
                           mouseReleaseWrapper(event, canvas, data))

    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(700, 600)
