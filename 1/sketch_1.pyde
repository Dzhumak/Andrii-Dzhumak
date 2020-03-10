def setup():
    rectMode(CORNER)
    size(900,600)
    
    
def draw():
    
    clear()
    
    if mousePressed:
        rect(mouseX,400,400,100)
        col = color(250)
        fill(col)
    else:
        rect(mouseX, mouseY,width/3*2,height/3*2)
        c = color(0,255,0)
        fill(c)
