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
    ["C110", "MG", "Hector", 2025, 2200000, "Diesel", 2]
]

def display():
    print("=== Car Detail ===")
    for car in cars:
        print(car)


def details():
    print(f"Total Number of Cars Models : {len(cars)}")


def display_brand():
    car_details = [f"Brand : {car[1]} | Model : {car[2]}"for car in cars]
    for car in car_details:
        print(car)


def search_car(car_id):
    if any(car_id in car for car in cars):

        for car in cars.index(car_id):
            print(car)
    else:
        print(f"Car is not available")

print("C101" in cars)
        
