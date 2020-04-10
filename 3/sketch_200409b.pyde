def setup():
    global f
    size(300,300)
    f = createFont("Arial",16)
    textSize(64)
    textAlign(CENTER)


def draw():
    global f
    background(38,43,48)
    
    
#--A----
    if (((keyPressed) and ((key == 'A') or (key == 'a'))) or ((key == CODED) and (keyCode == LEFT)) or ( 145 > mouseX > 80 and 105 < mouseY < 150 )):
        fill(255)
        #print(key)
    else:   
        fill(100)
        #print(key)
    
    text("A.",(width/2)-30,height/2)
#--------


#--D----
    if(((keyPressed) and ((key == 'D') or (key == 'd'))) or ((key == CODED) and (keyCode == RIGHT)) or ( 145+64 > mouseX > 80+64 and 105 < mouseY < 150 )):
        fill(255)
        #print(key)
    else:   
        fill(100)
        #print(key)
    
    text("D.", (width/2)+30, (height/2))
#---------

#--SHAPE--
    fill(62,199,230,90)
    s = createShape() 
    s.beginShape()
    s.stroke(255)
    s.vertex((width/2)+10, (height/4)-20) # a
    s.vertex(((width/2)+(width/4))+37, (height/2)-20) #b
    s.vertex((width/2)+10, ((height/2)+(height/4))-10) #c 
    s.vertex((width/4)-10, (height/2)-20) #d
    s.endShape(CLOSE) 
    shape(s,-20,0)

        
