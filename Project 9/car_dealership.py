cars = [
    ["C101", "Toyota", "Fortuner", 2024, 3500000, "Diesel", 3],
    ["C102", "Hyundai", "Creta", 2025, 1500000, "Petrol", 5],
    ["C103", "Tata", "Nexon", 2024, 1200000, "Petrol", 4],
    ["C104", "Mahindra", "Thar", 2025, 1800000, "Diesel", 2],
    ["C105", "Maruti", "Swift", 2025, 800000, "Petrol", 6],
    ["C106", "Honda", "City", 2025, 1400000, "Petrol", 3],
    ["C107", "Kia", "Seltos", 2024, 1600000, "Diesel", 4],
    ["C108", "Volkswagen", "Virtus", 2025, 1700000, "Petrol", 2],
    ["C109", "Skoda", "Slavia", 2024, 1500000, "Petrol", 3],
    ["C110", "MG", "Hector", 2025, 2200000, "Diesel", 2],
]


def display():
    print("\n=== Available Cars ===")
    for car in cars:
        print(f"{car[0]} | {car[1]} {car[2]} | {car[3]} | ₹{car[4]:,} | {car[5]} | Stock: {car[6]}")


def details():
    print(f"Total models: {len(cars)}")
    print(f"Total vehicles in stock: {sum(car[6] for car in cars)}")


def display_brand():
    for car in cars:
        print(f"Brand: {car[1]} | Model: {car[2]}")


def search_car(car_id):
    for car in cars:
        if car[0].lower() == car_id.lower():
            print(f"{car[0]} | {car[1]} {car[2]} | {car[3]} | ₹{car[4]:,} | {car[5]} | Stock: {car[6]}")
            return car
    print("Car ID not found.")
    return None


def main():
    while True:
        print("\n=== Car Dealership ===")
        print("1. Display all cars")
        print("2. Show inventory summary")
        print("3. Display brands and models")
        print("4. Search by car ID")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display()
        elif choice == "2":
            details()
        elif choice == "3":
            display_brand()
        elif choice == "4":
            search_car(input("Enter car ID (e.g. C101): ").strip())
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()
