_MIN_DIV_LENGTH = 8 #Minimum length for bacteria to divide

class Bacteria:
    def __init__(self, length, posX, posY, extraAtt, name = "unnamed"):
        self.len = length
        self.posX = posX 
        self.posY = posY
        self.age = extraAtt #for when another attribute is included later
        self.isDead = False
        self.name = name

    def divide(self, daugher1name = "D1", daughter2name = "D2"):
        """Returns (daughter 1, daughter 2) by dividing this bacterium.
        Daghter age is set to 0."""
        daughter1 = Bacteria( self.len/2, self.posX+1, self.posY-1, 0, daugher1name)
        daughter2 = Bacteria( self.len/2, self.posX-1, self.posY+1, 0, daughter2name)
        return (daughter1, daughter2)

    def print(self):
        """Prints properties of this bacterium."""
        print ("Length: {}".format(self.len))
        print ("X position: {}".format(self.posX))
        print ("Y position: {}".format(self.posY))
        print ("Other attribute: {}\n".format(self.age))

    def ageBacterium(self):
        """Age bacteria by one unit of time and increase length accordingly"""
        if not self.isDead:
            self.age += 1
            self.len *= 1.2*random.uniform(.9,1.25)

    def getDivisionProbability(self):
        """Return probablity that this bacteria will divide"""
        if self.len < _MIN_DIV_LENGTH or self.isDead:
            return 0
            #TODO: use a better function
        return min(1, 0.05*self.len)

    def murder(self):
        """Kill this bacteria in cold blood"""
        self.isDead = True