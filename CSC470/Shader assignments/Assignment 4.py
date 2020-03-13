'''
Name: Olivia Spears
CWID: 10240548
Date Due: 2/15/2018
Assignment No. 4
---
This program will build off the previous assignments by introducing lighting and shading models
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

'''apex2 = [-100,50,50]
base13 = [-125,0,25]
base14 = [-75,0,25]
base15 = [-75,0,75]
base16 = [-125,0,75]'''

base17 = [0, 50, 50]
base18 = [33, 33, 50]
base19 = [50,0,50]
base20 = [33, -33, 50]
base21 = [0, -50, 50]
base22 = [-33, -33, 50]
base23 = [-50, 0, 50]
base24 = [-33, 33, 50]

base25 = [0, 50, 200]
base26 = [33, 33, 200]
base27 = [50, 0, 200]
base28 = [33, -33, 200]
base29 = [0, -50, 200]
base30 = [-33, -33, 200]
base31 = [-50, 0, 200]
base32 = [-33, 33, 200]

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
        self.frontpoly = [self.pointCloud[0],self.pointCloud[2],self.pointCloud[1]]
        self.rightpoly = [self.pointCloud[0],self.pointCloud[3],self.pointCloud[2]]
        self.backpoly = [self.pointCloud[0],self.pointCloud[4],self.pointCloud[3]]
        self.leftpoly = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[4]]
        self.bottompoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[3]]
        self.bottompoly2 = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1]]
        self.bottom = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1],self.pointCloud[2]]
        self.color = [1, 1, 0]
        self.objectsurfaces = [self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly, self.bottom]
        self.object = [self.frontpoly,self.rightpoly,self.backpoly,self.leftpoly,self.bottompoly1,self.bottompoly2]
        #self.object = [self.frontpoly, self.rightpoly]

    # This function updates the polygons using the point cloud and then the entire pyramid
    def update(self):
        self.frontpoly = [self.pointCloud[0],self.pointCloud[2],self.pointCloud[1]]
        self.rightpoly = [self.pointCloud[0],self.pointCloud[3],self.pointCloud[2]]
        self.backpoly = [self.pointCloud[0],self.pointCloud[4],self.pointCloud[3]]
        self.leftpoly = [self.pointCloud[0],self.pointCloud[1],self.pointCloud[4]]
        self.bottompoly1 = [self.pointCloud[1],self.pointCloud[2],self.pointCloud[3]]
        self.bottompoly2 = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1]]
        self.bottom = [self.pointCloud[3],self.pointCloud[4],self.pointCloud[1],self.pointCloud[2]]
        self.objectsurfaces = [self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly, self.bottom]
        self.object = [self.frontpoly,self.rightpoly,self.backpoly,self.leftpoly,self.bottompoly1,self.bottompoly2]
        #self.object = [self.frontpoly, self.rightpoly]

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
        while (i < 3):
            move[i] = move[i]-center[i]
            i+=1
        return(move)

    def findNormal(self, poly):  
        v1 = []
        v2 = []
        i = 0
        # Two vectors are identified here so they can be mathed on 
        while (i < 3):
            v1.append(poly[1][i]-poly[0][i])
            v2.append(poly[2][i]-poly[0][i])
            i+=1

        # The cross product of the two vectors is found and stored as the coordinates for the normal vector
        normal = []
        normal.append((v1[1]*v2[2])-(v1[2]*v2[1]))
        normal.append((v1[2]*v2[0])-(v1[0]*v2[2]))
        normal.append((v1[0]*v2[1])-(v1[1]*v2[0]))
        return(normal)          

    # The pyramid class
class Cylinder:

    # This part is really just what used to be at the top with all the polys and such but now its in the class so it's remade whenever the class is initialized
    # It includes the individual points, a pointcloud, definitions for each polygon, and all the polygons in one object
    
    def __init__(self, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16):
        self.color = [1, 1, 0]
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13
        self.b14 = b14
        self.b15 = b15
        self.b16 = b16
        self.pointCloud = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
        self.center = self.findCenter()
        # Defining the polygons
        self.toppoly1 = [self.pointCloud[0],self.pointCloud[9],self.pointCloud[1]]
        self.toppoly2 = [self.pointCloud[0],self.pointCloud[8],self.pointCloud[9]]
        
        self.rightpoly1 = [self.pointCloud[2],self.pointCloud[11],self.pointCloud[3]]
        self.rightpoly2 = [self.pointCloud[2],self.pointCloud[10],self.pointCloud[11]]
        
        self.bottompoly1 = [self.pointCloud[4],self.pointCloud[13],self.pointCloud[5]]
        self.bottompoly2 = [self.pointCloud[4],self.pointCloud[12],self.pointCloud[13]]
        
        self.leftpoly1 = [self.pointCloud[6],self.pointCloud[15],self.pointCloud[7]]
        self.leftpoly2 = [self.pointCloud[6],self.pointCloud[14],self.pointCloud[15]]
        
        self.toprightpoly1 = [self.pointCloud[1],self.pointCloud[10],self.pointCloud[2]]
        self.toprightpoly2 = [self.pointCloud[1],self.pointCloud[9],self.pointCloud[10]]
        
        self.topleftpoly1 = [self.pointCloud[7],self.pointCloud[8],self.pointCloud[0]]
        self.topleftpoly2 = [self.pointCloud[7],self.pointCloud[15],self.pointCloud[8]]

        self.bottomrightpoly1 = [self.pointCloud[3], self.pointCloud[12], self.pointCloud[4]]
        self.bottomrightpoly2 = [self.pointCloud[3], self.pointCloud[11], self.pointCloud[12]]
        
        self.bottomleftpoly1 = [self.pointCloud[5], self.pointCloud[14], self.pointCloud[6]]
        self.bottomleftpoly2 = [self.pointCloud[5], self.pointCloud[13], self.pointCloud[14]]

        self.top = [self.pointCloud[0],self.pointCloud[8],self.pointCloud[9],self.pointCloud[1]]
        self.topright = [self.pointCloud[1],self.pointCloud[9],self.pointCloud[10],self.pointCloud[2]]
        self.right = [self.pointCloud[2],self.pointCloud[10],self.pointCloud[11],self.pointCloud[3]]
        self.topleft = [self.pointCloud[7],self.pointCloud[15],self.pointCloud[8],self.pointCloud[0]]
        self.left = [self.pointCloud[6],self.pointCloud[14],self.pointCloud[15],self.pointCloud[7]]
        self.bottom = [self.pointCloud[4],self.pointCloud[12],self.pointCloud[13],self.pointCloud[5]]
        self.bottomleft = [self.pointCloud[5], self.pointCloud[13], self.pointCloud[14], self.pointCloud[6]]
        self.bottomright = [self.pointCloud[5], self.pointCloud[13], self.pointCloud[14], self.pointCloud[6]]

        self.objectsurfaces = [self.top, self.topright, self.right, self.bottomright, self.bottom, self.bottomleft, self.left, self.topleft]
        self.object = [ self.toppoly1,self.toppoly2,self.rightpoly1,self.rightpoly2,self.leftpoly1,self.leftpoly2,self.bottompoly1,self.bottompoly2,self.toprightpoly1,self.toprightpoly2,self.topleftpoly1,self.topleftpoly2, self.bottomrightpoly1, self.bottomrightpoly2, self.bottomleftpoly1, self.bottomleftpoly2]
        #self.object = [self.toppoly1]

    # This function updates the polygons using the point cloud and then the entire pyramid
    def update(self):
        self.toppoly1 = [self.pointCloud[0],self.pointCloud[9],self.pointCloud[1]]
        self.toppoly2 = [self.pointCloud[0],self.pointCloud[8],self.pointCloud[9]]
        
        self.rightpoly1 = [self.pointCloud[2],self.pointCloud[11],self.pointCloud[3]]
        self.rightpoly2 = [self.pointCloud[2],self.pointCloud[10],self.pointCloud[11]]
        
        self.bottompoly1 = [self.pointCloud[4],self.pointCloud[13],self.pointCloud[5]]
        self.bottompoly2 = [self.pointCloud[4],self.pointCloud[12],self.pointCloud[13]]
        
        self.leftpoly1 = [self.pointCloud[6],self.pointCloud[15],self.pointCloud[7]]
        self.leftpoly2 = [self.pointCloud[6],self.pointCloud[14],self.pointCloud[15]]
        
        self.toprightpoly1 = [self.pointCloud[1],self.pointCloud[10],self.pointCloud[2]]
        self.toprightpoly2 = [self.pointCloud[1],self.pointCloud[9],self.pointCloud[10]]
        
        self.topleftpoly1 = [self.pointCloud[7],self.pointCloud[8],self.pointCloud[0]]
        self.topleftpoly2 = [self.pointCloud[7],self.pointCloud[15],self.pointCloud[8]]

        self.bottomrightpoly1 = [self.pointCloud[3], self.pointCloud[12], self.pointCloud[4]]
        self.bottomrightpoly2 = [self.pointCloud[3], self.pointCloud[11], self.pointCloud[12]]

        
        self.bottomleftpoly1 = [self.pointCloud[5], self.pointCloud[14], self.pointCloud[6]]
        self.bottomleftpoly2 = [self.pointCloud[5], self.pointCloud[13], self.pointCloud[14]]

        self.objectsurfaces = [self.top, self.topright, self.right, self.bottomright, self.bottom, self.bottomleft, self.left, self.topleft]
        self.object = [ self.toppoly1,self.toppoly2,self.rightpoly1,self.rightpoly2,self.leftpoly1,self.leftpoly2,self.bottompoly1,self.bottompoly2,self.toprightpoly1,self.toprightpoly2,self.topleftpoly1,self.topleftpoly2, self.bottomrightpoly1, self.bottomrightpoly2, self.bottomleftpoly1, self.bottomleftpoly2]
        #self.object = [self.toppoly1]

    # This function resets the pyramid with the originally passed in points
    def reset(self):
        self.pointCloud = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10, self.b11, self.b12, self.b13, self.b14, self.b15, self.b16]
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
obj2 = Cylinder(base17, base18, base19, base20, base21, base22, base23, base24, base25, base26, base27, base28, base29, base30, base31, base32)
#obj3 = Pyramid(apex2, base13, base14, base15, base16)

# A list of the objects and a variable to keep track of which object is selected
#objList = [obj3, obj2, obj1]
objList = [obj2, obj1]
selected = objList[0]
n = 0
zb = [[0 for i in range(500)] for j in range(500)]

# Booleans for the toggles to determine what sort of operations are being performed
edgeDraw = True
cullingOFF = True
polyFill = False
#zBuff = False
diffuse = False
specular = False
faceted = True
gouraud = False

'''# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud'''
def resetPyramid(object):
    # Calls the build in reset function in the object
    object.reset()

'''# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.'''
def translate(object, displacement):
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
def scale(object, scalefactor):

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
def rotateZ(object, degrees):
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
def rotateY(object, degrees):
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
def rotateX(object, degrees):
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
##############################################################################################DRAW OBJECT FUNCTIONS#######################################################################################
'''# The function will draw an object by repeatedly callying drawPoly on each polygon in the object'''
def drawObject(object):
    # First the passed in object is compared to the selected object to see if they are the same (if it's the selected object)
    # If it is drawPoly is called for each polygon in the object and True is passed in
    # Otherwise False is passed in
    if selected == object:
        for poly in object.object:
            drawPoly(poly, True, object)
    else:
        for poly in object.object:
            drawPoly(poly, False, object)

'''# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.'''
def drawPoly(poly, isSelected, object):
    polyPoints = []
    checkPoly = []
    i = 0
    # Goes through the points of the polygon and translates them to display coordinates by first sending them to the project function (to calculate their new X and Y
    # values) then sending them to the conversion function to place them on the TKinter canvas correctly
    # The new points are stored in polyPoints
    for point in poly:
        newPoint = project(point)
        checkPoly.append(newPoint)
        newPoint = convertToDisplayCoordinates(newPoint)
        polyPoints.append(newPoint)
    
    # Goes through the new set of points and calls drawLine based on pairs of points
    if (shouldDraw(checkPoly) or cullingOFF):
        if (polyFill):
            fillPoly(polyPoints, object)
        if (edgeDraw):
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

##############################################################################################PROJECTION MATH#######################################################################################
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
    zCoord = point[2]/(d+point[2])
    ps.append(zCoord)
    return ps

'''# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.'''
def convertToDisplayCoordinates(point):
    displayXY = []
    # The given canvas is 500 by 500
    # An X coordinate found using the projection function can be relatively placed by adding 250 to it
    xCoord = point[0] + 250
    # The y coordinate is subtracted from 250
    yCoord = 250 - point[1]
    # The new X and Y coordinates are appended to the displayXY array and returned
    displayXY.append(xCoord)
    displayXY.append(yCoord)
    displayXY.append(point[2])
    return displayXY

##############################################################################################BACKFACE CULLING MATHS#############################################################################################
# This function determines whether or not a polygon should be culled during backface culling
def shouldDraw(poly):
    i=0
    # This calls the function to find the normal and sets a relative point to a point on the polygon so the offset, D, can be found
    normal = findNormal(poly)
    point = poly[0]
    D = ((point[0]*normal[0])-(point[1]*normal[1])+(point[2]*normal[2]))

    # point is reset to be the focal point [0,0,-d] and the direction is found with the dot product of the normal and the focal point
    point = [0,0,-d]
    direction = ((point[0]*normal[0])-(point[1]*normal[1])+(point[2]*normal[2])) - D
    # If the direction is negative it will not draw the polygon, and if it is positive it will draw the polygon
    if (direction < 0):
        return False
    else:
        return True
####################################################################################EDGE TABLE MATHS#################################################################################################################
# Sets the edge table
def edgeTable(poly, object):
    table = []
    k = 0
    # Declares all the edges
    edge1 = [poly[0],poly[1]]
    edge2 = [poly[1],poly[2]]
    edge3 = [poly[2],poly[0]]
    edges = [edge1, edge2, edge3]
    # Goes through the edges and then populates the table with the properties found
    for n in edges:
        # Checks to see if the line is horizontal or not
        if (math.floor((n[0][1])-(n[1][1])) != 0):
            prop = findEdgeProps(n, object)
            table.insert(k, prop)
            k +=1
    # If there is a table, SORT IT!!!!!!!
    if (table):
        table = sorted(table, key=lambda edge: (-edge[0], edge[3]))
        return(table)
    else:
        return(None)

# Goes through the given edge to find all the properties needed for the edge table
def findEdgeProps(edge, object):
    # y_max
    # Compares the 2 y's and sets the larger as the y_max
    if (edge[0][1] > edge[1][1]):
        y_max = edge[0][1]
    else:
        y_max = edge[1][1]

    # y_min
    # whichever y wasn't the y_max is the y_min
    if (y_max == edge[0][1]):
        y_min = edge[1][1]
    else:
        y_min = edge[0][1]

    # dx
    # Calculates the run over rise
    dx = (edge[0][0]-edge[1][0])/(edge[0][1]-edge[1][1])

    # x_initial
    # sets x_initial to the x at the y_max and then moves it by a slope
    if (y_max == edge[0][1]):
        x_initial = edge[0][0] - dx
    else:
        x_initial = edge[1][0] - dx

    if (faceted):
        dI = 0
        Imax = 0
    else:
        # Intensity normals of the first two edges points
        rgb0 = findVertexNormals(edge[0], object)
        rgb1 = findVertexNormals(edge[1], object)

        rgb0 = lighting(rgb0, object.color)
        rgb1 = lighting(rgb1, object.color)

        R = (rgb0[0] - rgb1[0])/(edge[0][1]-edge[1][1])
        G = (rgb0[1] - rgb1[1])/(edge[0][1]-edge[1][1])
        B = (rgb0[2] - rgb1[2])/(edge[0][1]-edge[1][1])

        dI = [R, G, B]
        if (y_max == edge[0][1]):
            Imax = rgb0
        else:
            Imax = rgb1
        
    #properties = (y_max, y_min, dx, x_initial)
    properties = (y_max, y_min, dx, x_initial, dI, Imax)
    return(properties)

####################################################################################POLYGON FILLING#################################################################################################################

def fillPoly(poly, object):
    # create edge table based on edges that will be used
    # an edge won't be used if it's horizontal
    # z buffering does NOT work so I'm just gonna comment that OUT
    table = edgeTable(poly, object)
    if (table != None):
        #color = lighting(poly)
        if (faceted):
            normal = findNormal(poly)
            colorName = '#%02x%02x%02x' % lighting(normal, object.color)
        # For a triangle without a horizontal line the table's length will be 3
        if(len(table) == 3):
            if (gouraud):                    
                # This is the starting color for gouraud shading
                colorStart = list(table[0][5])
                colorEnd = list(table[1][5])
                
                # This is the change in intensity for each color
                diL = table[0][4]
                diR = table[1][4]
                
            # This is the slope of the left and right sides of the polygon
            dxL = table[0][2]
            dxR = table[1][2]

            # This is the starting and ending x for the first scanline 
            xStart = table[0][3]
            xEnd = table[1][3]

            # The starting and stopping point of the first half of the triangle
            yStart = math.floor(table[0][0])
            yEnd = math.floor(table[2][0])

            # Iterates from top to bottom of the first half of the triangle
            y = yStart
            if (gouraud):
                color = colorStart
            while (y > yEnd):
                x = xStart
                if (gouraud):
                    diX = finddix(colorStart, colorEnd, xStart, xEnd)
                    color[0] = round(color[0] + diX[0])
                    color[1] = round(color[1] + diX[1])
                    color[2] = round(color[2] + diX[2])
                    colorName = '#%02x%02x%02x' % tuple(color)
                # Iterates left to right for the scanline
                while (x < xEnd):
                    # sets the color and creates a rectangle (pixel) in that color then moves to the next point
                    #color = '#%02x%02x%02x' % lighting(poly)
                    w.create_rectangle(x,y,x-1,y-1,outline=(colorName))

                    x += 1          
                if (gouraud):
                    colorStart[0] = math.floor(colorStart[0] + diL[0])
                    colorStart[1] = math.floor(colorStart[1] + diL[1])
                    colorStart[2] = math.floor(colorStart[2] + diL[2])
                    colorEnd[0] = math.floor(colorEnd[0] + diR[0])
                    colorEnd[1] = math.floor(colorEnd[1] + diR[1])
                    colorEnd[2] = math.floor(colorEnd[2] + diR[2])
                # Moves the starting X, ending X, and y down along the triangle's slope
                xStart -= dxL
                xEnd -= dxR
                y -= 1

            # Determines which edge is to the left and which edge is to the right
            if (math.floor(table[0][1]) == yEnd):
                dxL = table[2][2]
                xStart = table[2][3] - dxL
                if (gouraud):
                    colorStart = list(table[2][5])
            elif (math.floor(table[0][1]) < yEnd):
                dxR = table[2][2]
                xEnd = table[2][3] - dxR
                if (gouraud):
                    colorEnd = list(table[2][5])
            # This repeats everything from above but for the bottom half of the triangle
            
            yStart = yEnd
            yEnd = math.floor(table[2][1])

            y = yStart
            if (gouraud):
                color = colorStart
            while (y > yEnd):
                x = xStart
                if (gouraud):
                    diX = finddix(colorStart, colorEnd, xStart, xEnd)
                    color[0] = round(color[0] + diX[0])
                    color[1] = round(color[1] + diX[1])
                    color[2] = round(color[2] + diX[2])
                    colorName = '#%02x%02x%02x' % tuple(color)
                while (x < xEnd):
                    #color = '#%02x%02x%02x' % lighting(poly)
                    w.create_rectangle(x,y,x-1,y-1,outline=(colorName))

                    x += 1          
                if (gouraud):
                    colorStart[0] = math.floor(colorStart[0] + diL[0])
                    colorStart[1] = math.floor(colorStart[1] + diL[1])
                    colorStart[2] = math.floor(colorStart[2] + diL[2])
                    colorEnd[0] = math.floor(colorEnd[0] + diR[0])
                    colorEnd[1] = math.floor(colorEnd[1] + diR[1])
                    colorEnd[2] = math.floor(colorEnd[2] + diR[2])
                xStart -= dxL
                xEnd -= dxR
                y -= 1

        # This handles if the triangle has a flat bottom and therefore only 2 edges that need to be drawn
        elif(len(table) ==  2):
            if (table[0][3] < table[1][3]):
                left = 0
                right = 1
            else:
                left = 1
                right = 0
                
            if (gouraud):
                # This is the change in intensity for each color
                diL = table[left][4]
                diR = table[right][4]
                    
                # This is the starting color for gouraud shading
                colorStart = list(table[0][5])
                colorEnd = list(table[0][5])
                
            dxL = table[left][2]
            dxR = table[right][2]

            xStart = table[left][3]
            xEnd = table[right][3]
            
            yStart = math.floor(table[0][0])
            yEnd = math.floor(table[1][1])

            y = yStart
            if (gouraud):
                color = colorStart
            
            while (y > yEnd):
                x = xStart
                if (gouraud):
                    diX = finddix(colorStart, colorEnd, xStart, xEnd)
                    color[0] = round(color[0] + diX[0])
                    color[1] = round(color[1] + diX[1])
                    color[2] = round(color[2] + diX[2])
                    colorName = '#%02x%02x%02x' % tuple(color)
                # Iterates left to right for the scanline
                while (x < xEnd):
                    # sets the color and creates a rectangle (pixel) in that color then moves to the next point
                    #color = '#%02x%02x%02x' % lighting(poly)
                    w.create_rectangle(x,y,x-1,y-1,outline=(colorName))

                    x += 1
                # Moves the starting X, ending X, and y down along the triangle's slope           
                if (gouraud):
                    colorStart[0] = math.floor(colorStart[0] + diL[0])
                    colorStart[1] = math.floor(colorStart[1] + diL[1])
                    colorStart[2] = math.floor(colorStart[2] + diL[2])
                    colorEnd[0] = math.floor(colorEnd[0] + diR[0])
                    colorEnd[1] = math.floor(colorEnd[1] + diR[1])
                    colorEnd[2] = math.floor(colorEnd[2] + diR[2])
                xStart -= dxL
                xEnd -= dxR
                y -= 1
####################################################################################VECTOR/VERTEX MATH#################################################################################################################
def normalize(vector):
    i = 0
    b = [0,0,0]
    j = (vector[0]*vector[0]) + (vector[1]*vector[1]) + (vector[2]*vector[2])
    j = j**.5
    while (i < 3):
        b[i] = vector[i]/j
        i+=1
    return b

# This function is used to find the normal vector of a polygon so that the direction it's facing can be determined
def findNormal(poly):
    v1 = []
    v2 = []
    i = 0
    # Two vectors are identified here so they can be mathed on 
    while (i < 3):
        v1.append(poly[1][i]-poly[0][i])
        v2.append(poly[2][i]-poly[0][i])
        i+=1

    # The cross product of the two vectors is found and stored as the coordinates for the normal vector
    normal = []
    normal.append((v1[1]*v2[2])-(v1[2]*v2[1]))
    normal.append((v1[2]*v2[0])-(v1[0]*v2[2]))
    normal.append((v1[0]*v2[1])-(v1[1]*v2[0]))
    return(normal)

# Calculates and returns normal of a given vertex
def findVertexNormals(vertex, object):
    sumX = 0
    sumY = 0
    sumZ = 0
    projectedSurfaces = []
    for j in object.objectsurfaces:
        newSurface = []
        for point in j:
            newpoint = convertToDisplayCoordinates(project(point))
            newSurface.append(newpoint)
        projectedSurfaces.append(newSurface)
                
    n = 0
    while n < len(projectedSurfaces):
        m = 0
        while m < len(projectedSurfaces[n]):
            if projectedSurfaces[n][m] == vertex:
                normal = findNormal(projectedSurfaces[n])
                sumX = sumX + normal[0]
                sumY = sumY + normal[1]
                sumZ = sumZ + normal[2]
            m += 1                
        n += 1
    '''mag = (sumX**2 + sumY**2 + sumZ**2)
        print("uhh")
        print(mag)
        mag = mag**0.5
        print(mag)
        print("ohh")
        normX = sumX/mag
        normY = sumY/mag
        normZ = sumY/mag'''
    normalVertex = [sumX, sumY, sumZ]
    #normalVertex = normalize(normalVertex)
    return normalVertex

# Calculates and returns change in x direction of intensity
def finddix(ia, ib, xStart, xEnd):
    R = (ib[0] - ia[0])/(xEnd - xStart)
    G = (ib[1] - ia[1])/(xEnd - xStart)
    B = (ib[2] - ia[2])/(xEnd - xStart)

    diX = [R, G, B]
    return diX

            
########################################################################################################LIGHTING#################################################################################################################

def lighting(N, color):
    #print("in here")
    # Declaring the intensities and constants. Because ambient light is always on, it always runs the first bit :)
    ka = [1, 1, 1]
    ia = [0.4, 0.4, 0.4]
    # Maths the color for R, G, and B
    ambient = [ia[0]*ka[0], ia[1]*ka[1], ia[2]*ka[2]]
    R = ambient[0]
    G = ambient[1]
    B = ambient[2]
    # Finds the values for diffuse lighting using the Normal passed in
    if (diffuse):
        ip = [0.5, 0.5, 0.5]
        L = [1, 1, -1]
        L = normalize(L)
        #N = normalize(N)
        dot = -1*((N[0]*L[0]) + (N[1]*L[1]) + (N[2]*L[2]))
        if (dot < 0):
            dot = 0
        diff = [ip[0] * ka[0] * dot, ip[1] * ka[1] * dot, ip[2] * ka[2] * dot]
        R = ambient[0] + diff[0]
        G = ambient[1] + diff[1]
        B = ambient[2] + diff[2]

        # Finds values for specular lighting
        if (specular):
            r = [0,0,0]
            v = [0, 0, -d]
            ks = [0.2, 0.2, 0.2]
            dot = -1*((N[0]*L[0]) + (N[1]*L[1]) + (N[2]*L[2]))
            twocos = 2 * dot
            if (twocos > 0):
                r[0] = N[0] - (L[0]/twocos)
                r[1] = N[1] - (L[1]/twocos)
                r[2] = N[2] - (L[2]/twocos)
            elif (twocos == 0):
                r[0] = -L[0]
                r[1] = -L[1]
                r[2] = -L[2]
            elif (twocos < 0):
                r[0] = -N[0] + (L[0]/twocos)
                r[1] = -N[1] + (L[1]/twocos)
                r[2] = -N[2] + (L[2]/twocos)
            
            dot = -1*((r[0]*L[0]) + (r[1]*L[1]) + (r[2]*L[2]))
            if (dot < 0):
                dot = 0

            spec = [ip[0] * ks[0] * dot, ip[1] * ks[1] * dot, ip[2] * ks[2] * dot]
            R = ambient[0] + diff[0] + spec[0]
            G = ambient[1] + diff[1] + spec[1]
            B = ambient[2] + diff[2] + spec[2]

    # The values are applied to the 255 color scale and then capped between 0 and 255
    R = round((R/1000)*255) * color[0]
    G = round((G/1000)*255) * color[1]
    B = round((B/1000)*255) * color[2]
    if R > 255:
        R = 255
    if R < 0:
        R = 0
        
    if G > 255:
        G = 255
    if G < 0:
        G = 0
        
    if B > 255:
        B = 255
    if B < 0:
        B = 0
    litColor = (R, G, B)
    return (litColor)
    
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
        n = 1
    else:
        n -= 1
    selected = objList[n]
    selected.findCenter()
    for i in objList:
        drawObject(i)

def nextB():
    w.delete(ALL)
    global n, selected
    if n == 1:
        n = 0
    else:
        n += 1
    selected = objList[n]
    selected.findCenter()
    for i in objList:
        drawObject(i)

# Toggles between no culling and culling
def bfaceCulling():
    w.delete(ALL)
    global cullingOFF
    if cullingOFF:
        cullingOFF = False
    else:
        cullingOFF = True
    for i in objList:
        drawObject(i)

# Toggles between 3 fill options
def fillToggle():
    w.delete(ALL)
    global edgeDraw, polyFill
    if (polyFill == False):
        polyFill = True
    elif(polyFill and edgeDraw):
        edgeDraw = False
    elif(polyFill and edgeDraw == False):
        polyFill = False
        edgeDraw = True
    for i in objList:
        drawObject(i)

# When z buffer works, uncomment this :(
'''def zBuf():
    w.delete(ALL)
    global zBuff
    if zBuff:
        zBuff = False
    else:
        zBuff = True
    for i in objList:
        drawObject(i)'''

def lightToggle():
    w.delete(ALL)
    global diffuse, specular
    if (not diffuse):
        diffuse = True
    elif (diffuse and not specular):
        specular = True
    elif (diffuse and specular):
        diffuse = False
        specular = False
    for i in objList:
        drawObject(i)

def shadeToggle():
    w.delete(ALL)
    global faceted, gouraud
    if (faceted):
        faceted = False
        gouraud = True
    elif (gouraud):
        gouraud = False
        faceted = True
    for i in objList:
        drawObject(i)    

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(obj1)
drawObject(obj2)
#drawObject(obj3)
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

visualcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
visualcontrols.pack(side=LEFT)

visualcontrolslabel = Label(visualcontrols, text="Options")
visualcontrolslabel.pack()

cullingtoggle = Checkbutton(visualcontrols, text="Culling", command=bfaceCulling)
cullingtoggle.pack(side=LEFT)

fillButton = Button(visualcontrols, text="Filling", command=fillToggle)
fillButton.pack(side=LEFT)

# When z buffer works, uncomment this :(
'''ztoggle = Checkbutton(visualcontrols, text="Z Buffer", command=zBuf)
ztoggle.pack(side=LEFT)'''

lightButton = Button(visualcontrols, text="Lighting", command=lightToggle)
lightButton.pack(side=LEFT)

shadingButton = Button(visualcontrols, text="Shading", command=shadeToggle)
shadingButton.pack(side=LEFT)

root.mainloop()
