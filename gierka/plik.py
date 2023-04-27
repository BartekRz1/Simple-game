import random

while True:
    list_guessed = []
    liczba_losowa = random.randint(1, 20)

    while True:
        x = input("Find number between 1 - 20 (press Q to quit): ")

        if x.lower() == 'q':
            print("Thanks for playing!")
            exit()

        try:
            x = int(x)
        except ValueError:
            print("Invalid input, please enter a number or 'Q' to quit.")
            continue

        if x == liczba_losowa:
            print("You guessed!")
            list_guessed.append(x)
            liczba_losowa = random.randint(1, 20)  # generuje nową losową liczbę
            break  # przerywa pętlę, gdy użytkownik trafi liczbę
        elif x < liczba_losowa:
            print("Too small number")
        else:
            print("Too big number")

    print("You guessed in", len(list_guessed), "tries.")

    

print("\n guessed numbers: ")
for i in list_guessed:
    print(i, end=" ")
# we want if number is guessed number append it to list 