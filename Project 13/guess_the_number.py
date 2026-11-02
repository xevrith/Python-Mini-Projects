import random as r

attempts = 5
number = r.randint(1,20)

guess_number = 0

while attempts >= 1:
    guess_number = int(input("Guess the number : "))
    if guess_number == number:
        print("You Won")
        break
    else:
        print("Wrong Guess")

    attempts -= 1
    print(f"{attempts} Attempts Left")

if attempts == 0:
    print(f"Correct Number : {number}")

else:
    print(f"Congrats for your victor")