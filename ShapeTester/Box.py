class Cube(object):
    volume = 0
    SA = 0

    def __init__(self):
        self.w = 0
        self.l = 0
        self.h = 0

    def volume(self):
        volume = self.w * self.l * self.h
        print("Your volume is: " + str(volume))

    def SA(self):
        SA = 2*self.w*self.l + 2*self.l*self.h + 2*self.w*self.h
        print("Your surface area is: " + str(SA))
    
    
          
