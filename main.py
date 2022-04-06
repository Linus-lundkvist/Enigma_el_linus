import random

rotor0 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
rotor1 = ['h', 'å', 'f', 'u', 'ö', 'ä', 's', 'b', 'l', 'i', 'd', 't', 'k', 'j', 'z', 'm', 'p', 'q', 'o', 'g', 'r', 'x', 'w', 'e', 'v', 'c', 'n', 'a', 'y']
rotor2 = ['å', 'o', 's', 'j', 'i', 'l', 'x', 'w', 'q', 'z', 'g', 'b', 'r', 'h', 'y', 'd', 'ö', 'c', 'f', 'ä', 't', 'v', 'a', 'e', 'n', 'u', 'p', 'm', 'k']
rotor3 = ['w', 'q', 'ö', 'h', 'e', 'b', 'i', 'l', 'v', 'r', 'n', 'x', 'k', 'a', 'm', 'c', 'd', 'å', 'f', 'o', 't', 'p', 's', 'y', 'g', 'j', 'z', 'u', 'ä']

def rotor_blend():
    random.shuffle(rotor1)
    print(rotor1)

def mixer(text):
    print(rotor0)
    rotor0.append(rotor0.pop(0))
    print(rotor0)
    # for bokstav in text:
    #     print(bokstav)


def main():
    text = input("Text: ")
    mixer(text)
    #rotor_blend()

if __name__ == "__main__":
    main()