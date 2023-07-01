import random

def find_num_of_pc(max=10):
    print(f"Keling bir o'yin o'ynaymiz. Men {max} gacha biror son o'yladim.")
    print("Hozir siz men o'ylagan sonimni topishingiz zarur.")
    min = 1
    i = 1
    pc_number = random.randint(min, max)
    while True:
        guessed_number = int(input(f">>> "))
        if guessed_number==pc_number:
            print(f"Siz men o'ylagan sonni {i}-urunishda topdingiz. Tabriklayman!")
            break
        elif guessed_number>pc_number:
            print("Men o'ylagan son bundan kichikroq!")
            i+=1
        else:
            print("Men o'ylagan son bundan kattaroq!")
            i+=1
    return i   

def find_num_of_user(max = 10):
    print(f"Endi siz {max} gacha son o'ylang. Men uni topishga harakat qilaman.")
    i = 1
    min = 1
    input("Agar son o'ylagan bo'lsangiz biror tugmani bosing")
    while True:
        guess_num_pc = random.randint(min, max)
        tasdiq = input(f"Siz {guess_num_pc} ni o'yladingiz: to'g'ri(t), kattaroq(+), kichikroq(-)\n>>>")
        if tasdiq=='t':
            print(f"Siz o'ylagan sonni men {i}-urinishda topdim!")
            break
        elif tasdiq=='+':
            min=guess_num_pc+1
            i+=1
        else:
            max=guess_num_pc-1
            i+=1
    return i
def play():
    taxmin_user = find_num_of_pc()
    print("\n")
    taxmin_pc = find_num_of_user()
    if taxmin_user>taxmin_pc:
        print("Men yutdim!\nsiz : kompyuter\n  "+str(taxmin_user), ':', taxmin_pc)
    elif taxmin_user<taxmin_pc:
        print("Siz yutdingiz!\nsiz : kompyuter\n  "+str(taxmin_user), ' :', taxmin_pc)
    else:
        print("Durrang!")