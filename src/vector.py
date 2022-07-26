import math

class Vector:

    def __init__(self,x,y):

        self.x = x
        self.y = y

    def add(self,other_vector):

        self.x = self.x + other_vector.x
        self.y = self.y + other_vector.y

    def sub(self,other_vector):

        self.x = self.x - other_vector.x
        self.y = self.y - other_vector.y

    def scale(self, value):

        self.x = self.x * value
        self.y = self.y * value
    
    def get_mag(self):

        return math.sqrt(self.x **2 + self.y ** 2)

    def norm(self):

        mag = self.get_mag()
        if mag > 0:
            self.x = self.x / mag
            self.y = self.y / mag
    
    def set_mag(self, value):

        self.norm()
        self.scale(value)
    
    def limit_mag(self, max_value):

        if (self.get_mag() * self.get_mag()) > (max_value * max_value):
            self.set_mag(max_value)


    def div(self, value):

        self.x = self.x / value
        self.y = self.y / value


    def dist(self, other_vector):

        distance = math.sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)
        return distance