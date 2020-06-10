def setup():
  global img
  size(640,480)
  
  imageMode(CENTER)
  rectMode(CENTER)
  textAlign(CENTER)
  
  background(0)
  textSize(16)
  strokeWeight(7)
  noFill()
  
def draw():
  global img # 500x375
  
  try:
    img = loadImage("duck.jpg")
    image(img, width/2, height/2)
  except:
    stroke(255, 0, 0)
    rect (width/2,height/2,500,375)
    text("Brak pliku lub blad wczytywania", width/2, height/2)
  else:
    stroke(0, 0, 255)
    rect (width/2,height/2,500,375)
    image(img, width/2, height/2)
