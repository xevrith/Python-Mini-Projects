hospital = {}

def info():
    print(f"1. Add Patient")
    print(f"2. View Patient Details")
    print(f"3. Remove Patient")
    print(f"4. Track Appointment Status")
    print(f"5. Exit")


while True:
    info()

    try:
        customer_choice = input("Enter the choice : ")
        if customer_choice == 1:
            try:
                customer_id = int(input("Enter patient ID : "))
                if customer_choice not in hospital:
                    patient_name = input("Enter the patient name : ").title()
                    try:
                        patient_age = int(input(f"Enter {patient_name} age : "))
                    except ValueError:
                        print("Wrong Value")
                    department = input("Enter the Department")
                    appointment_status = input("Enter the status : ").capitalize()
                    try:
                        bill_amount = float(input("Enter the bill amount : "))
                    except ValueError:
                        print("Wrong Value")
            except ValueError:
                print("Wrong Value")


    except ValueError:
        print(f"Wrong Input, Check again")

