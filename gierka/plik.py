import random
 
list_guessed = []

while True:

    liczba_losowa = random.randint(1, 10)
    tries = 0
    while True:
        x = input("Find number between 1 - 10 (press Q to quit): ")
        tries += 1
        if x.lower() == 'q':
            print("\nThanks for playing!")
            break

        try:
            x = int(x)
        except ValueError:
            print("Invalid input, please enter a number or 'Q' to quit.")
            continue

        if x == liczba_losowa:
            print("You guessed!")
            list_guessed.append(x)
            liczba_losowa = random.randint(1, 20)  # generuje nową losową liczbę
            print("You guessed in", tries, "tries.")
            break  # przerywa pętlę, gdy użytkownik trafi liczbę
        elif x < liczba_losowa:
            print("Too small number")
        else:
            print("Too big number")

    
    
    if(x == 'q'):
        break


print("\nGuessed numbers: ")
for i in list_guessed:
    print(i, end=" ")