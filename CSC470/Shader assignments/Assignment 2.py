'''
Name: Olivia Spears
CWID: 10240548
Date Due: 1/11/2018
Assignment No. 2
---
This program will build off the previous assignment by implementing multiple objects and doing in-place rotations and scaling
---
'''
import math
from tkinter import *

CanvasWidth = 500
CanvasHeight = 500
d = 500

# ***************************** Initialize Pyramid Object ***************************
# The points for the three pyramids
apex1 = [100,50,50]
base1 = [75,0,25]
base2 = [125,0,25]
base3 = [125,0,75]
base4 = [75,0,75]

base5 = [-25,0,25]
base6 = [25,0,25]
base7 = [25,0,75]
base8 = [-25,0,75]
base9 = [-25,50,25]
base10 = [25,50,25]
base11 = [25,50,75]
base12 = [-25,50,75]

apex2 = [-100,50,50]
base13 = [-125,0,25]
base14 = [-75,0,25]
base15 = [-75,0,75]
base16 = [-125,0,75]

#************************************************************************************

# The pyramid class
class Pyramid:

    # This part is really just what used to be at the top with all the polys and such but now its in the class so it's remade whenever the class is initialized
    # It includes the individual points, a pointcloud, definitions for each polygon, and all the polygons in one object
    
    def __init__(self, ap, b1, b2, b3, b4):
        self.ap = ap
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.pointCloud = [ap, b1, b2, b3, b4]
        self.center = self.findCenter()
        self.frontpoly = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[2]]
        self.rightpoly = [self.pointCloud[0],self.pointCloud[2],self.pointCloud[3]]
        self.backpoly = [self.pointCloud[0],self.pointCloud[3],self.pointCloud[4]]
        self.leftpoly = [self.pointCloud[0],self.pointCloud[4],self.pointCloud[1]]
        self.bottompoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[3]]
        self.bottompoly2 = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1]]
        self.object = [self.frontpoly,self.rightpoly,self.backpoly,self.leftpoly,self.bottompoly1,self.bottompoly2]

    # This function updates the polygons using the point cloud and then the entire pyramid
    def update(self):
        self.frontpoly = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[2]]
        self.rightpoly = [self.pointCloud[0],self.pointCloud[2],self.pointCloud[3]]
        self.backpoly = [self.pointCloud[0],self.pointCloud[3],self.pointCloud[4]]
        self.leftpoly = [self.pointCloud[0],self.pointCloud[4],self.pointCloud[1]]
        self.bottompoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[3]]
        self.bottompoly2 = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1]]
        self.object = [self.frontpoly,self.rightpoly,self.backpoly,self.leftpoly,self.bottompoly1,self.bottompoly2]

    # This function resets the pyramid with the originally passed in points
    def reset(self):
        self.pointCloud = [self.ap, self.b1, self.b2, self.b3, self.b4]
        self.update()

    # This function will find the center of the pyramid by find the average of each point and creating a new set of coordinates
    def findCenter(self):
        xCoord = self.pointCloud[0][0] + self.pointCloud[1][0] + self.pointCloud[2][0] + self.pointCloud[3][0] + self.pointCloud[4][0]
        xCoord = xCoord/5
        zCoord = self.pointCloud[0][2] + self.pointCloud[1][2] + self.pointCloud[2][2] + self.pointCloud[3][2] + self.pointCloud[4][2]
        zCoord = zCoord/5
        yCoord = self.pointCloud[0][1] + self.pointCloud[1][1] + self.pointCloud[2][1] + self.pointCloud[3][1] + self.pointCloud[4][1]
        yCoord = yCoord/5
        center = [xCoord, yCoord, zCoord]
        return center

    def moveToOrigin(self, center):
        move = [0,0,0]
        i=0
        while (i<3):
            move[i] = move[i]-center[i]
            i+=1
        return(move)

    # The pyramid class
class Cube:

    # This part is really just what used to be at the top with all the polys and such but now its in the class so it's remade whenever the class is initialized
    # It includes the individual points, a pointcloud, definitions for each polygon, and all the polygons in one object
    
    def __init__(self, b1, b2, b3, b4, b5, b6, b7, b8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.pointCloud = [b1, b2, b3, b4, b5, b6, b7, b8]
        self.center = self.findCenter()
        self.frontpoly1 = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[5]]
        self.frontpoly2 = [self.pointCloud[5],self.pointCloud[4],self.pointCloud[0]]
        self.rightpoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[6]]
        self.rightpoly2 = [self.pointCloud[6],self.pointCloud[5],self.pointCloud[1]]
        self.backpoly1 = [self.pointCloud[2],self.pointCloud[3],self.pointCloud[7]]
        self.backpoly2 = [self.pointCloud[7],self.pointCloud[6],self.pointCloud[2]]
        self.leftpoly1 = [self.pointCloud[3],self.pointCloud[0],self.pointCloud[4]]
        self.leftpoly2 = [self.pointCloud[4],self.pointCloud[7],self.pointCloud[3]]
        self.bottompoly1 = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[2]]
        self.bottompoly2 = [self.pointCloud[2],self.pointCloud[3],self.pointCloud[0]]
        self.toppoly1 = [self.pointCloud[6],self.pointCloud[7],self.pointCloud[4]]
        self.toppoly2 = [self.pointCloud[4],self.pointCloud[5],self.pointCloud[6]]
        self.object = [ self.frontpoly1,self.frontpoly2,self.rightpoly1,self.rightpoly2,self.backpoly1,self.backpoly2,self.leftpoly1,self.leftpoly2,self.bottompoly1,self.bottompoly2,self.toppoly1,self.toppoly2]

    # This function updates the polygons using the point cloud and then the entire pyramid
    def update(self):
        self.frontpoly1 = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[5]]
        self.frontpoly2 = [self.pointCloud[5],self.pointCloud[4],self.pointCloud[0]]
        self.rightpoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[6]]
        self.rightpoly2 = [self.pointCloud[6],self.pointCloud[5],self.pointCloud[1]]
        self.backpoly1 = [self.pointCloud[2],self.pointCloud[3],self.pointCloud[7]]
        self.backpoly2 = [self.pointCloud[7],self.pointCloud[6],self.pointCloud[2]]
        self.leftpoly1 = [self.pointCloud[3],self.pointCloud[0],self.pointCloud[4]]
        self.leftpoly2 = [self.pointCloud[4],self.pointCloud[7],self.pointCloud[3]]
        self.bottompoly1 = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[2]]
        self.bottompoly2 = [self.pointCloud[2],self.pointCloud[3],self.pointCloud[0]]
        self.toppoly1 = [self.pointCloud[6],self.pointCloud[7],self.pointCloud[4]]
        self.toppoly2 = [self.pointCloud[4],self.pointCloud[5],self.pointCloud[6]]
        self.object = [ self.frontpoly1,self.frontpoly2,self.rightpoly1,self.rightpoly2,self.backpoly1,self.backpoly2,self.leftpoly1,self.leftpoly2,self.bottompoly1,self.bottompoly2,self.toppoly1,self.toppoly2]

    # This function resets the pyramid with the originally passed in points
    def reset(self):
        self.pointCloud = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8]
        self.update()

    # This function will find the center of the pyramid by find the average of each point and creating a new set of coordinates
    def findCenter(self):
        xCoord = self.pointCloud[0][0] + self.pointCloud[1][0] + self.pointCloud[2][0] + self.pointCloud[3][0] + self.pointCloud[4][0] + self.pointCloud[5][0] + self.pointCloud[6][0] + self.pointCloud[7][0]
        xCoord = xCoord/8
        zCoord = self.pointCloud[0][2] + self.pointCloud[1][2] + self.pointCloud[2][2] + self.pointCloud[3][2] + self.pointCloud[4][2] + self.pointCloud[5][2] + self.pointCloud[6][2] + self.pointCloud[7][2]
        zCoord = zCoord/8
        yCoord = self.pointCloud[0][1] + self.pointCloud[1][1] + self.pointCloud[2][1] + self.pointCloud[3][1] + self.pointCloud[4][1] + self.pointCloud[5][1] + self.pointCloud[6][1] + self.pointCloud[7][1]
        yCoord = yCoord/8
        center = [xCoord, yCoord, zCoord]
        return center

    # This function will calculate the change in coordinates needed to move the center of the object to the origin
    def moveToOrigin(self, center):
        move = [0,0,0]
        i=0
        while (i<3):
            move[i] = move[i]-center[i]
            i+=1
        return(move)

# Declaring the 3 objects based on the established coordinates at the beginning
obj1 = Pyramid(apex1, base1, base2, base3, base4)
obj2 = Cube(base5, base6, base7, base8, base9, base10, base11, base12)
obj3 = Pyramid(apex2, base13, base14, base15, base16)

# A list of the objects and a variable to keep track of which object is selected
objList = [obj3, obj2, obj1]
selected = objList[0]
n = 0

'''# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud'''
def resetPyramid(object):
    # Calls the build in reset function in the object
    print("resetPyramid executed.")
    object.reset()

'''# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.'''
def translate(object, displacement):
    print("translate executed.")
    # Iterates through the point cloud of the object and adjusts each point by the given amount
    # each adjusted point is put in a new object
    newObj = []
    for poly in object.pointCloud:
        newPoint = []
        i = 0
        while (i < 3):
            newPoint.append(poly[i] + displacement[i])
            i += 1
        newObj.append(newPoint)
    # sets the point cloud equal to the new object
    # then calls the update function
    object.pointCloud = newObj
    object.update()
    
'''# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.'''
def scale(object,scalefactor):
    print("scale executed.")

    # The center is found with the findCenter() function in the class and the coordinates to move are found with the moveToOrigin() function
    center = object.findCenter()
    move = object.moveToOrigin(center)
    # Translate is called to move the object to the origin so it can be scaled
    translate(object,move)

    # Iterates through the point cloud of the object and adjusts each point by the given amount
    # each adjusted point is put in a new object
    newObj = []
    for poly in object.pointCloud:
        newPoint = []
        i = 0
        while (i < 3):
            newPoint.append(poly[i] * scalefactor)
            i += 1
        newObj.append(newPoint)
    # sets the point cloud equal to the new object
    # then calls the update function
    object.pointCloud = newObj
    object.update()

    # The object is moved back to it's original point
    translate(object, center)
    

'''# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]'''
def rotateZ(object,degrees):
    print("rotateZ executed.")
    newObj = []
    # Cos and sin are set up here just to clarify for myself and reassure that it's all working
    # This could've been done in-line below I just wanted to make sure it was set
    cos = math.cos(math.radians(degrees))
    sin = math.sin(math.radians(degrees))

    # The center is found with the findCenter() function in the class and the coordinates to move are found with the moveToOrigin() function
    center = object.findCenter()
    move = object.moveToOrigin(center)
    # Translate is called to move the object to the origin so it can be scaled
    translate(object,move)

    # Goes through the object and does the Z-rotation calculation on each point
    for poly in object.pointCloud:
        newPoint = []
        xCoord = ((poly[0] * cos) - (poly[1] * sin))
        yCoord = ((poly[0] * sin) + (poly[1] * cos))
        zCoord = poly[2]
        newPoint.append(xCoord)
        newPoint.append(yCoord)
        newPoint.append(zCoord)
        newObj.append(newPoint)
    # sets the point cloud equal to the new object
    # then calls the update function
    object.pointCloud = newObj
    object.update()

    # The object is moved back to it's original point
    translate(object,center)
    
'''# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.'''
def rotateY(object,degrees):
    print("rotateY executed.")
    newObj = []
    # Cos and sin are set up here just to clarify for myself and reassure that it's all working
    # This could've been done in-line below I just wanted to make sure it was set
    cos = math.cos(math.radians(degrees))
    sin = math.sin(math.radians(degrees))

    # The center is found with the findCenter() function in the class and the coordinates to move are found with the moveToOrigin() function
    center = object.findCenter()
    move = object.moveToOrigin(center)
    # Translate is called to move the object to the origin so it can be scaled
    translate(object,move)

    # Goes through the object and does the Y-rotation calculation on each point
    for poly in object.pointCloud:
        newPoint = []
        xCoord = ((poly[0] * cos) + (poly[2] * sin))
        yCoord = poly[1]
        zCoord = ((poly[2] * cos) - (poly[0] * sin))
        newPoint.append(xCoord)
        newPoint.append(yCoord)
        newPoint.append(zCoord)
        newObj.append(newPoint)

    # sets the point cloud equal to the new object
    # then calls the update function
    object.pointCloud = newObj
    object.update()

    # The object is moved back to it's original point
    translate(object,center)

'''# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.'''
def rotateX(object,degrees):
    print("rotateX executed.")
    newObj = []
    # Cos and sin are set up here just to clarify for myself and reassure that it's all working
    # This could've been done in-line below I just wanted to make sure it was set
    cos = math.cos(math.radians(degrees))
    sin = math.sin(math.radians(degrees))
    
    # The center is found with the findCenter() function in the class and the coordinates to move are found with the moveToOrigin() function
    center = object.findCenter()
    move = object.moveToOrigin(center)
    # Translate is called to move the object to the origin so it can be scaled
    translate(object,move)

    # Goes through the object and does the X-rotation calculation on each point
    for poly in object.pointCloud:
        newPoint = []
        xCoord = poly[0]
        yCoord = ((poly[1] * cos) - (poly[2] * sin))
        zCoord = ((poly[1] * sin) + (poly[2] * cos))
        newPoint.append(xCoord)
        newPoint.append(yCoord)
        newPoint.append(zCoord)
        newObj.append(newPoint)

    # sets the point cloud equal to the new object
    # then calls the update function
    object.pointCloud = newObj
    object.update()

    # The object is moved back to it's original point
    translate(object,center)

'''# The function will draw an object by repeatedly callying drawPoly on each polygon in the object'''
def drawObject(object):
    print("drawObject executed.")
    # First the passed in object is compared to the selected object to see if they are the same (if it's the selected object)
    # If it is drawPoly is called for each polygon in the object and True is passed in
    # Otherwise False is passed in
    if selected == object:
        for poly in object.object:
            drawPoly(poly, True)
    else:
        for poly in object.object:
            drawPoly(poly, False)

'''# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.'''
def drawPoly(poly, isSelected):
    polyPoints = []
    i = 0

    # Goes through the points of the polygon and translates them to display coordinates by first sending them to the project function (to calculate their new X and Y
    # values) then sending them to the conversion function to place them on the TKinter canvas correctly
    # The new points are stored in polyPoints
    for point in poly:
        newPoint = convertToDisplayCoordinates(project(point))
        polyPoints.append(newPoint)

    # Goes through the new set of points and calls drawLine based on pairs of points
    while i < (len(polyPoints)-1):     
        # isSelected is used from drawObject so the correct draw function can be called here
        if (isSelected):
            drawSelected(polyPoints[i], polyPoints[i+1])
            i += 1
        else:
            drawLine(polyPoints[i], polyPoints[i+1])
            i += 1
    # Connects the last point to the first based on if its selected or not
    if isSelected:
        drawSelected(polyPoints[i], polyPoints[0])
    else:
        drawLine(polyPoints[i], polyPoints[0])

''' Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method'''
def drawLine(start,end):
    # Draws the line using create_line
    w.create_line(start[0], start[1], end[0], end[1])

def drawSelected(start,end):
    # Draws the line using create_line. Colors the object's lines red and makes the lines a little bolder
    w.create_line(start[0], start[1], end[0], end[1], width = 3, fill = 'red')

'''# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering'''
def project(point):
    ps = []
    # Uses the projection calculation for the x and y coordinates using the given formula and value for d
    # The new X and Y coordinates are added to ps and sent back to whatever called it
    xCoord = d * (point[0]/(d + point[2]))
    ps.append(xCoord)
    yCoord = d * (point[1]/(d + point[2]))
    ps.append(yCoord)
    return ps

'''# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.'''
def convertToDisplayCoordinates(point):
    displayXY = []
    # The given canvas is 400 by 400
    # An X coordinate found using the projection function can be relatively placed by adding 200 to it
    xCoord = point[0] + 250
    # The y coordinate is subtracted from 200
    yCoord = 250 - point[1]
    # The new X and Y coordinates are appended to the displayXY array and returned
    displayXY.append(xCoord)
    displayXY.append(yCoord)
    return displayXY
    

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid(selected)
    for i in objList:
        drawObject(i)

def larger():
    w.delete(ALL)
    scale(selected,1.1)
    for i in objList:
        drawObject(i)

def smaller():
    w.delete(ALL)
    scale(selected,.9)
    for i in objList:
        drawObject(i)

def forward():
    w.delete(ALL)
    translate(selected,[0,0,25])
    for i in objList:
        drawObject(i)

def backward():
    w.delete(ALL)
    translate(selected,[0,0,-25])
    for i in objList:
        drawObject(i)

def left():
    w.delete(ALL)
    translate(selected,[-25,0,0])
    for i in objList:
        drawObject(i)

def right():
    w.delete(ALL)
    translate(selected,[25,0,0])
    for i in objList:
        drawObject(i)

def up():
    w.delete(ALL)
    translate(selected,[0,25,0])
    for i in objList:
        drawObject(i)

def down():
    w.delete(ALL)
    translate(selected,[0,-25,0])
    for i in objList:
        drawObject(i)

def xPlus():
    w.delete(ALL)
    rotateX(selected,5)
    for i in objList:
        drawObject(i)
def xMinus():
    w.delete(ALL)
    rotateX(selected,-5)
    for i in objList:
        drawObject(i)

def yPlus():
    w.delete(ALL)
    rotateY(selected,5)
    for i in objList:
        drawObject(i)

def yMinus():
    w.delete(ALL)
    rotateY(selected,-5)
    for i in objList:
        drawObject(i)

def zPlus():
    w.delete(ALL)
    rotateZ(selected,5)
    for i in objList:
        drawObject(i)

def zMinus():
    w.delete(ALL)
    rotateZ(selected,-5)
    for i in objList:
        drawObject(i)

def prevB():
    w.delete(ALL)
    global n, selected
    if n == 0:
        n = 2
    else:
        n -= 1
    selected = objList[n]
    selected.findCenter()
    for i in objList:
        drawObject(i)

def nextB():
    w.delete(ALL)
    global n, selected
    if n == 2:
        n = 0
    else:
        n += 1
    selected = objList[n]
    selected.findCenter()
    for i in objList:
        drawObject(i)
    

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(obj1)
drawObject(obj2)
drawObject(obj3)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="DN", command=down)
upButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

selectioncontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
selectioncontrols.pack(side=LEFT)

selectioncontrolslabel = Label(selectioncontrols, text="Selection")
selectioncontrolslabel.pack()

prevButton = Button(selectioncontrols, text="prev", command=prevB)
prevButton.pack(side=LEFT)

nextButton = Button(selectioncontrols, text="next", command=nextB)
nextButton.pack(side=LEFT)

root.mainloop()
