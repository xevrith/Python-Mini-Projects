# Calculator 


print("Use (+) For Addition)")
print("Use (-) For Subtraction)")
print("Use (*) For Multiplication)")
print("Use (/) For Division)")
print("Use (%) For Reminder)")
print("Use (**) For Power)")
print("Write 'Exit' and to stop the loop and 'Yes' To continue")

while True:

    command = input("Enter exist to stop the calc : ").lower()

    if command == "exit":
        print("Thank for use the calculator")
        break

    elif command == "yes":
        try:
            num1 = int(input("Enter the number : "))
            operation = input("Enter the Operation : ")
            num2 = int(input("Enter the number : "))

            if operation == "+":
                print(f"Addition : {num1 + num2}")

            elif operation == "-":
                print(f"Substraction: {num1 - num2}")

            elif operation == "*":
                print(f"Multiplication: {num1 * num2}")  

            elif operation == "**":
                print(f"Power: {num1 ** num2}") 

            elif operation == "%":
                print(f"Multiplication: {num1 % num2}")

            else:
                print(f"Division : {num1 / num2}")

        except ValueError:
            print("Wrong Input, Try Again")

        except ZeroDivisionError:
            print("Divided By 0, Try again")
    else:
        print("Wrong Input")
             