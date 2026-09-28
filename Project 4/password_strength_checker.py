while True:
    password = input("Enter a password : ")

    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
        print("Strong password")
        break
    else:
        print("Weak Password")