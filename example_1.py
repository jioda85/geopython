# script to exercies "CLASS"

from math import sqrt

class point():
    
    def __init__(self, x, y):   #__init__: init = initialized the object
        self.x = x
        self.y = y 
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
        
    def __add__(self, other):     #__add__: 
        return point(self.x + other.x, self.y + other.y)
        #isinstance(other, point)
    
    def __repr__(self):         #__repr__: representative?
        return 'point(', self.x, self.y,')'
    
    def __str__(self):          #__str__: string
        return '(%f, %f)' % (self.x, self.y)
        

p1 = point(1.0, 2.0)
p2 = point(3.0, 4.0)
p3 = p1 + p2

print 'p1 = ', p1.x, p1.y
print 'p2 = ', p2.x, p2.y

print 'p1.norm() = ', p1.norm()
print 'p2.norm() = ', p2.norm()

print 'p1 + p2 =', p3