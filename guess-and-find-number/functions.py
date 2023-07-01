import random

def find_num_of_pc(max=10):
    print(f"Lets play a game! I have guessed a number from 1 to {max}.")
    print("Can you find it?!")
    min = 1
    i = 1
    pc_number = random.randint(min, max)
    while True:
        guessed_number = int(input(f"⇨ "))
        if guessed_number==pc_number:
            print(f"You have found my guessed number in {i} attempts. Congrats!")
            break
        elif guessed_number>pc_number:
            print("My number is less than that!")
            i+=1
        else:
            print("My number is more than that!")
            i+=1
    return i   

def find_num_of_user(max = 10):
    print(f"Now, guess the number from 1 to {max} and I will find it in several attempts!.")
    i = 1
    min = 1
    input("If you already chose the number, press ↲Enter")
    while True:
        guess_num_pc = random.randint(min, max)
        tasdiq = input(f"You have guessed {guess_num_pc}: correct(c), more(+), less(-)\n⇨")
        if tasdiq=='t':
            print(f"I have found in {i} attempts")
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
        print("I won the game!\nyou : pc\n  "+str(taxmin_user), ':', taxmin_pc)
    elif taxmin_user<taxmin_pc:
        print("You won the game!\nyou : pc\n  "+str(taxmin_user), ' :', taxmin_pc)
    else:
        print("Draw!")
