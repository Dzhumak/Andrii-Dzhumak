global side
side = 100    

global xpos
xpos = 0 

global ypos
ypos = 0 

global xdirection
xdirection = 1

global ydirection
ydirection = 1

def setup():
    global xpos, ypos
    size(640, 360)
    frameRate(60)
    rectMode(CENTER)
    xpos = width/2
    ypos = height/2


def draw():
    
    background(100)
    dict = {"red":(255,0,0), "blue":(0,0,255), "grey":(120)}
  
    global xpos, ypos, xdirection, ydirection, side
    xpos = xpos + xdirection 
    ypos = ypos + ydirection 
    
    if (xpos > width-(side/2) or xpos < side/2):
        xdirection *= -1
        fill(*dict["red"])
            
  
    if (ypos > height-(side/2) or ypos < side/2):
        ydirection *= -1
        fill(*dict["blue"])
        
  
    rect(xpos, ypos, side, side)

def mousePressed():
    exit()
