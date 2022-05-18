
from resources import Rotorer, ActiveRotors
from math import floor
import random

z = ActiveRotors(0)



# transformer = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
# 27,0,6,4,28,14,18,13,3,15,10,19,5,11,26,17,25,16,23,1,29,2,21,20,7,22,9,8,12,24,
# def rotor_blend(transformer):
#     random.shuffle(transformer)
#     print(transformer)

# rotor_blend(transformer)

def open_textfile():
    with open('text_dokument.txt', "r", encoding="utf8" ) as txt_file:
        contents = txt_file.read()
        #print(contents)
        contents.replace("\n", "")
        return contents
        #print(contents)
        # with open('text_dokument2.txt', "w", encoding="utf8" ) as txt_file2:
        #     txt_file2.write(contents)

        # while True:
        #     i = contents.find("\n")

def new_text(contents):
    with open('text_dokument2.txt', "w", encoding="utf8" ) as txt_file2:
        txt_file2.write(contents)

# open_textfile()

def krypt(pos,x,rot,bigin):
    if rot == 0:
        return x[rot].get_kombination()[pos]
    elif bigin == 0:
        pos = int(x[rot].get_kombination()[pos])
        rot = rot - 1
        return krypt(pos,x,rot,bigin)
    elif rot == len(x)-1:
        bigin = 0
        pos = int(x[rot].get_kombination()[pos])
        return krypt(pos,x,rot,bigin)
    else:
        pos = int(x[rot].get_kombination()[pos])
        rot = rot + 1 
        return krypt(pos,x,rot,bigin)



def krypting():
    #text = input("Text: ")
    text = open_textfile()
    x = z.get_rotors()
    ctypted = ""
    for leter in text:
        pos = 0
        for i in x[0].get_kombination():
            if i == leter:
                rot = 1
                bigin = 1
                #print(rotation(pos,x,rot,bigin))
                ctypted = ctypted + krypt(pos,x,rot,bigin)
                #ctypted = ctypted + x[0].get_kombination()[int(x[1].get_kombination()[int(x[2].get_kombination()[int(x[3].get_kombination()[int(x[3].get_kombination()[int(x[2].get_kombination()[int(x[1].get_kombination()[pos])])])])])])]
                for i in range(1,len(x)):
                    c = x[i].rotate_rotor()
                    if c == 0:
                        break
                break
            pos = pos + 1
    new_text(ctypted)


def key_create(choice):
    key = [0]
    print("Nyckel segment x får vara 0 <= x <= 29")
    print("Skriv ett segment sen tryck return")
    for i in range(3):
        key.append(int(input("")))
    if choice == 1:
        load_rotors(key)
    elif choice == 2:
        
        pass

def decrypt_calculator(text,key):
    pass  #                          <----------------------
    if len(text) >= 841:
        key[1] = floor(key[1] + (len(text)/841)) 
    if len(text) >= 29:
        key[2] = floor(key[2] + (len(text)/29))
    if len(text) >= 0:
        key[3] = floor(key[3] + len(text))





def load_rotors(key):
    with open("rotors.txt", "r", encoding="utf8") as rotor_file:
        z.clear_rotors()
        kombination_txt = []
        for line in rotor_file.readlines():
            a = line.split(",")
            a.pop(len(a)-1)
            kombination_txt.append(a)
    for i in range(1):
        z.add_rotor(Rotorer(i,key[0],kombination_txt[i]))
    for i in range(1,4):
        z.add_rotor(Rotorer(i,key[i],kombination_txt[i]))
    # for i in z.get_rotors():
    #     print(i.get_kombination())

def option_1():
    key_create(1)

    krypting()

def option_2():
    key_create(2)
    pass

def options():
    print("[1] Kryptering")
    print("[2] Dekryptering")
    print("[0] Avsluta programet")

def menu():
    while True:
        options()
        choice = input(">> ")
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "0":
            break

def main():

    menu()
    # rotors = int(input("Hur många rotors vill di använda? "))
    # mixer(text)
    # rotor_blend()
    #krypting()
   
    

if __name__ == "__main__":
    main()


# for i in range(1,len(x)):
#     c = x[i].rotate_rotor()
#     if c == 0:
#         break
#break