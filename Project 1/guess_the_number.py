secret_number = 7
attempts = 5

while attempts != 0:

    guess_number = int(input("Guess the Number : "))

    if guess_number == secret_number:
        print(f"You Won : {secret_number} This guess is right")
        break

    elif guess_number > secret_number:
        print(f"Too High : {guess_number}")

    else:
        print(f"Too Low")

    attempts -= 1
    print(f"Attempts Left : {attempts}")