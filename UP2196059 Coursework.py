###WRITTEN BY JUAN RAFAEL MORENO - UP2196059

from graphics import *

def main():
    
    def studentInputs():
        studentNumberInput = input("Please input your student number: ")
        patchSize = int(input("Please input the patch size, 5 for 5x5, 7 for 7x7, 9 for 9x9: "))
        if patchSize == 5:
            win = GraphWin("500x500", 500, 500)
            patchParameters(win, studentNumberInput, 5)
        elif patchSize == 7:
            win = GraphWin("700x700", 700, 700)
            patchParameters(win, studentNumberInput, 7)
        elif patchSize == 9:
            win = GraphWin("900x900", 900, 900)
            patchParameters(win, studentNumberInput, 9)
        else:
            print("Please input 5, 7 or 9 for patches!")

    def patchParameters(win, studentNumber, size):
        penultimatePatch = int(studentNumber[-2])
        finalPatch = int(studentNumber[-1])
        colours = []
        sameColourCheck = False
        loop = 0
        while loop < 3:
            colourInput = input("Please input one of the three colours you want to input (red, green, blue, magenta, orange, yellow or cyan): ").lower()
            if colourInput == "red" or colourInput == "magenta" or colourInput == "orange" or colourInput == "yellow" or colourInput == "cyan" or colourInput == "green" or colourInput == "blue":
                for i in range(len(colours)):
                    if colourInput == colours[i]:
                        print("You have already inputted that colour")
                        sameColourCheck = True
                if sameColourCheck == False:
                    colours.append(colourInput)
                    loop = loop + 1
                else:
                    sameColourCheck = False
            else:
                print("Please input from the colours given")
        patchColours, patchDesigns = totalBoard(win, studentNumber[-3], size)
        for j in range(len(patchColours)):
            colourLine = patchColours[j]
            patchLine = patchDesigns[j]
            for i in range(len(patchColours[j])):
                colourNumber = colourLine[i]
                colour = colours[int(colourNumber)]
                patchType = patchLine[i]
                patchDrawing(win, (i * 100), (j * 100), patchType, colour, penultimatePatch, finalPatch)    
                    
    def patchDrawing(win, tlX, tlY, patchType, colour, penultimatePatch, finalPatch):
        patchW = 100
        patchH = 100
        if patchType == "C":
            drawRectangle(win, tlX, tlY, colour, colour, patchW, patchH)
        elif patchType == "P":
            drawRectangle(win, tlX, tlY, "white", "white", patchW, patchH)
            penultimatePatchSelector(win, tlX, tlY, colour, penultimatePatch)
        elif patchType == "F":
            drawRectangle(win, tlX, tlY, "white", "white", patchW, patchH)
            finalPatchSelector(win, tlX, tlY, colour, finalPatch)
    
    def penultimatePatchSelector(win, tlX, tlY, colour, penultimatePatch):
        if penultimatePatch == 0:
            patchP0(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 1:
            patchP1(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 2:
            patchP2(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 3:
            patchP3(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 4:
            patchP4(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 5:
            patchP5(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 6:
            patchP6(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 7:
            patchP7(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 8:
            patchP8(win, tlX, tlY, colour, "white")
        elif penultimatePatch == 9:
            patchP9(win, tlX, tlY, colour, "white")
    
    def finalPatchSelector(win, tlX, tlY, colour, finalPatch):
        if finalPatch == 0:
            patch0(win, tlX, tlY, colour, "white")
        elif finalPatch == 1:
            patch1(win, tlX, tlY, colour, "white")
        elif finalPatch == 2:
            patch2(win, tlX, tlY, colour, "white")
        elif finalPatch == 3:
            patch3(win, tlX, tlY, colour, "white")
        elif finalPatch == 4:
            patch4(win, tlX, tlY, colour, "white")
        elif finalPatch == 5:
            patch5(win, tlX, tlY, colour, "white")
        elif finalPatch == 6:
            patch6(win, tlX, tlY, colour, "white")
        elif finalPatch == 7:
            patch7(win, tlX, tlY, colour, "white")
        elif finalPatch == 8:
            patch8(win, tlX, tlY, colour, "white")
        elif finalPatch == 9:
            patch9(win, tlX, tlY, colour, "white")
        
    def totalBoard(win, studentNumber, size):
        
        #Blue = 0, Yellow = 1, Red = 2
        
        if studentNumber == "0":
            if size == 5:
                patchColours = ["01110", "20102", "22022", "20102","01110"]
                patchDesigns = ["CCCCC", "CFPFC", "CPFPC", "CFPFC","CCCCC"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0111110", "2011102", "2201022", "2220222", "2201011", "2011102", "0111110"]
                patchDesigns = ["CCCCCCC", "CFPPPFC", "CPFPFPC", "CPPFPPC", "CPFPFPC", "CFPPPFC", "CCCCCCC"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["011111110", "201111102", "220111022", "222010222", "222202222", "222010222", "220111022", "201111102", "011111110"]
                patchDesigns = ["CCCCCCCCC", "CFPPPPPFC", "CPFPPPFPC", "CPPFPFPPC", "CPPPFPPPC", "CPPFPFPPC", "CPFPPPFPC", "CFPPPPPFC", "CCCCCCCCC"]
                return patchColours, patchDesigns
        elif studentNumber == "1":
            if size == 5:
                patchColours = ["00001", "00012", "00122", "01222", "12222"]
                patchDesigns = ["PPPPF", "PCCCF", "PCFCF", "PCFCF", "FCFCF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0000001", "0000012", "0000122", "0001222", "0012222", "0122222", "1222222"]
                patchDesigns = ["PPPPPPF", "PCCCCCF", "PCCCFCF", "PCCCFCF", "PCFCFCF", "PCFCFCF", "FCFCFCF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["000000001", "000000012", "000000122", "000001222", "000012222", "000122222", "001222222", "012222222", "122222222"]
                patchDesigns = ["PPPPPPPPF", "PCCCCCCCF", "PCCCCCFCF", "PCCCCCFCF", "PCCCFCFCF", "PCCCFCFCF", "PCFCFCFCF", "PCFCFCFCF", "FCFCFCFCF"]
                return patchColours, patchDesigns
        elif studentNumber == "2":
            if size == 5:
                patchColours = ["01111", "20111", "22011", "22201", "22220"]
                patchDesigns = ["FFFFF", "CFCCF", "CPFCF", "CPPFF", "CCCCF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0111111", "2011111", "2201111", "2220111", "2222011", "2222201", "2222220"]
                patchDesigns = ["FFFFFFF", "CFCCCCF", "CPFCCCF", "CPPFCCF", "CPPPFCF", "CPPPPFF", "CCCCCCF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["011111111", "201111111", "220111111", "222011111", "222201111", "222220111", "222222011", "222222201", "222222220"]
                patchDesigns = ["FFFFFFFFF", "CFCCCCCCF", "CPFCCCCCF", "CPPFCCCCF", "CPPPFCCCF", "CPPPPFCCF", "CPPPPPFCF", "CPPPPPPFF", "CCCCCCCCF"]
                return patchColours, patchDesigns
        elif studentNumber == "3":
            if size == 5:
                patchColours = ["01010", "12221", "02220", "12221", "01010"]
                patchDesigns = ["FPPPP", "CFCCC", "PPFPP", "CCCFC", "PPPPF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0101010", "1222221", "0222220", "1222221", "0222220", "1222221", "0101010"]
                patchDesigns = ["FPPPPPP", "CFCCCCC", "PPFPPPP", "CCCFCCC", "PPPPFPP", "CCCCCFC", "PPPPPPF" ]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["010101010", "122222221", "022222220", "122222221", "022222220", "122222221", "022222220", "122222221", "010101010"]
                patchDesigns = ["FPPPPPPPP", "CFCCCCCCC", "PPFPPPPPP", "CCCFCCCCC", "PPPPFPPPP", "CCCCCFCCC", "PPPPPPFPP", "CCCCCCCFC", "PPPPPPPPF" ]
                return patchColours, patchDesigns
        elif studentNumber == "4":
            if size == 5:
                patchColours = ["00122", "00122", "11111", "22100", "22100"]
                patchDesigns = ["FCFCF", "FPFPF", "FPFPF", "FPFPF", "FCFCF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0001222", "0001222", "0001222", "1111111", "2221000", "2221000", "2221000"]
                patchDesigns = ["FCFCFCF", "FPFPFPF", "FPFPFPF", "FPFPFPF", "FPFPFPF", "FPFPFPF", "FCFCFCF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["000012222", "000012222", "000012222", "000012222", "111111111", "22221000", "22221000", "222210000", "222210000"]
                patchDesigns = ["FCCFCFCCF", "FPPFPFPPF", "FPPFPFPPF", "FPPFPFPPF", "FPPFPFPPF", "FPPFPFPPF", "FPPFPFPPF", "FPPFPFPPF", "FCCFCFCCF"]
                return patchColours, patchDesigns
        elif studentNumber == "5":
            if size == 5:
                patchColours = ["00000", "01110", "01120", "01220", "00000"]
                patchDesigns = ["FFFFF", "CCCCC", "FPPFF", "CCCCC", "FFFFF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0000000", "0111110", "0111120", "0111220", "0112220", "0122220", "0000000"]
                patchDesigns = ["FFFFFFF", "CCCCCCC", "FPPPPFF", "CCCCCCC", "FPPFFFF", "CCCCCCC", "FFFFFFF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["000000000", "011111110", "011111120", "011111220", "011112220", "011122220", "011222220", "012222220", "000000000"]
                patchDesigns = ["FFFFFFFFF", "CCCCCCCCC", "FPPPPPPFF", "CCCCCCCCC", "FPPPPFFFF", "CCCCCCCCC", "FPPFFFFFF", "CCCCCCCCC", "FFFFFFFFF"]
                return patchColours, patchDesigns
        elif studentNumber == "6":
            if size == 5:
                patchColours = ["00001", "00012", "00122", "01222", "12222"]
                patchDesigns = ["CCCCC", "CCCCC", "FFFCC", "FPFCC", "FFFCC"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0000001", "0000012", "0000122", "0001222", "0012222", "0122222", "1222222"]
                patchDesigns = ["CCCCCCC", "CCCCCCC", "CCCCCCC", "FFFFCCC", "FPPFCCC", "FPPFCCC", "FFFFCCC"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["000000001", "000000012", "000000122", "000001222", "000012222", "000122222", "001222222", "012222222", "122222222"]
                patchDesigns = ["CCCCCCCCC", "CCCCCCCCC", "CCCCCCCCC", "CCCCCCCCC", "FFFFFCCCC", "FPPPFCCCC", "FPPPFCCCC", "FPPPFCCCC", "FFFFFCCCC"]
                return patchColours, patchDesigns
        elif studentNumber == "7":
            if size == 5:
                patchColours = ["01111", "02111", "02011", "02021", "02020"]
                patchDesigns = ["CFFFF", "CPCCF", "CPPCF", "CPPPF", "CCCCC"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0111111", "0211111", "0201111", "0202111", "0202011", "0202021", "0202020"]
                patchDesigns = ["CFFFFFF", "CPCCCCF", "CPPCCCF", "CPPPCCF", "CPPPPCF", "CPPPPPF", "CCCCCCC"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["011111111", "021111111", "020111111", "020211111", "020201111", "020202111", "020202011", "020202021", "020202020"]
                patchDesigns = ["CFFFFFFFF", "CPCCCCCCF", "CPPCCCCCF", "CPPPCCCCF", "CPPPPCCCF", "CPPPPPCCF", "CPPPPPPCF", "CPPPPPPPF", "CCCCCCCCC"]
                return patchColours, patchDesigns
        elif studentNumber == "8":
            if size == 5:
                patchColours = ["00000", "10002", "11022", "10002", "00000"]
                patchDesigns = ["CCCCC", "PCCCP", "PPFPP", "CFFFC", "FFFFF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0000000", "1000002", "1100022", "1110222", "1100022", "1000002", "0000000"]
                patchDesigns = ["CCCCCCC", "PCCCCCP", "PPCCCPP", "PPPFPPP", "CCFFFCC", "CFFFFFC", "FFFFFFF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["000000000", "100000002", "110000022", "111000222", "111102222", "111000222", "110000022", "100000002", "000000000"]
                patchDesigns = ["CCCCCCCCC", "PCCCCCCCP", "PPCCCCCPP", "PPPCCCPPP", "PPPPFPPPP", "CCCFFFCCC", "CCFFFFFCC", "CFFFFFFFC", "FFFFFFFFF"]
                return patchColours, patchDesigns
        elif studentNumber == "9":
            if size == 5:
                patchColours = ["01110", "01110", "00000", "02220", "02220"]
                patchDesigns = ["FPFPF", "CFPFC", "FCFCF", "CFPFC", "FPFPF"]
                return patchColours, patchDesigns
            elif size == 7:
                patchColours = ["0111110", "0111110", "0111110", "0000000", "0222220", "0222220", "0222220"]
                patchDesigns = ["FPFPFPF", "CFPFPFC", "FPFPFPF", "CFCFCFC", "FPFPFPF", "CFPFPFC", "FPFPFPF"]
                return patchColours, patchDesigns
            elif size == 9:
                patchColours = ["011111110", "011111110", "011111110", "011111110", "000000000", "022222220", "022222220", "022222220", "022222220"]
                patchDesigns = ["FPFPFPFPF", "CFPFPFPFC", "CFPFPFPFC", "FPFPFPFPF", "CFCFCFCFC", "FPFPFPFPF", "CFPFPFPFC", "CFPFPFPFC", "FPFPFPFPF"]
                return patchColours, patchDesigns
    
    def variableAssignment(win, tL):
        tX = tL.getX()
        tY = tL.getY()
        return tX, tY
    
    def parameterAssignment(win, parameters):
        width = parameters[0]
        height = parameters[1]
        if len(parameters) > 2:
            radius = parameters[2]
            return width, height, radius
        else:
            return width, height
    
    def drawRectangle(win, x, y, colour, outline, width, height):
        rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        rectangle.setFill(colour)
        rectangle.setOutline(outline)
        rectangle.draw(win)
    
    def drawCircle(win, center, colour, width, height, radius):
        x = center.getX()
        y = center.getY()
        for j in range(0, 20, 10):
            for i in range(0, 20, 10):
                circle = Circle(Point(x + width / 2, y + height / 2), radius)
                circle.setFill(colour)
                circle.setOutline(colour)
                circle.draw(win)

    def writeMessage(win, i, j, text, colour, size):
        message = Text(Point(j + 10, i + 10), text)
        message.setFill(colour)
        message.setSize(size)
        message.draw(win)
    
    def drawDiamond(win, x, y, colour, width, height):
        p1 = Point(x, y + 10)
        p2 = Point(x + 10, y)
        p3 = Point(x + 20, y + 10)
        p4 = Point(x + 10, y + 20)
        polygon = Polygon(p1, p2, p3, p4)
        polygon.setFill(colour)
        polygon.setOutline(colour)
        polygon.draw(win)
    
    def drawArrow(win, tL, tY, width, height, colour, outline):
        p0 = Point(tL, tY)
        p1 = Point(tL, tY + 10)
        p2 = Point(tL + 10, tY + 20)
        p3 = Point(tL + 20, tY + 10)
        p4 = Point(tL + 20, tY)
        p5 = Point(tL + 10, tY + 10)
        polygon = Polygon(p0, p1, p2, p3, p4, p5)
        polygon.setFill(colour)
        polygon.setOutline(outline)
        polygon.draw(win)
                
    def drawTriangle(win, x, y, parameters, colour):
        p1 = Point(x, y + 20)
        p2 = Point(x + 10, y)
        p3 = Point(x + 20, y + 20)
        triangle = Polygon(p1, p2, p3)
        triangle.setFill(colour)
        triangle.setOutline(colour)
        triangle.draw(win)
    
    def drawSidewaysTriangle(win, x, y, width, height, radius, colour):
        p1 = Point(x + radius, y + radius)
        p2 = Point(x + width, y + height)
        p3 = Point(x + width, y)
        triangle = Polygon(p1, p2, p3)
        triangle.setFill(colour)
        triangle.setOutline(colour)
        triangle.draw(win)
    
    def downwardsTriangle(win, x, y, width, height, radius, colour):
        p1 = Point(x, y)
        p2 = Point(x + radius, y + height)
        p3 = Point(x + width, y)
        triangle = Polygon(p1, p2, p3)
        triangle.setFill(colour)
        triangle.setOutline(colour)
        triangle.draw(win)

    def drawCircles(win, x, y, colour, radius):
        for j in range (0, 20, 10):
            for i in range(0, 20, 10):
                circle = Circle(Point(x + (radius + i), y + (radius + j)), radius)
                circle.setFill(colour)
                circle.setOutline(colour)
                circle.draw(win)
    
    def drawLine(win, Point1, Point2, colour):
        line = Line(Point1, Point2)
        line.setFill(colour)
        line.draw(win)
    
    def drawCircleOutline(win, center, colour, outline, width, height, radius):
        x = center.getX()
        y = center.getY()
        for j in range(0, 20, 10):
            for i in range(0, 20, 10):
                circle = Circle(Point(x + width / 2, y + height / 2), radius)
                circle.setFill(colour)
                circle.setOutline(outline)
                circle.draw(win)
    
    def drawH(win, i, j, colour, outline, width, height):
        drawRectangle(win, i, j, colour, outline, 5, 25)
        drawRectangle(win, i + 5, j + 10, colour, outline, 15, 5)
        drawRectangle(win, i + 20, j, colour, outline, 5, 25)
    
    def drawI(win, i, j, colour, outline, width, height):
        drawRectangle(win, i, j, colour, outline, 25, 5)
        drawRectangle(win, i + 10, j + 5, colour, outline, 5, 15)
        drawRectangle(win, i, j + 20, colour, outline, 25, 5)
    
    def drawPacMan(win, x, y, center, colour1, width, height, radius, colour2):
        drawCircle(win, center, colour1, width, height, radius)
        drawSidewaysTriangle(win, x, y, width, height, radius, colour2)
    
    def drawFlippedPacman(win, x, y, center, colour1, width, height, radius, colour2):
        drawCircle(win, center, colour1, width, height, radius)
        reversewidth = width * -1
        reverseheight = height * -1
        reverseradius = radius * -1
        drawSidewaysTriangle(win, x + 20, y + 20, reversewidth, reverseheight, reverseradius, colour2)
            
    def redRectWhiteCircle(win, tL, parameters, colour, white):
        colourRect = colour
        colourRectOutline = colour
        colourCircle = white
        tX, tY = variableAssignment(win, tL)
        width, height, radius = parameterAssignment(win, parameters)
        drawRectangle(win, tX, tY, colourRect, colourRectOutline, width, height)
        drawCircles(win, tX, tY, colourCircle, radius)
    
    def whiteRectRedCircle(win, tL, parameters, colour, white):
        colourRect = white
        colourRectOutline = white
        colourCircle = colour
        tX, tY = variableAssignment(win, tL)
        width, height, radius = parameterAssignment(win, parameters)
        drawRectangle(win, tX, tY, colourRect, colourRectOutline, width, height)
        drawCircles(win, tX, tY, colourCircle, radius)
        
    def squareCirclesFull(win, tL, colour, parameters):
        tX, tY = variableAssignment(win, tL)
        width, height, radius = parameterAssignment(win, parameters)
        drawRectangle(win, tX, tY, colour[0], colour[2], width, height)
        drawCircle(win, Point(tX, tY), colour[1], width, height, radius)
    
    def squareCirclesAlternating(win, tL, colour, count, parameters):
        tX, tY = variableAssignment(win, tL)
        width, height, radius = parameterAssignment(win, parameters)
        if count == True:
            drawRectangle(win, tX, tY, colour[0], colour[2], width, height)
            drawCircle(win, Point(tX, tY), colour[1], width, height, radius)
        else:
            drawDiamond(win, tX, tY, colour[0], width, height)
            drawCircle(win, Point(tX, tY), colour[1], width, height, radius)
        
    def alternatingRectangles(win, i, j, count, parameters, colour, white):
        if count == True:
            redRectWhiteCircle(win, Point(i, j), parameters, colour, white)
        elif count == False:
            whiteRectRedCircle(win, Point(i, j), parameters, colour, white)
        
    def alternatingCirclesAndTriangles(win, i, j, center, count, parameters, colour):
        width, height, radius = parameterAssignment(win, parameters)
        if count == True:
            drawCircle(win, center, colour, width, height, radius)
        elif count == False:
            if i % 40 == 0:
                downwardsTriangle(win, i, j, width, height / 2, radius, colour)
                downwardsTriangle(win, i, j + radius, width, height / 2, radius, colour)
            else:
                reversewidth = width * -1
                reverseheight  = height * -1
                reverseradius  = radius * -1
                drawSidewaysTriangle(win, i, j, width - width, height, radius, colour)
                drawSidewaysTriangle(win, i + radius, j, width - width, height, radius, colour)
    
    def squareFiller(win, i, j, count, colour, squareFill, parameters):
        if squareFill == False:
            squareCirclesAlternating(win, Point(i, j), colour, count, parameters)
        else:
            squareCirclesFull(win, Point(i, j), colour, parameters)
        
    def alternatingBricks(win, count, tlX, tlY, j, colours):
        brickCount = True
        if count == True:
            for i in range(0, 100, 25):
                width = 25
                height = 10
                drawRectangle(win, tlX + i, tlY + j, colours[0], colours[2], width, height)
        else:
            for i in range(0, 100, 20):
                width = 20
                height = 10
                if brickCount == True:
                    drawRectangle(win, tlX + i, tlY + j, colours[0], colours[2], width, height)
                    brickCount = False
                else:
                    drawRectangle(win, tlX + i, tlY + j, colours[1], colours[2], width, height)
                    brickCount = True
    
    def alternatingPacMan(win, count, i, j, colours, parameters):
        width, height, radius = parameterAssignment(win, parameters)
        center = Point(i, j)
        if count == True:
            if j % 40 == 0:
                drawFlippedPacman(win, i, j, center, colours[0], width, height, radius, colours[1])
            else:
                drawPacMan(win, i, j, center, colours[0], width, height, radius, colours[1])
        elif count == False:
            drawRectangle(win, i, j, colours[0], colours[0], width, height)
            
    def RectangleSquare(win, i, j, colours, width, height):
        drawRectangle(win, i, j, colours[0], colours[2], width, height)
        drawRectangle(win, i + 5, j, colours[1], colours[2], width, height)
        drawRectangle(win, i + 10, j, colours[0], colours[2], width, height)
        drawRectangle(win, i + 15, j, colours[1], colours[2], width, height)
    
    def ReverseRectangleSquare(win, i, j, colours, width, height):
        drawRectangle(win, i, j, colours[0], colours[2], height, width)
        drawRectangle(win, i, j + 5, colours[1], colours[2], height, width)
        drawRectangle(win, i, j + 10, colours[0], colours[2], height, width)
        drawRectangle(win, i, j + 15, colours[1], colours[2], height, width)
    
    def alternatingHI(win, count, i, j, colours, parameters, lineCount, y):
        width, height = parameterAssignment(win, parameters)
        if lineCount == True:
            if count == True:
                drawRectangle(win, i, j, colours[1], colours[1], 25, 25)
                drawH(win, i, j, colours[0], colours[0], width, height)
            else:
                drawRectangle(win, i, j, colours[1], colours[1], 25, 25)
                drawI(win, i, j, colours[0], colours[0], width, height)
        else:
            if count == True:
                drawRectangle(win, i, j, colours[0], colours[0], 25, 25)
                drawH(win, i, j, colours[1], colours[1], width, height)
            else:
                drawRectangle(win, i, j, colours[0], colours[0], 25, 25)
                drawI(win, i, j, colours[1], colours[1], width, height)
    
    def alternatingRectangleSquares(win, count, i, j, colours, parameters):
        width, height = parameterAssignment(win, parameters)
        if count == True:
            RectangleSquare(win, i, j ,colours, width, height)
        else:
            ReverseRectangleSquare(win, i, j, colours, width, height)
        
    def circlesRectangles(win, i, j, count, parameters, lineCount, colour):
        width, height, radius = parameterAssignment(win, parameters)
        if count == True:
            if lineCount == True:
                 drawCircle(win, Point(i, j), colour, width, height, radius)
            else:
                drawCircle(win, Point(i-5, j), colour, width, height, radius)
                drawRectangle(win, i, j, colour, colour, width, height)
                drawCircle(win, Point(i+5, j), colour, width, height, radius)
        else:
            if lineCount == True:
                drawCircle(win, Point(i-5, j), colour, width, height, radius)
                drawRectangle(win, i, j, colour, colour, width, height)
                drawCircle(win, Point(i+5, j), colour, width, height, radius)
            else:   
                drawCircle(win, Point(i, j), colour, width, height, radius)
    
    def arrowZigZag(win, tL, tY, count, lineCount, parameters, colours):
        width, height = parameterAssignment(win, parameters)
        if lineCount == True:
            drawArrow(win, tL, tY, width, height, colours[0], colours[0])
        else:
            if count == False:
                drawArrow(win, tL, tY, width, height, colours[1], colours[0])
            else:
                drawArrow(win, tL, tY, width, height, colours[0], colours[0])
        
    def patch0(win, tlX, tlY, colour, white):
        x = True
        parameters = [100, 100]
        for i in range(0, 50, 5):
            parameters[0] = parameters[0] - 5
            parameters[1] = parameters[1] - 5
            j = i
            if x == True:
                drawRectangle(win, tlX + (i + 2), tlY + (j + 2), colour, colour, parameters[0] - i, parameters[1] - j)
                x = False
            else:
                drawRectangle(win, tlX + (i + 2), tlY + (j + 2), white, colour, parameters[0] - i, parameters[1] - j)
                x = True
            print(i)
        
    def patch1(win, tlX, tlY, colour, white):
        x = True
        parameters = [100, 100]
        for i in range(0, 100, 10):
            if x == True:
                drawRectangle(win, tlX, tlY + i, white, white, parameters[0], parameters[1])
                x = False
            else:
                drawRectangle(win, tlX, tlY + i, colour, colour, parameters[0], parameters[1])
                x = True
            parameters[0] = parameters[0] - 10
            parameters[1] = parameters[1] - 10
            
    def patch2(win, tlX, tlY, colour, white):
        count = True
        parameters = [20, 20, 10]
        for j in range(0, 100, 20):
            count = not count
            for i in range(0, 100, 20):
                if count == True:#
                    drawCircleOutline(win, Point(tlX + i, tlY + j), white, colour, parameters[0], parameters[1], parameters[2])
                else:
                    drawCircle(win, Point(tlX + i, tlY + j), colour, parameters[0], parameters[1], parameters[2])

    def patch3(win, tlX, tlY, colour, white):
        j = 100
        parameters = [10, 10]
        for i in range(0, 100, 10):
            j = j - 10
            drawRectangle(win, tlX + i, tlY + j, colour, colour, parameters[0], parameters[1])
            
    def patch4(win, tlX, tlY, colour, white):
        j = 50
        parameters = [10, 10]
        for i in range(50, 0, -5):
            j = j + 5
            drawCircleOutline(win, Point(tlX + 45, tlY + (j - 10)), white, colour, parameters[0], parameters[1], i)
                
    def patch5(win, tlX, tlY, colour, white):
        j = 0
        y = 100
        for i in range(0, 100, 10):
            j = j + 10
            drawLine(win, Point(tlX + i, tlY), Point(tlX + 100, tlY + j), colour)
            drawLine(win, Point(tlX, tlY + i), Point(tlX + j, tlY + 100), colour)
            
    def patch6(win, tlX, tlY, colour, white):
        j = 100
        for i in range(0, 100, 10):
            j = j - 10
            drawRectangle(win, tlX + i, tlY + j, colour, colour, tlX + 10, tlY + 10)
            
    def patch7(win, tlX, tlY, colour, white):
        j = 100
        for i in range(0, 100, 20):
            j = j - 20
            drawLine(win, Point(tlX + 0, tlY + j), Point(tlX + i + 20, tlY + 100), colour)
            drawLine(win, Point(tlX + i, tlY + 0), Point(tlX + 100, tlY + 100 - i), colour)
            drawLine(win, Point(tlX + 100, tlY + j), Point(tlX + 80 - i, tlY + 100), colour)
            drawLine(win, Point(tlX + 100 - i, tlY + 0), Point(tlX + 0, tlY + 100 - i), colour)

    def patch8(win, tlX, tlY, colour, white):
        for i in range(0, 100, 10):
            drawLine(win, Point(tlX + 50, tlY + 50), Point(tlX + i, tlY), colour)
        for i in range(0, 100, 10):
            drawLine(win, Point(tlX + 50, tlY + 50), Point(tlX + 100, tlY + i), colour)
        for i in range(0, 100, 10):
            drawLine(win, Point(tlX + 50, tlY + 50), Point(tlX + (100 - i), tlY + 100), colour)
        for i in range(0, 100, 10):
            drawLine(win, Point(tlX + 50, tlY + 50), Point(tlX, tlY + (100 - i)), colour)

    def patch9(win, tlX, tlY, colour, white):
        parameters = [20, 20]
        size = 10
        text = "hi!"
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                drawRectangle(win, tlX + i, tlY + j, white, colour, parameters[0], parameters[1])       
                writeMessage(win, tlY + i, tlX + j, text, colour, size)
                writeMessage(win, tlY + j, tlX + i, text, colour, size)
                
    def patchP0(win, tlX, tlY, colour, white):
        colours = ["red", "white"]
        count = True
        lineCount = True
        parameters = [20, 20]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                arrowZigZag(win, tlX + i, tlY + j, count, lineCount, parameters, colours)
                count = not count
            lineCount = not lineCount
            
    def patchP1(win, tlX, tlY, colour, white):
        count = True
        lineCount = True
        parameters = [10, 20, 10]
        for j in range(0, 100, 20):
            for i in range(0, 100, 25):
                circlesRectangles(win, (tlX + i) + 5, tlY + j, count, parameters, lineCount, colour)
                count = not count
            lineCount = not lineCount
            
    def patchP2(win, tlX, tlY, colour, white):
        count = True
        squareFill = True
        colours = [colour, white, colour]
        parameters = [20, 20, 5]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                if j % 40 == 0:
                    squareFill = False
                else:
                    squareFill = True
                squareFiller(win, tlX + i, tlY + j, count, colours, squareFill, parameters)
                count = not count
        
    def patchP3(win, tlX, tlY, colour, white):
        count = True
        parameters = [20, 20, 5]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                alternatingRectangles(win, tlX + i, tlY + j, count, parameters, colour, white)
                count = not count
    
    def patchP4(win, tlX, tlY, colour, white):
        count = True
        parameters = [20, 20]
        for j in range(0, 100, 20):
            if count == True:
                for i in range(0, 100, 20):
                    drawTriangle(win, tlX + i, tlY + j, parameters, colour)
                    count = False
            else:
                for i in range(-10, 110, 20):
                    parameters = [20, 20]
                    drawTriangle(win, tlX + i, tlY + j, parameters, colour)
                    count = True
                
    def patchP5(win, tlX, tlY, colour, white):
        count = True
        colours = [colour, white, "black"]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                parameters = [5, 20]
                alternatingRectangleSquares(win, count, tlX + i , tlY + j, colours, parameters)
                count = not count
        
    def patchP6(win, tlX, tlY, colour, white):
        count = True
        colours = [colour, white]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                parameters = [20, 20, 10]
                alternatingPacMan(win, count, tlX + i, tlY + j, colours, parameters)
                count = not count 
    
    def patchP7(win, tlX, tlY, colour, white):
        count = True
        colours = [colour, white, "black"]
        for j in range(0, 100, 10):
            alternatingBricks(win, count, tlX, tlY, j, colours)
            count = not count
        
    def patchP8(win, tlX, tlY, colour, white):
        count = True
        lineCount = True
        colours = [colour,white,"black"]
        parameters = [25, 25]
        for j in range(0, 100, 25):
            for i in range(0, 100, 25):
                alternatingHI(win, count, tlX + i, tlY + j, colours, parameters, lineCount, j)
                count = not count
            lineCount = not lineCount
            
    def patchP9(win, tlX, tlY, colour, white):
        count = True
        parameters = [20, 20, 10]
        for j in range(0, 100, 20):
            for i in range(0, 100, 20):
                alternatingCirclesAndTriangles(win, tlX + i, tlY + j, Point(tlX + i, tlY + j), count, parameters, colour)
                count = not count
    
    studentInputs()

main()