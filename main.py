import random

comearer = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"," "]
# rotor1 = ['h', 'å', 'f', 'u', 'ö', 'ä', 's', 'b', 'l', 'i', 'd', 't', 'k', 'j', 'z', 'm', 'p', 'q', 'o', 'g', 'r', 'x', 'w', 'e', 'v', 'c', 'n', 'a', 'y']
# rotor2 = ['å', 'o', 's', 'j', 'i', 'l', 'x', 'w', 'q', 'z', 'g', 'b', 'r', 'h', 'y', 'd', 'ö', 'c', 'f', 'ä', 't', 'v', 'a', 'e', 'n', 'u', 'p', 'm', 'k']
# rotor3 = ['w', 'q', 'ö', 'h', 'e', 'b', 'i', 'l', 'v', 'r', 'n', 'x', 'k', 'a', 'm', 'c', 'd', 'å', 'f', 'o', 't', 'p', 's', 'y', 'g', 'j', 'z', 'u', 'ä']

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
                print(rotor1[pos])
                ctypted.append(rotor1[pos])
                rotater(rotor1)
                break
            pos = pos + 1
    print(ctypted)
    

if __name__ == "__main__":
    main()