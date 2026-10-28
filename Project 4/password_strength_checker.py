import string


def check_password_strength(password):
    requirements = {
        "at least 8 characters": len(password) >= 8,
        "an uppercase letter": any(char.isupper() for char in password),
        "a lowercase letter": any(char.islower() for char in password),
        "a digit": any(char.isdigit() for char in password),
        "a special character": any(char in string.punctuation for char in password),
    }

    missing = [rule for rule, passed in requirements.items() if not passed]
    return missing


def main():
    print("=== Password Strength Checker ===")
    print("Your password should have 8+ characters, uppercase and lowercase letters,")
    print("a number, and a special character.\n")

    while True:
        password = input("Enter a password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Goodbye.")
            break

        missing = check_password_strength(password)

        if not missing:
            print("Strong password: all requirements are met.")
            break

        print("Password is not strong enough. Missing:")
        for requirement in missing:
            print(f"- {requirement}")


if __name__ == "__main__":
    main()
