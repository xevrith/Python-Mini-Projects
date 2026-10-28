hospital = {}


def show_menu():
    print("\n=== Hospital Management ===")
    print("1. Add Patient")
    print("2. View Patient Details")
    print("3. Remove Patient")
    print("4. Exit")


def add_patient(hospital, patient_id, name, age, department, status, amount, admitted):
    if patient_id in hospital:
        print("A patient with this ID already exists.")
        return

    hospital[patient_id] = {
        "Name": name,
        "Age": age,
        "Department": department,
        "Appointment Status": status,
        "Bill Amount": amount,
        "Is Admitted": admitted,
    }
    print("Patient added successfully.")


def show_detail(hospital, patient_id):
    patient = hospital.get(patient_id)

    if patient is None:
        print("Patient does not exist.")
        return

    print(f"\nPatient ID: {patient_id}")
    for field, value in patient.items():
        print(f"{field}: {value}")


def remove_patient(hospital, patient_id):
    if patient_id not in hospital:
        print("Patient does not exist.")
        return

    del hospital[patient_id]
    print("Patient removed successfully.")


def read_patient_id(prompt):
    try:
        patient_id = int(input(prompt))
        if patient_id <= 0:
            print("Patient ID must be a positive number.")
            return None
        return patient_id
    except ValueError:
        print("Please enter a valid numeric patient ID.")
        return None


def add_patient_from_input():
    patient_id = read_patient_id("Enter patient ID: ")
    if patient_id is None:
        return

    if patient_id in hospital:
        print("A patient with this ID already exists.")
        return

    name = input("Enter patient name: ").strip().title()
    if not name:
        print("Patient name cannot be empty.")
        return

    try:
        age = int(input("Enter patient age: "))
        amount = float(input("Enter bill amount: "))
    except ValueError:
        print("Age must be a whole number and bill amount must be numeric.")
        return

    if age <= 0:
        print("Age must be greater than zero.")
        return
    if amount < 0:
        print("Bill amount cannot be negative.")
        return

    department = input("Enter department: ").strip().title()
    status = input("Enter appointment status: ").strip().capitalize()
    if not department or not status:
        print("Department and appointment status cannot be empty.")
        return

    admitted_input = input("Is the patient admitted? (yes/no): ").strip().lower()
    if admitted_input not in ("yes", "no"):
        print("Please enter yes or no.")
        return

    add_patient(
        hospital,
        patient_id,
        name,
        age,
        department,
        status,
        amount,
        admitted_input == "yes",
    )


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            add_patient_from_input()

        elif choice == 2:
            patient_id = read_patient_id("Enter patient ID to view: ")
            if patient_id is not None:
                show_detail(hospital, patient_id)

        elif choice == 3:
            patient_id = read_patient_id("Enter patient ID to remove: ")
            if patient_id is not None:
                remove_patient(hospital, patient_id)

        elif choice == 4:
            print("Thank you for using the hospital management system.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
