'''
Olivia Spears
CSC 470
Assignment 5
Due: 2/26/2018

The goal of this assignment is to implement recursive ray tracing based on a given outline and our previously implemented lighting model.
Two balls of different colors and sizes are reflective and floating above a red and white checkerboard which is less reflective.
'''

import math
from tkinter import *

CanvasWidth = 600
CanvasHeight = 600
d = 800

def render_proc():
    # depth of ray tracing
    depth = 5

    # Center of projection
    cop = [0, 0, -d]

    # SCREEN SCANNER :^)
    pixel_x = 1
    while (pixel_x < 600):
        screen_x = pixel_x - 300
        pixel_y = 1
        while (pixel_y < 600):
            screen_y = 300 - pixel_y

            ray = [screen_x - cop[0], screen_y - cop[1], 0 - cop[2]]

            RGB = trace_ray(depth, cop, ray)

            put_pixel(pixel_x, pixel_y, RGB)
            
            pixel_y += 1
        pixel_x += 1
        w.update()

def put_pixel(x, y, RGB):
    i = 0
    # Goes through the list of colors and turns it into integers
    while (i < 3):
        RGB[i] = round(RGB[i])
        # Then sets the color maximum
        if (RGB[i] > 255):
            RGB[i] = 255
        # And the color minimum
        elif (RGB[i] < 0):
            RGB[i] = 0
        i += 1
    # Puts the color in a tuple so it can be READ
    color = (RGB[0], RGB[1], RGB[2])
    color = '#%02x%02x%02x' % color
    # Creates the pixel :^)
    w.create_rectangle(x, y, x + 1, y + 1, outline = color)

def trace_ray(level, cop, ray):
    if(level == 0):
    # Max depth. Return black
        rgb = [0, 0, 0]
    else:
        # Check intersection of ray w/ objects and set rgb values

        # Distance of closest object initially v large
        t = 100000

        # Initially no object has been intersected
        obj_cd = -1
        # Checks for checkerboard
        board_intersect = checkerboard_intersection(cop, ray, t)
        if (board_intersect[0]):
            obj_cd = 0
            intersection = board_intersect[1]
            normal = board_intersect[2]
            t = board_intersect[3]

        # Checks for sphere1
        sphere1_intersect = sphere1_intersection(cop, ray, t)
        if (sphere1_intersect[0]):
            obj_cd = 1
            intersection = sphere1_intersect[1]
            normal = sphere1_intersect[2]
            t = sphere1_intersect[3]

        # Checks for sphere2
        sphere2_intersect = sphere2_intersection(cop, ray, t)
        if (sphere2_intersect[0]):
            obj_cd = 2
            intersection = sphere2_intersect[1]
            normal = sphere2_intersect[2]
            t = sphere2_intersect[3]

        # Checking the object codes
        if (obj_cd == 0):
            rgb = checkerboard_pt_intensity(level, ray, intersection, normal) # Checkerboard
        elif (obj_cd == 1):
            rgb = sphere1_pt_intensity(level, ray, intersection, normal) # Sphere1
        elif (obj_cd == 2):
            rgb = sphere2_pt_intensity(level, ray, intersection, normal) # Sphere2
        else:
            rgb = [150, 150, 255] # Sky :]

    return rgb

def lightingModel(normal, color): 
    kd = 0.8
    ambient = 0.4 * kd

    L = [1, 1, -1] # Light vector
    mag = math.sqrt(L[0]**2 + L[1]**2 + L[2]**2) # The magnitude to calculate the normal
    L[0] = L[0]/mag
    L[1] = L[1]/mag
    L[2] = L[2]/mag

    # Colors passed in are going to be a value between 0 and 255. This will set them as percentages of 255 like the vectors found in this function do
    i = 0
    while i < 3:
        color[i] = color[i]/255
        i += 1

    ip = 0.7
    # The dot product!!!! of the normal and the light vector!!!!
    dot = ((normal[0]*L[0]) + (normal[1]*L[1]) + (normal[2]*L[2]))

    diffuse = ip * dot * kd

    r = [0, 0, 0] # for the reflection vector and the viewing vector :)
    v = [0, 0, -100]

    ks = 0.9
    twocos = 2 * dot

    # Light is above
    if (twocos > 0):
        r[0] = normal[0] - (L[0]/twocos)
        r[1] = normal[1] - (L[1]/twocos)
        r[2] = normal[2] - (L[2]/twocos)
    # Light is at 90
    elif (twocos == 0):
        r[0] = -L[0]
        r[1] = -L[1]
        r[2] = -L[2]
    # Light is below
    elif (twocos < 0):
        r[0] = -normal[0] + (L[0]/twocos)
        r[1] = -normal[1] + (L[1]/twocos)
        r[2] = -normal[2] + (L[2]/twocos)
    else:
        print("UH OH") # ERROR CASE THING

    mag = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2) # Normalizing the reflection vector
    r[0] = r[0]/mag
    r[1] = r[1]/mag
    r[2] = r[2]/mag
    mag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2) # Normalizing the viewing vector
    v[0] = v[0]/mag
    v[1] = v[1]/mag
    v[2] = v[2]/mag

    # 
    dot = ((v[0]*r[0]) + (v[1]*r[1]) + (v[2]*r[2]))
    specular = ip * (dot**16) * ks

    light = ambient + diffuse + specular
    
    R = light * color[0] * 255
    G = light * color[1] * 255
    B = light * color[2] * 255

    return [R, G, B]    

def sphere1_intersection(cop, ray, t):
    # center of sphere
    cos = [50, -100, 900]
    # radius of sphere
    r = 100

    # the array that will be returned with the relevant information to the intersection
    results = [False]

    # math up the intersection
    asphere = ray[0]**2 + ray[1]**2 + ray[2]**2
    bsphere = (2*ray[0]*(cop[0]-cos[0])) + (2*ray[1]*(cop[1]-cos[1])) + (2*ray[2]*(cop[2]-cos[2]))
    csphere = cos[0]**2 + cos[1]**2 + cos[2]**2 + cop[0]**2 + cop[1]**2 + cop[2]**2 + 2*(-cos[0]*cop[0] - cos[1]*cop[1] - cos[2]*cop[2]) - r**2

    disc = bsphere**2 - 4*asphere*csphere

    # Check where the light is and all that
    if (disc < 0.001):
        return results
    else:
        ts1= (-bsphere + math.sqrt(disc)) / (2*asphere)
        ts2 = (-bsphere - math.sqrt(disc)) / (2*asphere)
        if (ts1 >= ts2):
            tsphere = ts2
        else:
            tsphere = ts1
            
        if (t < tsphere):
            return results
        elif (tsphere < 0.001):
            return results
        else:
            t = tsphere
            x = cop[0] + ray[0]*tsphere
            y = cop[1] + ray[1]*tsphere
            z = cop[2] + ray[2]*tsphere
            nx = x - cos[0]
            ny = y - cos[1]
            nz = z - cos[2]
            intersection = [x, y, z]
            normal = [nx, ny, nz]
            results = [True, intersection, normal, t] # YAY CIRCLES
            return results

# Same as sphere1
def sphere2_intersection(cop, ray, t):
    # center of sphere
    cos = [-200, 150, 2000]
    # radius of sphere
    r = 250

    # the array that will be returned with the relevant information to the intersection
    results = [False]

    # math up the intersection
    asphere = ray[0]**2 + ray[1]**2 + ray[2]**2
    bsphere = (2*ray[0]*(cop[0]-cos[0])) + (2*ray[1]*(cop[1]-cos[1])) + (2*ray[2]*(cop[2]-cos[2]))
    csphere = cos[0]**2 + cos[1]**2 + cos[2]**2 + cop[0]**2 + cop[1]**2 + cop[2]**2 + 2*(-cos[0]*cop[0] - cos[1]*cop[1] - cos[2]*cop[2]) - r**2

    # math for the disc
    disc = bsphere**2 - 4*asphere*csphere

    if (disc < 0.001):
        return results
    else:
        ts1= (-bsphere + math.sqrt(disc)) / (2*asphere)
        ts2 = (-bsphere - math.sqrt(disc)) / (2*asphere)
        if (ts1 >= ts2):
            tsphere = ts2
        else:
            tsphere = ts1
            
        if (t < tsphere):
            return results
        elif (tsphere < 0.001):
            return results
        else:
            t = tsphere
            x = cop[0] + ray[0]*tsphere
            y = cop[1] + ray[1]*tsphere
            z = cop[2] + ray[2]*tsphere
            nx = x - cos[0]
            ny = y - cos[1]
            nz = z - cos[2]
            intersection = [x, y, z]
            normal = [nx, ny, nz]
            results = [True, intersection, normal, t]
            return results

# Similar to spheres
def checkerboard_intersection(cop, ray, t):

    #global intersection, t
    # normal of plane
    N = [0, 1, 0]
    # point on plane
    P = [0, -300, 0]
    # compute intersection of ray with plane
    denom = N[0]*ray[0] + N[1]*ray[1] + N[2]*ray[2]

    # the array that will be returned with the relevant information to the intersection
    results = [False]

    if ( abs(denom) <= 0.001): # parallel to plane
        return results
    else:
        D = N[0]*P[0] + N[1]*P[1] + N[2]*P[2]
        t_object = -(N[0]*cop[0] + N[1]*cop[1] + N[2]*cop[2] - D) / denom
        x = cop[0] + ray[0] * t_object
        y = cop[1] + ray[1] * t_object
        z = cop[2] + ray[2] * t_object
        if ( z < 0.001 or z > 8000 or t_object < 0.001): # no visible intersection
            return results
        elif (t < t_object): # another object is closer
            return results
        else:
            intersection = [x, y, z]
            t = t_object
            results = [True, intersection, N, t] # sends back the normal and the intersection and the t value
            return results

def sphere1_pt_intensity(level, ray, intersection, normal):
    # magnitude to normalize the ray
    mag = math.sqrt(ray[0]**2 + ray[1]**2 + ray[2]**2)
    rxn = ray[0]/mag
    ryn = ray[1]/mag
    rzn = ray[2]/mag

    # normalize the incoming normal
    mag = math.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
    nxn = normal[0]/mag
    nyn = normal[1]/mag
    nzn = normal[2]/mag

    # Calculate reflection vector
    cos_phi = -(rxn*nxn) - (ryn*nyn) - (rzn*nzn)

    # Check the relationship of the light to the object :^)
    if (cos_phi > 0):
        rx = nxn - (-rxn) / (2*cos_phi)
        ry = nyn - (-ryn) / (2*cos_phi)
        rz = nzn - (-rzn) / (2*cos_phi)

    if (cos_phi == 0):        
        rx = rxn
        ry = ryn
        rz = rzn

    if (cos_phi < 0):        
        rx = -nxn + (-rxn) / (2*cos_phi)
        ry = -nyn + (-ryn) / (2*cos_phi)
        rz = -nzn + (-rzn) / (2*cos_phi)

    new_ray = [rx, ry, rz]
    new_normal=[nxn,nyn,nzn]
    color = [17, 255, 132]
    RGB = trace_ray(level - 1, intersection, new_ray) # Call trace_ray one depth level lower

    lighting = lightingModel(new_normal, RGB) # Call the lighting for the objecet

    R = .2 * color[0] + .8 * lighting[0]
    G = .2 * color[1] + .8 * lighting[1]
    B = .2 * color[2] + .8 * lighting[2]

    RGB = [R, G, B]
    
    return RGB

# Same as ^^ with a different color passed in (I deff could've made this more efficient oops...)
def sphere2_pt_intensity(level, ray, intersection, normal):
    # magnitude to normalize the ray
    mag = math.sqrt(ray[0]**2 + ray[1]**2 + ray[2]**2)
    rxn = ray[0]/mag
    ryn = ray[1]/mag
    rzn = ray[2]/mag

    # normalize the incoming normal
    mag = math.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
    nxn = normal[0]/mag
    nyn = normal[1]/mag
    nzn = normal[2]/mag

    # Calculate reflection vector
    cos_phi = -(rxn*nxn) - (ryn*nyn) - (rzn*nzn)

    if (cos_phi > 0):
        rx = nxn - (-rxn) / (2*cos_phi)
        ry = nyn - (-ryn) / (2*cos_phi)
        rz = nzn - (-rzn) / (2*cos_phi)

    if (cos_phi == 0):        
        rx = rxn
        ry = ryn
        rz = rzn

    if (cos_phi < 0):        
        rx = -nxn + (-rxn) / (2*cos_phi)
        ry = -nyn + (-ryn) / (2*cos_phi)
        rz = -nzn + (-rzn) / (2*cos_phi)

    new_ray = [rx, ry, rz]
    new_normal=[nxn,nyn,nzn]
    color = [17, 53, 255]
    RGB = trace_ray(level - 1, intersection, new_ray)

    lighting = lightingModel(new_normal, RGB)

    R = .2 * color[0] + .8 * lighting[0]
    G = .2 * color[1] + .8 * lighting[1]
    B = .2 * color[2] + .8 * lighting[2]

    RGB = [R, G, B]
    
    return RGB
# Similar to above with a color checker for red or white
def checkerboard_pt_intensity(level, ray, intersection, normal):
    color_flag = True
    if (intersection[0] >= 0 ):
        color_flag = True
    else:
        color_flag = False

    if ((abs(math.fmod(intersection[0], 400.0))) > 200.0):
        color_flag = not color_flag
    if ((abs(math.fmod(intersection[2], 400.0))) > 200.0):
        color_flag = not color_flag

    if (color_flag):
        color = [255, 0, 0]
    else:
        color = [255, 255, 255]

    mag = math.sqrt(ray[0]**2 + ray[1]**2 + ray[2]**2)
    rxn = ray[0]/mag
    ryn = ray[1]/mag
    rzn = ray[2]/mag

    # Calculate reflection vector
    cos_phi = -(rxn*normal[0]) - (ryn*normal[1]) - (rzn*normal[2])

    if (cos_phi > 0):
        rx = normal[0] - (-rxn) / (2*cos_phi)
        ry = normal[1] - (-ryn) / (2*cos_phi)
        rz = normal[2] - (-rzn) / (2*cos_phi)

    if (cos_phi == 0):        
        rx = rxn
        ry = ryn
        rz = rzn

    if (cos_phi < 0):        
        rx = -normal[0] + (-rxn) / (2*cos_phi)
        ry = -normal[1] + (-ryn) / (2*cos_phi)
        rz = -normal[2] + (-rzn) / (2*cos_phi)

    new_ray = [rx, ry, rz]

    # trace the reflection vector
    RGB = trace_ray(level - 1, intersection, new_ray)

    lighting = lightingModel(normal, RGB)

    R = .5 * color[0] + .5 * lighting[0]
    G = .5 * color[1] + .5 * lighting[1]
    B = .5 * color[2] + .5 * lighting[2]

    RGB = [R, G, B]

    return RGB

def quit_proc():
    root.destroy()
    
###########################################################################################################################################################################################################################
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
#render_proc()
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

rendercontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
rendercontrols.pack(side=LEFT)

renderButton = Button(rendercontrols, text="Render", fg="green", command=render_proc)
renderButton.pack(side=LEFT)

quitButton = Button(rendercontrols, text="Quit", fg="red", command=quit_proc)
quitButton.pack(side=RIGHT)
