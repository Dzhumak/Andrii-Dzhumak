def setup():
    size(400,600)

def draw(): 
    rect(mouseX, mouseY,width/3*2,height/3*2)
    
    if mousePressed:
        background(255, 204, 0)

    else: 
        circle(width/2,height/2,100)




    
