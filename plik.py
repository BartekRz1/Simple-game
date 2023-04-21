import random

liczba_losowa = random.randint(1, 20)


while(True):
    x = int(input("find number between 1 - 20 "))
    if(x == liczba_losowa):
        print("you guessed")
        break
    elif(x < liczba_losowa):
        print("too small number")
    else:
        print("too big number")