import random

comearer = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"," "]
transformer = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
rotor1 = [9,3,10,25,27,18,28,7,22,23,11,12,29,5,8,20,4,1,0,24,26,13,15,6,14,2,21,17,19,16]
rotor2 = [23,21,16,4,0,1,9,26,7,27,2,18,25,8,20,12,22,29,15,5,6,3,13,17,10,28,24,14,11,19]

def rotor_blend(transformer):
    random.shuffle(transformer)
    print(transformer)
    

def rotater(rotor):
    rotor.append(rotor.pop(0))
    return rotor

def main():
    # rotors = int(input("Hur många rotors vill di använda? "))
    text = input("Text: ")
    # mixer(text)
    # rotor_blend()
    ctypted = []
    for leter in text:
        pos = 0
        for i in comearer:
            if i == leter:
                ctypted.append(rotor1[pos])
                rotater(rotor1)
                break
            pos = pos + 1
    new_text =""
    for i in ctypted:
        new_text = new_text + comearer[i]
    print(new_text)
    

if __name__ == "__main__":
    main()