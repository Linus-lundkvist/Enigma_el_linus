

class Rotorer():
    
    def __init__(self,id,rotation,kombination) -> None:
        self.id = id
        self.rotation = rotation
        for _ in range(self.rotation):
            kombination.append(kombination.pop(0))
        self.kombination = kombination
    
    def rotate_rotor(self):
        if self.rotation == len(self.kombination):
            self.rotation = 0
            self.kombination.append(self.kombination.pop(0))
            Active_rotors
        else: 
            self.kombination.append(self.kombination.pop(0))
            self.rotation = self.rotation + 1



class Active_rotors():

    def __init__(self,rotors) -> None:
        self.rotors = []
    
    def add_rotor(self,rotor):
        self.rotors.append(rotor)
    
    def get_rotors(self):
        return self.rotors
    
    def clear_rotors(self):
        self.rotors = []
