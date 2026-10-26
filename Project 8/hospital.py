hospital = {}

def info():
    print(f"1. Add Patient")
    print(f"2. View Patient Details")
    print(f"3. Remove Patient")
    print(f"4. Exit")

def add_patient(id,name,age,department,status,amount,admit):
    hospital[id] = {"Name":name,"Age":age,"Department":department,"Appoitment Status":status,"Bill Amount":amount,"Is Admitted":admit}

def show_detail(id_num):
    if id_num in hospital:
        for data,details in hospital[id].items():
            print(f"{data} | {details}")
    else:
        print("Patient Not exist")


def remove_patient(id_num):
    if id_num in hospital:
        del hospital[id_num]
        print("Patient Removed Successfully")
    else:
        print("Patient Not exists")


while True:
    info()

    try:
        customer_choice = int(input("Enter the choice : "))
        if customer_choice == 1:
            try:
                customer_id = int(input("Enter patient ID : "))
                if customer_choice not in hospital:
                    patient_name = input("Enter the patient name : ").title()
                    try:
                        patient_age = int(input(f"Enter {patient_name} age : "))
                    except ValueError:
                        print("Wrong Value")
                    patient_department = input("Enter the Department")
                    appointment_status = input("Enter the status : ").capitalize()
                    try:
                        bill_amount = float(input("Enter the bill amount : "))
                    except ValueError:
                        print("Wrong Value")
                    is_admitted = bool(input("Enter the status : (True | False)"))
                    add_patient(customer_id,patient_name,patient_age,patient_department,appointment_status,bill_amount,is_admitted)            
            except ValueError:
                print("Wrong Value")

        elif customer_choice == 2:
            try:
                search_detail = int(input("Enter ID number : "))
                show_detail(search_detail)
            except ValueError:
                print("Wrong Value")

        elif customer_choice == 3:
            try:
                search_detail = int(input("Enter ID number : "))
                remove_patient(search_detail)
            except ValueError:
                print("Wrong Value")

        elif customer_choice == 4:
            print("Thanks for using our service")
            break 

        else:
            print("Wrong Choice, Try Again")
        
    except ValueError:
        print(f"Wrong Input, Check again")

