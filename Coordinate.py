class Coordinate:
    '''Base class to represent the coordinates of the robots and the tasks.'''
    
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
        
    def get_coordinates(self):
        return self
    
    pass