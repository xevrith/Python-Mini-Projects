# Basic Calculator


def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operation == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot calculate remainder with zero.")
        return num1 % num2
    elif operation == "**":
        return num1 ** num2
    else:
        raise ValueError("Unsupported operation.")


def main():
    print("=== Calculator ===")
    print("Operations: +  -  *  /  %  **")
    print("Type 'exit' at the operation prompt to quit.")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operation = input("Enter operation: ").strip()
            if operation.lower() == "exit":
                print("Thank you for using the calculator.")
                break
            num2 = float(input("Enter second number: "))
            result = calculate(num1, operation, num2)
            print(f"Result: {result:g}")
        except ValueError as error:
            print(error if str(error) == "Unsupported operation." else "Please enter valid numbers and an available operation.")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
