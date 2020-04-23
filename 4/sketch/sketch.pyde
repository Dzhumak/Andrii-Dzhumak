add_library('pdf')

def setup():
    global img, t1, t2
    size(400, 400)
    
    textAlign(CENTER)
    textSize(32)
    
    img = loadImage("Bill.png")
    t1 = loadImage("t1.png")
    t2 = loadImage("t2.png")

def draw ():
    global img, t1, t2
#----------MENU-------------   
    background(38,43,48)
    
    fill(62,199,230)
    rect(50,50,300,100,12)
    rect(50,250,300,100,12)
    
    fill (255)
    text("Press and hold for mod-type 1", 50, 50, 300, 100)
    text("Press and hold for mod-type 2", 50, 250, 300, 100)

#---------Services menu------ 
    
    #-----Type1--------------
    if mousePressed and (mouseButton == LEFT) and (50 < mouseX < 350) and (50 < mouseY < 150):
        clear()
        beginRecord(PDF, "BillType1.pdf")
        image(img, 0,0, height, width)
        image(t1, 100, 230, width / 2, height / 2)
        endRecord()
    
    #-----Type2--------------
    elif mousePressed and (mouseButton == LEFT) and (50 < mouseX < 350) and (250 < mouseY < 350):
        clear()
        beginRecord(PDF, "BillType2.pdf")
        image(img, 0,0, height, width)
        image(t2, 100, 230, width / 2, height / 4)
        endRecord()
