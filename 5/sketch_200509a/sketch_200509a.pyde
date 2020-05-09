class Robots():
    
    robots_quantity = 0
    
    def __init__(self, name, health, intelligence, power, durability):
        
        self.name = name
        self.hp = health
        self.iq = intelligence
        self.power = power
        self.durability = durability
        
        Robots.robots_quantity +=1
        
    def show_robots_specs(self):
        print("Name: " + self.name + ", " + str(self.hp) + "HP, " + str(self.iq) + "IQ, " 
              + "Power out of 100: " + str(self.power) + ", " + "Durability out of 100: " + str(self.durability) + ";")
def setup():
    global android, cyborg
    
    android = Robots("Android X", 100, 215, 85, 70)
    cyborg = Robots("Cyborg 2000", 100, 160, 95, 90)
    
    android.show_robots_specs()
    cyborg.show_robots_specs()
    
    print(Robots.robots_quantity)
