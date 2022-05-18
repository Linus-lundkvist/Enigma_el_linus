

class Rotorer:
    
    def __init__(self,id,rotation,kombination) -> None:
        self.id = id
        self.rotation = rotation
        for _ in range(self.rotation):
            kombination.append(kombination.pop(0))
        self.kombination = kombination
    
    def get_kombination(self):
        return self.kombination
    
    def rotate_rotor(self):
        if self.rotation == len(self.kombination)-1:
            self.rotation = 0
            self.kombination.append(self.kombination.pop(0))
            return 1
        else: 
            self.kombination.append(self.kombination.pop(0))
            self.rotation = self.rotation + 1
            return 0

    def reverse_rotate_rotor(self):
        if self.rotation == 0:
            self.rotation = 29
            plaze = self.kombination[0]
            self.kombination[0] = self.kombination[29]
            self.kombination[29] = plaze
            return 1
        else:
            plaze = self.kombination[0]
            self.kombination[0] = self.kombination[29]
            self.kombination[29] = plaze
            self.rotation = self.rotation - 1
            return 0


class ActiveRotors:

    def __init__(self,id) -> None:
        self.rotors = []
    
    def add_rotor(self,rotor):
        self.rotors.append(rotor)
    
    def get_rotors(self):
        return self.rotors
    
    def clear_rotors(self):
        self.rotors = []


# x0 = Rotorer(1,5,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
# x1 = Rotorer(2,7,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])

# z = Active_rotors(0)

# rotations = [0,0,0,0]

# with open("rotors.txt", "r", encoding="utf8") as rotor_file:
#     kombination_txt = []
#     for line in rotor_file.readlines():
#         a = line.split(",")
#         a.pop(len(a)-1)
#         kombination_txt.append(a)
#         #print(line.split(","))
#         #kombination_txt.append(line.split(","))
#         #kombination_txt.pop(len(kombination_txt))
#         #kombination_txt.append(line)
#     #print(kombination_txt[3])
#     for i in range(4):
#         z.add_rotor(Rotorer(i,rotations[i],kombination_txt[i]))
#     for i in z.get_rotors():
#         print(i.get_kombination())

# z.add_rotor(x0)
# z.add_rotor(x1)
# print(x0.get_kombination())
# print(x1.get_kombination())

# for i in z.get_rotors():
#     print(i.get_kombination())

