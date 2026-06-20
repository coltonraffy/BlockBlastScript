import pyautogui
import time
import sys

# VARS

mouseX = 0
mouseY = 0

XCord = 0
YCord = 0

pieceNum = 0
errorNum = 0

boxColor = []
bgBoardColor = []
bgPieceColor = [0, 0, 0]
bgGoodPieceColor = [56, 83, 143]

realBoard = []
testBoard = []
bestBoard = []

placeHolderBoard1 = []
placeHolderBoard2 = []

pieceIDs = [0, 0, 0]
lastPieceIDs = [0, 0, 0]

testBrokenRows = 0
helperTestBrokenRows1 = 0
helperTestBrokenRows2 = 0
testHappinessFactor = 0
testOrder = 0
testP1Xcord = 0
testP1Ycord = 0
testP2Xcord = 0
testP2Ycord = 0
testP3Xcord = 0
testP3Ycord = 0

bestBrokenRows = 0
bestHappinessFactor = 0
bestOrder = 0
best1x1holes = 0
bestP1Xcord = 0
bestP1Ycord = 0
bestP2Xcord = 0
bestP2Ycord = 0
bestP3Xcord = 0
bestP3Ycord = 0

# ID 33
left_pointForID33X = 815
pointForID33Y = 920

# ID 32
left_pointForID32X = 815
pointForID32Y = 905

# ID 34
left_pointForID34X = 757
pointForID34Y = 862

# ID 31
left_pointForID31X = 770
pointForID31Y = 862

# ID 8
left_pointForID8X = 781
pointForID8Y = 862

# ID 9
left_pointForID9X = 815
pointForID9Y = 830

# ID 2
left_pointForID2X = 795
pointForID2Y = 862

# ID 3
left_pointForID3X = 815
pointForID3Y = 841

# THE DOT
left_pointForID1X = 815
pointForID1Y = 862

# left 3x3
left3x3TopLeftX = 782
left3x3TopLeftY = 829

left3x3TopRightX = 847
left3x3TopRightY = 829

left3x3BottomRightX = 847
left3x3BottomRightY = 896

left3x3BottomLeftX = 780
left3x3BottomLeftY = 896

# left 3x2
left3x2TopLeftX = 795
left3x2TopLeftY = 832

left3x2TopRightX = 832
left3x2TopRightY = 832

left3x2BottomRightX = 835
left3x2BottomRightY = 892

left3x2BottomLeftX = 794
left3x2BottomLeftY = 892

# left 2x3
left2x3TopLeftX = 784
left2x3TopLeftY = 841

left2x3TopRightX = 844
left2x3TopRightY = 841

left2x3BottomRightX = 844
left2x3BottomRightY = 879

left2x3BottomLeftX = 783
left2x3BottomLeftY = 880

# left 2x2
left2x2TopLeftX = 793
left2x2TopLeftY = 843

left2x2TopRightX = 835
left2x2TopRightY = 845

left2x2BottomRightX = 835
left2x2BottomRightY = 880

left2x2BottomLeftX = 793
left2x2BottomLeftY = 880

# FUNK-SHUNS

def colorMatch(color1, color2, strictness='lax'):
    rdiff = abs(color1[0] - color2[0])
    gdiff = abs(color1[1] - color2[1])
    bdiff = abs(color1[2] - color2[2])
    total = rdiff + gdiff + bdiff
    if (strictness == 'lax'):
        output = (total < 30)
    elif (strictness == 'strict'):
        output = (total < 10)
    return output

def XcordToPixel(Xcord):
    pixel = 767+(54*Xcord)
    return pixel

def YcordToPixel(Ycord):
    pixel = 327+(54*Ycord)
    return pixel

def blockFilled(Xcord, Ycord):
    if (Xcord >= 0 and Xcord <= 7 and Ycord >= 0 and Ycord <= 7):
        return testBoard[Xcord + (8 * Ycord)]
    else:
        return False

def fillTestBlock(Xcord, Ycord):
    testBoard[Xcord + (8 * Ycord)] = True

def emptyTestBlock(Xcord, Ycord):
    testBoard[Xcord + (8 * Ycord)] = False

def updateTestBoard(Xcord, Ycord, pieceID):
    if (pieceID == 1):
        fillTestBlock(Xcord, Ycord)
    elif (pieceID == 2):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
    elif (pieceID == 3):
        fillTestBlock(Xcord, Ycord) 
        fillTestBlock(Xcord, Ycord + 1)
    elif (pieceID == 4):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 5):
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
    elif (pieceID == 6):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord + 2, Ycord + 2)
    elif (pieceID == 7):
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
    elif (pieceID == 8):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
    elif (pieceID == 9):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
    elif (pieceID == 10):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 11):
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 12):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 1)
    elif (pieceID == 13):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
    elif (pieceID == 14):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)           
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 15):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 16):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 17):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 18):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 19):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 20):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 21):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 22):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 23):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 24):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 2)
    elif (pieceID == 25):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
    elif (pieceID == 26):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 27):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 28):
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord)
    elif (pieceID == 29):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
    elif (pieceID == 30):
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 1)
    elif (pieceID == 31):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 3, Ycord)
    elif (pieceID == 32):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord, Ycord + 3)
    elif (pieceID == 33):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord, Ycord + 3)
        fillTestBlock(Xcord, Ycord + 4)
    elif (pieceID == 34):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 3, Ycord)
        fillTestBlock(Xcord + 4, Ycord)
    elif (pieceID == 35):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord + 2, Ycord + 1)
    elif (pieceID == 36):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 2)
    elif (pieceID == 37):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord + 1, Ycord + 1)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 2, Ycord + 2)
    elif (pieceID == 38):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2)
    elif (pieceID == 39):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord + 1, Ycord)
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord + 2, Ycord + 2)
    elif (pieceID == 40):
        fillTestBlock(Xcord + 2, Ycord)
        fillTestBlock(Xcord + 2, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2) 
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 2, Ycord + 2)
    elif (pieceID == 41):
        fillTestBlock(Xcord, Ycord)
        fillTestBlock(Xcord, Ycord + 1)
        fillTestBlock(Xcord, Ycord + 2) 
        fillTestBlock(Xcord + 1, Ycord + 2)
        fillTestBlock(Xcord + 2, Ycord + 2)
    elif (pieceID == 0):
        time.sleep(0)
    else:
        sys.exit("no piece found")

    global testBrokenRows    

    rowsToBeBroken = []
    columnsToBeBroken = []
    rowNum = 0
    columnNum = 0

    while(rowNum < 8):
        if (blockFilled(0, rowNum) and  blockFilled(1, rowNum) and  blockFilled(2, rowNum) and  blockFilled(3, rowNum)  
            and  blockFilled(4, rowNum) and  blockFilled(5, rowNum) and  blockFilled(6, rowNum) and  blockFilled(7, rowNum)):
            rowsToBeBroken.append(rowNum)
        rowNum += 1

    while(columnNum < 8):
        if (blockFilled(columnNum, 0) and blockFilled(columnNum, 1) and blockFilled(columnNum, 2) and blockFilled(columnNum, 3)  
            and blockFilled(columnNum, 4) and blockFilled(columnNum, 5) and blockFilled(columnNum, 6) and blockFilled(columnNum, 7)):
            columnsToBeBroken.append(columnNum)
        columnNum += 1

    rowNum = 0
    columnNum = 0

    while(rowNum < 8):
        if (rowNum in rowsToBeBroken):
            emptyTestBlock(0, rowNum)
            emptyTestBlock(1, rowNum)
            emptyTestBlock(2, rowNum)
            emptyTestBlock(3, rowNum)
            emptyTestBlock(4, rowNum)
            emptyTestBlock(5, rowNum)
            emptyTestBlock(6, rowNum)
            emptyTestBlock(7, rowNum)
            testBrokenRows += 1
        rowNum += 1

    while(columnNum < 8):
        if (columnNum in columnsToBeBroken):
            emptyTestBlock(columnNum, 0)
            emptyTestBlock(columnNum, 1)
            emptyTestBlock(columnNum, 2)
            emptyTestBlock(columnNum, 3)
            emptyTestBlock(columnNum, 4)
            emptyTestBlock(columnNum, 5)
            emptyTestBlock(columnNum, 6)
            emptyTestBlock(columnNum, 7)
            testBrokenRows += 1
        columnNum += 1

def canPieceFit(Xcord, Ycord, pieceID):
    if (pieceID == 1):
        return not blockFilled(Xcord, Ycord)
    elif (pieceID == 2):
        if (Xcord < 7):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord))
        else:
            return False
    elif (pieceID == 3):
        if (Ycord < 7):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1))
        else:
            return False
    elif (pieceID == 4):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 5):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord, Ycord + 1))
        else:
            return False
    elif (pieceID == 6):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord + 2, Ycord + 2))
        else:
            return False
    elif (pieceID == 7):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord, Ycord + 2))
        else:
            return False
    elif (pieceID == 8):
        if (Xcord < 6):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord))
        else:
            return False
    elif (pieceID == 9):
        if (Ycord < 6):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord + 2))
        else:
            return False
    elif (pieceID == 10):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 11):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 12):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord, Ycord + 1))
        else:
            return False
    elif (pieceID == 13):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord, Ycord + 1))
        else:
            return False
    elif (pieceID == 14):
        if ((Ycord < 7) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 15):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 16):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 17):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 18):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 19):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 20):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord)
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 21):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 22):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 23):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 24):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 2))
        else:
            return False
    elif (pieceID == 25):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord, Ycord + 1))
        else:
            return False
    elif (pieceID == 26):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 27):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord)
                    and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 28):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord))
        else:
            return False
    elif (pieceID == 29):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 2, Ycord + 1))
        else:
            return False
    elif (pieceID == 30):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 1))
        else:
            return False
    elif (pieceID == 31):
        if ((Xcord < 5)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord)
                    and not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 3, Ycord))
        else:
            return False
    elif (pieceID == 32):
        if ((Ycord < 5)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord, Ycord + 3))
        else:
            return False
    elif (pieceID == 33):
        if ((Ycord < 4)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord + 2)
                    and not blockFilled(Xcord, Ycord + 3) and not blockFilled(Xcord, Ycord + 4))
        else:
            return False
    elif (pieceID == 34):
        if ((Xcord < 4)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord + 3, Ycord) and not blockFilled(Xcord + 4, Ycord))
        else:
            return False
    elif (pieceID == 35):
        if ((Ycord < 7) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord + 2, Ycord + 1))
        else:
            return False
    elif (pieceID == 36):
        if ((Ycord < 6) and (Xcord < 7)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord + 2)
                    and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 2))
        else:
            return False
    elif (pieceID == 37):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord + 1, Ycord + 1) and not blockFilled(Xcord + 2, Ycord + 1)
                    and not blockFilled(Xcord, Ycord + 2) and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 2, Ycord + 2))
        else:
            return False
    elif (pieceID == 38):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord + 2) )
        else:
            return False
    elif (pieceID == 39):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord + 1, Ycord) and not blockFilled(Xcord + 2, Ycord)
                    and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord + 2, Ycord + 2))
        else:
            return False
    elif (pieceID == 40):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord + 2, Ycord) and not blockFilled(Xcord + 2, Ycord + 1) and not blockFilled(Xcord, Ycord + 2) 
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 2, Ycord + 2))
        else:
            return False
    elif (pieceID == 41):
        if ((Ycord < 6) and (Xcord < 6)):
            return (not blockFilled(Xcord, Ycord) and not blockFilled(Xcord, Ycord + 1) and not blockFilled(Xcord, Ycord + 2) 
                    and not blockFilled(Xcord + 1, Ycord + 2) and not blockFilled(Xcord + 2, Ycord + 2))
        else:
            return False
    elif (pieceID == 0):
        return True
    else:
        return False

def movePieceToBoard(Xcord, Ycord, pieceID, slot):
    slot -= 1
    pyautogui.moveTo(left_pointForID1X + (slot * 143), pointForID1Y, duration=1)

    Xto00 = 0
    Yto00 = 0
    if (pieceID == 1):
        Xto00 = 783
        Yto00 = 568
    elif (pieceID == 2):
        Xto00 = 799
        Yto00 = 566
    elif (pieceID == 3):
        Xto00 = 782
        Yto00 = 587
    elif (pieceID == 8):
        Xto00 = 817
        Yto00 = 565
    elif (pieceID == 9):
        Xto00 = 781
        Yto00 = 604
    elif (pieceID == 31):
        Xto00 = 841
        Yto00 = 568
    elif (pieceID == 32):
        Xto00 = 780
        Yto00 = 624
    elif (pieceID == 33):
        Xto00 = 780
        Yto00 = 642
    elif (pieceID == 34):
        Xto00 = 859
        Yto00 = 563
    elif ((pieceID >= 10 and pieceID <=14) or pieceID == 4 or pieceID == 5):
        Xto00 = 803
        Yto00 = 584
    elif ((pieceID >= 15 and pieceID <= 30 and (pieceID % 2) == 1) or pieceID == 35):
        Xto00 = 821
        Yto00 = 585
    elif ((pieceID >= 15 and pieceID <= 30 and (pieceID % 2) == 0) or pieceID == 36):
        Xto00 = 803
        Yto00 = 606
    elif (pieceID >= 37 or pieceID == 6 or pieceID == 7):
        Xto00 = 821
        Yto00 = 607
    elif (pieceID == 0):
        Xto00 = 500
        Yto00 = 500
    else:
        sys.exit("no can do!!!")
    
    # pyautogui.mouseDown(button='left')
    # pyautogui.moveRel(-100 * slot, 0, duration=1)
    # pyautogui.moveTo(Xto00 + (43 * slot), Yto00, duration=1)
    # pyautogui.moveRel(round((Xcord * 54)/1.43), round((Ycord * 54)/1.43), duration=1)
    # pyautogui.mouseUp(button='left')
    pyautogui.dragTo(Xto00 + (43 * slot) + round((Xcord * 55)/1.43), Yto00 + round((Ycord * 55)/1.43), duration=1)

def findHappinessFactor():
    happinessFactor = 0
    YcordForLoop = 0
    while (YcordForLoop < 8):
        XcordForLoop = 0
        while (XcordForLoop < 8):
            blockType = blockFilled(XcordForLoop, YcordForLoop)
            sidesFilled = 0
            if (XcordForLoop != 0):
                if (blockFilled(XcordForLoop - 1, YcordForLoop) == blockType):
                    sidesFilled += 1
            elif (YcordForLoop != 0):
                if (blockFilled(XcordForLoop, YcordForLoop - 1) == blockType):
                    sidesFilled += 1
            elif (XcordForLoop != 7):
                if (blockFilled(XcordForLoop + 1, YcordForLoop) == blockType):
                    sidesFilled += 1
            elif (YcordForLoop != 7):
                if (blockFilled(XcordForLoop, YcordForLoop + 1) == blockType):
                    sidesFilled += 1
            happinessFactor += sidesFilled - 2
            XcordForLoop += 1
        YcordForLoop += 1
    return happinessFactor


# real program

time.sleep(1)

ColtonsCatIsCool = True

while (ColtonsCatIsCool):

    time.sleep(2.5)

    mouseX, mouseY = pyautogui.position()
    pyautogui.moveTo(200, 200, duration=0.2)
    bgBoardColor = pyautogui.pixel(mouseX, mouseY)

    YCord = 0
    while (YCord !=8):
        XCord = 0
        while (XCord != 8):
            boxColor = list(pyautogui.pixel(XcordToPixel(XCord), YcordToPixel(YCord)))
            realBoard.append(not colorMatch(bgBoardColor, boxColor))
            XCord += 1
        YCord += 1

   
    bgPieceColor = list(pyautogui.pixel(960, 980))
    if (not colorMatch(bgPieceColor, bgGoodPieceColor, 'strict')):
        pyautogui.moveTo(1158, 134, duration=0.5)
        pyautogui.click(button='left')
        pyautogui.moveTo(947, 424, duration=0.5)
        pyautogui.click(button='left')
        time.sleep(0.5)
        bgPieceColor = list(pyautogui.pixel(960, 980))

    pyautogui.moveTo(200, 200,duration=0.2)

    lastPieceIDs = pieceIDs.copy()
    pieceNum = 0
    while (pieceNum != 3):
            #3x3
        topLeft3x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x3TopLeftX + (pieceNum * 143), left3x3TopLeftY))
        topRight3x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x3TopRightX + (pieceNum * 143), left3x3TopRightY))
        bottomRight3x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x3BottomRightX + (pieceNum * 143), left3x3BottomRightY))
        bottomLeft3x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x3BottomLeftX + (pieceNum * 143), left3x3BottomLeftY))

            #2x3 = 2 rows 3 columns 
        topLeft2x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x3TopLeftX + (pieceNum * 143), left2x3TopLeftY))
        topRight2x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x3TopRightX + (pieceNum * 143), left2x3TopRightY))
        bottomRight2x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x3BottomRightX + (pieceNum * 143), left2x3BottomRightY))
        bottomLeft2x3 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x3BottomLeftX + (pieceNum * 143), left2x3BottomLeftY))

            #3x2 = 3 rows 2 columns
        topLeft3x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x2TopLeftX + (pieceNum * 143), left3x2TopLeftY))
        topRight3x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x2TopRightX + (pieceNum * 143), left3x2TopRightY))
        bottomRight3x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x2BottomRightX + (pieceNum * 143), left3x2BottomRightY))
        bottomLeft3x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left3x2BottomLeftX + (pieceNum * 143), left3x2BottomLeftY))

            #2x2
        topLeft2x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x2TopLeftX + (pieceNum * 143), left2x2TopLeftY))
        topRight2x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x2TopRightX + (pieceNum * 143), left2x2TopRightY))
        bottomRight2x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x2BottomRightX + (pieceNum * 143), left2x2BottomRightY))
        bottomLeft2x2 = not colorMatch(bgPieceColor, pyautogui.pixel(left2x2BottomLeftX + (pieceNum * 143), left2x2BottomLeftY))
            
            # long stuff 
        if (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID33X + (pieceNum * 143), pointForID33Y))):
            pieceIDs[pieceNum] = 33
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID34X + (pieceNum * 143), pointForID34Y))):
            pieceIDs[pieceNum] = 34
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID32X + (pieceNum * 143), pointForID32Y))):
            pieceIDs[pieceNum] = 32
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID31X + (pieceNum * 143), pointForID31Y))):
            pieceIDs[pieceNum] = 31

            # 3x3  
        elif ((topLeft3x3) and (topRight3x3) and (bottomLeft3x3) and (bottomRight3x3)):
            pieceIDs[pieceNum] = 37
        elif ((topRight3x3) and (bottomLeft3x3) and (bottomRight3x3)):
            pieceIDs[pieceNum] = 40
        elif ((topLeft3x3) and (bottomLeft3x3) and (bottomRight3x3)):
            pieceIDs[pieceNum] = 41
        elif ((topLeft3x3) and (topRight3x3)and (bottomRight3x3)):
            pieceIDs[pieceNum] = 39
        elif ((topLeft3x3) and (topRight3x3) and (bottomLeft3x3)):
            pieceIDs[pieceNum] = 38
        elif ((topLeft3x3) and (bottomRight3x3)):
            pieceIDs[pieceNum] = 6
        elif ((topRight3x3) and (bottomLeft3x3)):
            pieceIDs[pieceNum] = 7

            # 2x3
        elif ((topLeft2x3) and (topRight2x3) and (bottomLeft2x3) and (bottomRight2x3)):
            pieceIDs[pieceNum] = 35
        elif ((topRight2x3) and (bottomLeft2x3) and (bottomRight2x3)):
            pieceIDs[pieceNum] = 23
        elif ((topLeft2x3) and (bottomLeft2x3) and (bottomRight2x3)):
            pieceIDs[pieceNum] = 27
        elif ((topLeft2x3) and (topRight2x3)and (bottomRight2x3)):
            pieceIDs[pieceNum] = 29
        elif ((topLeft2x3) and (topRight2x3) and (bottomLeft2x3)):
            pieceIDs[pieceNum] = 25
        elif ((topLeft2x3) and (bottomRight2x3)):
            pieceIDs[pieceNum] = 21
        elif ((topRight2x3) and (bottomLeft2x3)):
            pieceIDs[pieceNum] = 19
        elif ((topLeft2x3) and (topRight2x3)):
            pieceIDs[pieceNum] = 15
        elif ((bottomLeft2x3) and (bottomRight2x3)):
            pieceIDs[pieceNum] = 17

            # 3x2
        elif ((topLeft3x2) and (topRight3x2) and (bottomLeft3x2) and (bottomRight3x2)):
            pieceIDs[pieceNum] = 36
        elif ((topRight3x2) and (bottomLeft3x2) and (bottomRight3x2)):
            pieceIDs[pieceNum] = 30
        elif ((topLeft3x2) and (bottomLeft3x2) and (bottomRight3x2)):
            pieceIDs[pieceNum] = 24
        elif ((topLeft3x2) and (topRight3x2)and (bottomRight3x2)):
            pieceIDs[pieceNum] = 26
        elif ((topLeft3x2) and (topRight3x2) and (bottomLeft3x2)):
            pieceIDs[pieceNum] = 28
        elif ((topLeft3x2) and (bottomRight3x2)):
            pieceIDs[pieceNum] = 20
        elif ((topRight3x2) and (bottomLeft3x2)):
            pieceIDs[pieceNum] = 22
        elif ((topLeft3x2) and (bottomLeft3x2)):
            pieceIDs[pieceNum] = 18
        elif ((topRight3x2) and (bottomRight3x2)):
            pieceIDs[pieceNum] = 16
            
            # short long stuff
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID8X + (pieceNum * 143), pointForID8Y))):
            pieceIDs[pieceNum] = 8
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID9X + (pieceNum * 143), pointForID9Y))):
            pieceIDs[pieceNum] = 9

            # 2x2  
        elif ((topLeft2x2) and (topRight2x2) and (bottomLeft2x2) and (bottomRight2x2)):
            pieceIDs[pieceNum] = 14
        elif ((topRight2x2) and (bottomLeft2x2) and (bottomRight2x2)):
            pieceIDs[pieceNum] = 11
        elif ((topLeft2x2) and (bottomLeft2x2) and (bottomRight2x2)):
            pieceIDs[pieceNum] = 12
        elif ((topLeft2x2) and (topRight2x2)and (bottomRight2x2)):
            pieceIDs[pieceNum] = 10
        elif ((topLeft2x2) and (topRight2x2) and (bottomLeft2x2)):
            pieceIDs[pieceNum] = 13
        elif ((topLeft2x2) and (bottomRight2x2)):
            pieceIDs[pieceNum] = 4
        elif ((topRight2x2) and (bottomLeft2x2)):
            pieceIDs[pieceNum] = 5

            # even shorter long stuff
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID3X + (pieceNum * 143), pointForID3Y))):
            pieceIDs[pieceNum] = 3
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID2X + (pieceNum * 143), pointForID2Y))):
            pieceIDs[pieceNum] = 2

            # THE DOT
        elif (not colorMatch(bgPieceColor, pyautogui.pixel(left_pointForID1X + (pieceNum * 143), pointForID1Y))):
            pieceIDs[pieceNum] = 1
        else:
            pieceIDs[pieceNum] = 0

        pieceNum += 1

    # if (pieceIDs == [33, 33, 33]):
    #     print(bgPieceColor)
    #     print(pyautogui.pixel(left_pointForID33X + (0 * 143), pointForID33Y))
    #     sys.exit("33 33 33")
    
    bestBrokenRows = -1
    bestHappinessFactor = -100000000000
    bestOrder = 0

    testOrder = 123
    testP1Ycord = 0
    while (testP1Ycord !=8):
        testP1Xcord = 0
        while (testP1Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP2Ycord = 0
                while (testP2Ycord < 8):
                    testP2Xcord = 0
                    while (testP2Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                            updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP3Ycord = 0
                            while (testP3Ycord < 8):
                                testP3Xcord = 0
                                while (testP3Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                                        updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP3Xcord += 1
                                testP3Ycord += 1
                        testP2Xcord += 1
                    testP2Ycord += 1
            testP1Xcord += 1
        testP1Ycord += 1

    testOrder = 132
    testP1Ycord = 0
    while (testP1Ycord !=8):
        testP1Xcord = 0
        while (testP1Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP3Ycord = 0
                while (testP3Ycord < 8):
                    testP3Xcord = 0
                    while (testP3Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                            updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP2Ycord = 0
                            while (testP2Ycord < 8):
                                testP2Xcord = 0
                                while (testP2Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                                        updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP2Xcord += 1
                                testP2Ycord += 1
                        testP3Xcord += 1
                    testP3Ycord += 1
            testP1Xcord += 1
        testP1Ycord += 1

    testOrder = 213
    testP2Ycord = 0
    while (testP2Ycord !=8):
        testP2Xcord = 0
        while (testP2Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP1Ycord = 0
                while (testP1Ycord < 8):
                    testP1Xcord = 0
                    while (testP1Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                            updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP3Ycord = 0
                            while (testP3Ycord < 8):
                                testP3Xcord = 0
                                while (testP3Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                                        updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP3Xcord += 1
                                testP3Ycord += 1
                        testP1Xcord += 1
                    testP1Ycord += 1
            testP2Xcord += 1
        testP2Ycord += 1

    testOrder = 231
    testP2Ycord = 0
    while (testP2Ycord !=8):
        testP2Xcord = 0
        while (testP2Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP3Ycord = 0
                while (testP3Ycord < 8):
                    testP3Xcord = 0
                    while (testP3Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                            updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP1Ycord = 0
                            while (testP1Ycord < 8):
                                testP1Xcord = 0
                                while (testP1Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                                        updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP1Xcord += 1
                                testP1Ycord += 1
                        testP3Xcord += 1
                    testP3Ycord += 1
            testP2Xcord += 1
        testP2Ycord += 1

    testOrder = 312
    testP3Ycord = 0
    while (testP3Ycord !=8):
        testP3Xcord = 0
        while (testP3Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP1Ycord = 0
                while (testP1Ycord < 8):
                    testP1Xcord = 0
                    while (testP1Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                            updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP2Ycord = 0
                            while (testP2Ycord < 8):
                                testP2Xcord = 0
                                while (testP2Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                                        updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP2Xcord += 1
                                testP2Ycord += 1
                        testP1Xcord += 1
                    testP1Ycord += 1
            testP3Xcord += 1
        testP3Ycord += 1

    testOrder = 321
    testP3Ycord = 0
    while (testP3Ycord !=8):
        testP3Xcord = 0
        while (testP3Xcord != 8):
            testBoard = realBoard.copy()
            testBrokenRows = 0
            if (canPieceFit(testP3Xcord, testP3Ycord, pieceIDs[2])):
                updateTestBoard(testP3Xcord, testP3Ycord, pieceIDs[2])
                placeHolderBoard1 = testBoard.copy()
                helperTestBrokenRows1 = testBrokenRows
                testP2Ycord = 0
                while (testP2Ycord < 8):
                    testP2Xcord = 0
                    while (testP2Xcord < 8):
                        testBoard = placeHolderBoard1.copy()
                        testBrokenRows = helperTestBrokenRows1
                        if (canPieceFit(testP2Xcord, testP2Ycord, pieceIDs[1])):
                            updateTestBoard(testP2Xcord, testP2Ycord, pieceIDs[1])
                            placeHolderBoard2 = testBoard.copy()
                            helperTestBrokenRows2 = testBrokenRows
                            testP1Ycord = 0
                            while (testP1Ycord < 8):
                                testP1Xcord = 0
                                while (testP1Xcord < 8):
                                    testBoard = placeHolderBoard2.copy()
                                    testBrokenRows = helperTestBrokenRows2
                                    if (canPieceFit(testP1Xcord, testP1Ycord, pieceIDs[0])):
                                        updateTestBoard(testP1Xcord, testP1Ycord, pieceIDs[0])
                                        if (testBrokenRows > 0):
                                            testHappinessFactor = 1000000000000 + findHappinessFactor()
                                        else:
                                            testHappinessFactor = findHappinessFactor()
                                        if ((testHappinessFactor > bestHappinessFactor)):
                                            bestBoard = testBoard.copy()
                                            bestHappinessFactor = testHappinessFactor
                                            bestOrder = testOrder
                                            
                                            bestP1Xcord = testP1Xcord
                                            bestP1Ycord = testP1Ycord

                                            bestP2Xcord = testP2Xcord
                                            bestP2Ycord = testP2Ycord

                                            bestP3Xcord = testP3Xcord
                                            bestP3Ycord = testP3Ycord
                                    testP1Xcord += 1
                                testP1Ycord += 1
                        testP2Xcord += 1
                    testP2Ycord += 1
            testP3Xcord += 1
        testP3Ycord += 1

    if (bestOrder == 123):
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
    elif (bestOrder == 132):
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
    elif (bestOrder == 213):
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
    elif (bestOrder == 231):
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
    elif (bestOrder == 312):
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
    elif (bestOrder == 321):
        movePieceToBoard(bestP3Xcord, bestP3Ycord, pieceIDs[2], 3)
        movePieceToBoard(bestP2Xcord, bestP2Ycord, pieceIDs[1], 2)
        movePieceToBoard(bestP1Xcord, bestP1Ycord, pieceIDs[0], 1)
    else:
        sys.exit("NO CAN DO!!!")

    # realBoard = bestBoard.copy()

    realBoard = []
    testBoard = bestBoard.copy()

    hasFoundEmpty = False
    YCord = 1
    while (YCord < 7 and hasFoundEmpty == False):
        XCord = 1
        while (XCord < 7 and hasFoundEmpty == False):
            if (not blockFilled(XCord, YCord)):
                if (pieceIDs == lastPieceIDs):
                    pyautogui.moveTo(XcordToPixel(XCord + errorNum), YcordToPixel(YCord), duration=0.2)
                    errorNum += 1
                else:
                    errorNum = -1
                    pyautogui.moveTo(XcordToPixel(XCord), YcordToPixel(YCord), duration=0.2)
                hasFoundEmpty = True
            XCord += 1
        YCord += 1


# print(bestP1Xcord, bestP1Ycord)
# print(bestP2Xcord, bestP2Ycord)
# print(bestP3Xcord, bestP3Ycord)
# print(bestBrokenRows, bestOrder)
# print(pieceIDs)








# pyautogui.moveTo(left_pointForID1X + (1 * 143), pointForID1Y, duration=0.5)
# time.sleep(7)
# print(pyautogui.position())
# pyautogui.moveTo(200, 200, duration=2)
# # movePieceToBoard(6, 6, 2, 1)
# # movePieceToBoard(5, 5, 37, 0)