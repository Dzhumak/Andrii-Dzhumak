class Kwadrat():
    
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
# 2pkt
            
class KwadratKolorowy (Kwadrat, PasiastyKwadrat):
    
    def sketchKolorowy(self, x, y, r, g, b):
        fill(r,g,b)
        Kwadrat.sketch(self, x, y)
    
    def sketchPasiastyKolorowy(self, x, y, paski, r, g, b):
        fill(r,g,b)
        PasiastyKwadrat.sketchPasiasty(self, x, y, paski)
        
def setup():
    size(500, 500)
    
    kwadratCzerwony = KwadratKolorowy(100)
    kwadratCzerwony.sketchKolorowy(10, 10, 255, 0, 0)
    
    kwadratPasiastyZielony = KwadratKolorowy(100)
    kwadratPasiastyZielony.sketchPasiastyKolorowy(120, 10, 5, 0, 255, 0)
