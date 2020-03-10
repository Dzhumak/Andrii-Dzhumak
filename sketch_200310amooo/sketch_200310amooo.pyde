#uzycie tablicy, przemieszczanie sie, zmiana kolorow po tablice, pakowanie rozpakowanie kolekcji, zamkniecie programu
#() krotka - do wartosci tylko odczytywanych
#[] lista - pozostale 
#{} slownik - dla kontaktowania programow, kiedy musimy rozmawiac z zewnetrznymi programami
#{} zbior - zeby sie nie powtazali wartosci, wartosci unikalne

def setup():
    size(400,600)
    frameRate(10)
    
    global dict
    global natezenie
    
    natezenie = 0
    
    dict = {"red":(255,0,0), "blue":(0,0,255), "grey":(120)}

def draw():
    global natezenie
    
    colors = {(255,0,0), (0,0,255), (0,255,0)}
    
    stroke (natezenie, 0, 0, 100)
    
    natezenie +=1
    
    if (natezenie == 255):
        natezenie=0
    
    line(mouseX, mouseY, width/3, height/3)
    fill(*dict["red"])
    
    rect(60,20,200,300)
    fill(dict["grey"])
    stroke(*dict["red"])
    
    rect(250,350,100,100)
    
    list_IN_list = [[10,20,30],[40,50,60],[70,80,90]]
    #print (list_IN_list[0][0])
    for sub_list in list_IN_list:
        print (sub_list)
        for element in sub_list:
            print (element)

            
def mousePressed():
    exit()
    
    #myList = [[236,189,189,0], [236,80,189,189], [236,189,189,80], [236,0,189,80]]
    #for i in range(100):
     #   for index0 in myList:
      #      for index1 in index:
       #         stroke(20)
        #        print(myList[index0][index1])
         #       point (i,100)
