import math
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
frontpoly = [apex,base1,base2]
rightpoly = [apex,base2,base3]
backpoly = [apex,base3,base4]
leftpoly = [apex,base4,base1]
bottompoly = [base4,base3,base2,base1]

# Definition of the object
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
#************************************************************************************

'''# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud'''
def resetPyramid():
    # Setting the point cloud as a global so it can be manipulated within the function and then calling the update function to set all the points to the point cloud
    print("resetPyramid executed.")
    global PyramidPointCloud
    PyramidPointCloud = [[0,50,100], [-50,-50,50], [50,-50,50], [50,-50,150], [-50,-50,150]]
    updateWithCloud()

def updateWithCloud():
    # I couldn't think of a better way to make sure all parts of this update so this is what I've got FOR NOW!!!
    global PyramidPointCloud, apex, base1, base2, base3, base4, bottompoly, frontpoly, rightpoly, backpoly, leftpoly, Pyramid
    # Update all the individual points to be the same as the point cloud
    apex = PyramidPointCloud[0]
    base1 = PyramidPointCloud[1]
    base2 = PyramidPointCloud[2]
    base3 = PyramidPointCloud[3]
    base4 = PyramidPointCloud[4]
    # Update the polygons to match the new points
    frontpoly = [apex,base1,base2]
    rightpoly = [apex,base2,base3]
    backpoly = [apex,base3,base4]
    leftpoly = [apex,base4,base1]
    bottompoly = [base4,base3,base2,base1]
    # Update the Pyramid with the new polygons
    Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

'''# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.'''
def translate(object, displacement):
    print("translate executed.")
    # Iterates through the passed in object (the point cloud) and adjusts each point by the given amount
    # each adjusted point is put in a new object
    newObj = []
    for poly in object:
        newPoint = []
        i = 0
        while (i < 3):
            newPoint.append(poly[i] + displacement[i])
            i += 1
        newObj.append(newPoint)
    # sets the point cloud equal to the new object
    # then calls the update function
    global PyramidPointCloud
    PyramidPointCloud = newObj
    updateWithCloud()
    
'''# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.'''
def scale(object,scalefactor):
    print("scale executed.")
    # Iterates through the passed in object (the point cloud) and adjusts each point by the given amount
    # each adjusted point is put in a new object
    newObj = []
    for poly in object:
        newPoint = []
        i = 0
        while (i < 3):
            newPoint.append(poly[i] * scalefactor)
            i += 1
        newObj.append(newPoint)
    # sets the point cloud equal to the new object
    # then calls the update function
    global PyramidPointCloud
    PyramidPointCloud = newObj
    updateWithCloud()

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

    # Goes through the object and does the Z-rotation calculation on each point
    for poly in object:
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
    global PyramidPointCloud
    PyramidPointCloud = newObj
    updateWithCloud()
    
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

    # Goes through the object and does the Y-rotation calculation on each point
    for poly in object:
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
    global PyramidPointCloud
    PyramidPointCloud = newObj
    updateWithCloud()

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

    # Goes through the object and does the X-rotation calculation on each point
    for poly in object:
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
    global PyramidPointCloud
    PyramidPointCloud = newObj
    updateWithCloud()

'''# The function will draw an object by repeatedly callying drawPoly on each polygon in the object'''
def drawObject(object):
    print("drawObject executed.")

    # Calls the drawPoly function for each polygon in the object
    for poly in object:
        drawPoly(poly)

'''# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.'''
def drawPoly(poly):
    polyPoints = []
    i = 0

    # Goes through the points of the polygon and translates them to display coordinates by first sending them to the project function (to calculate their new X and Y
    # values) then sending them to the conversion function to place them on the TKinter canvas correctly
    # The new points are stored in polyPoints
    for point in poly:
        newPoint = convertToDisplayCoordinates(project(point))
        polyPoints.append(newPoint)

    # Goes through the new set of points and calls drawLine based on pairs of points
    while (i < (len(polyPoints)-1)):
        drawLine(polyPoints[i], polyPoints[i+1])
        i += 1
    # Connects the last point to the first
    drawLine(polyPoints[i], polyPoints[0])

''' Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method'''
def drawLine(start,end):
    # Draws the line using create_line
    w.create_line(start[0], start[1], end[0], end[1])    

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
    xCoord = point[0] + 200
    # If a Y coordinate is positive, it's new position can be found by subtracting it from 200
    if (point[1] > 0):
        yCoord = 200 - point[1]
    # If the Y coord. is negative, the absolute value of the point is added to 200
    elif (point[1] < 0):
        yCoord = 200 + abs(point[1])
    # And if it's 0, the point's value is 0
    elif (point[1] == 0):
        yCoord = 200
    # The new X and Y coordinates are appended to the displayXY array and returned
    displayXY.append(xCoord)
    displayXY.append(yCoord)
    return displayXY
    

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid()
    drawObject(Pyramid)

def larger():
    w.delete(ALL)
    scale(PyramidPointCloud,1.1)
    drawObject(Pyramid)

def smaller():
    w.delete(ALL)
    scale(PyramidPointCloud,.9)
    drawObject(Pyramid)

def forward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,25])
    drawObject(Pyramid)

def backward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,-25])
    drawObject(Pyramid)

def left():
    w.delete(ALL)
    translate(PyramidPointCloud,[-25,0,0])
    drawObject(Pyramid)

def right():
    w.delete(ALL)
    translate(PyramidPointCloud,[25,0,0])
    drawObject(Pyramid)

def up():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,25,0])
    drawObject(Pyramid)

def down():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,-25,0])
    drawObject(Pyramid)

def xPlus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,5)
    drawObject(Pyramid)

def xMinus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,-5)
    drawObject(Pyramid)

def yPlus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,5)
    drawObject(Pyramid)

def yMinus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,-5)
    drawObject(Pyramid)

def zPlus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,5)
    drawObject(Pyramid)

def zMinus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,-5)
    drawObject(Pyramid)

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(Pyramid)
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

root.mainloop()
