# PUP Parking Garage Simulation
# Case Study 1 (STACK - LIFO)
# Case Study 2 (QUEUE - FIFO)
# Case Study 3 (Dictionary with Garage and Waiting)

import time
from datetime import datetime
import csv

MAX_CAPACITY = 6  # For the new garage

# Dictionary to store parking data
parking_data = {}

# Import CSV data
csv_path = 'C:/Users/Cherylle/Desktop/parking_lot.csv'
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        plate = row['plate_number'].upper()
        arrival_count = 1 if row['arrival'] else 0
        departure_count = 1 if row['departure'] else 0
        parking_data[plate] = {'arrival': arrival_count, 'departure': departure_count}

print("Dictionary initialized and CSV imported successfully!")

def stack_garage():
    stack = []

    waiting_list = []
    arrivals = 0
    departures = 0

    while True:
        print("\n--- PUP PARKING GARAGE (STACK - LIFO) ---")
        print("A - Arrival")
        print("D - Departure")
        print("S - Show Garage")
        print("E - Exit to Menu")
        print("Loading...")
        time.sleep(1)
        choice = input("Enter choice: ").lower()

        if choice == 'a':
            plate = input("Enter plate number: ").upper()
            if len(stack) < MAX_CAPACITY:
                stack.append(plate)
                arrivals += 1
                print(f"Car {plate} arrived and parked. Total cars: {len(stack)}")
            else:
                waiting_list.append(plate)
                print(f"Garage is FULL! Car {plate} added to waiting list.")

        elif choice == 'd':
            if stack:
                plate = stack.pop()
                departures += 1
                print(f"Car {plate} departed. Total cars: {len(stack)}")
                if waiting_list:
                    next_car = waiting_list.pop(0)
                    stack.append(next_car)
                    print(f"Car {next_car} from waiting list entered the garage.")
            else:
                print("Garage is empty!")

        elif choice == 's':
            print("\nCurrent cars in garage (Top → Bottom):")
            for car in reversed(stack):
                print(f"- {car}")
            print(f"Waiting list: {waiting_list}")
            print(f"Total arrivals: {arrivals}, Total departures: {departures}")

        elif choice == 'e':
            break
        else:
            print("Invalid choice! Try again.")


def queue_garage():
    queue = []
    waiting_list = []
    arrivals = 0
    departures = 0

    while True:
        print("\n--- PUP PARKING GARAGE (QUEUE - FIFO) ---")
        print("A - Arrival")
        print("D - Departure")
        print("S - Show Garage")
        print("E - Exit to Menu")
        print("Loading...")
        time.sleep(1)
        choice = input("Enter choice: ").lower()

        if choice == 'a':
            plate = input("Enter plate number: ").upper()
            if len(queue) < MAX_CAPACITY:
                queue.append(plate)
                arrivals += 1
                print(f"Car {plate} arrived and parked. Total cars: {len(queue)}")
            else:
                waiting_list.append(plate)
                print(f"Garage is FULL! Car {plate} added to waiting list.")

        elif choice == 'd':
            if queue:
                plate = queue.pop(0)
                departures += 1
                print(f"Car {plate} departed. Total cars: {len(queue)}")
                if waiting_list:
                    next_car = waiting_list.pop(0)
                    queue.append(next_car)
                    print(f"Car {next_car} from waiting list entered the garage.")
            else:
                print("Garage is empty!")

        elif choice == 's':
            print("\nCurrent cars in garage (Front → Rear):")
            for car in queue:
                print(f"- {car}")
            print(f"Waiting list: {waiting_list}")
            print(f"Total arrivals: {arrivals}, Total departures: {departures}")

        elif choice == 'e':
            break
        else:
            print("Invalid choice! Try again.")


def database_garage():
    global parking_data

    garage = []  # List of plate numbers in garage
    waiting = []  # Waiting list

    while True:
        print("\n--- PUP PARKING GARAGE (DICTIONARY) ---")
        print("A - Arrival")
        print("D - Departure")
        print("G - Get Arrival and Departure")
        print("S - Show Garage")
        print("E - Exit to Menu")
        print("Loading...")
        time.sleep(1)
        choice = input("Enter choice: ").lower()

        if choice == 'a':
            plate = input("Enter plate number: ").upper()
            if len(garage) < MAX_CAPACITY:
                if plate in parking_data:
                    parking_data[plate]['arrival'] += 1
                else:
                    parking_data[plate] = {'arrival': 1, 'departure': 0}
                garage.append(plate)
                print(f"Car {plate} arrived and parked. Total cars: {len(garage)}")
            else:
                waiting.append(plate)
                print(f"Garage is FULL! Car {plate} added to waiting list.")

        elif choice == 'd':
            plate = input("Enter plate number: ").upper()
            if plate in garage:
                index = garage.index(plate)
                parking_data[plate]['departure'] += 1
                if index < len(garage) - 1:
                    # Cars behind need to be shifted
                    for i in range(index + 1, len(garage)):
                        car = garage[i]
                        parking_data[car]['arrival'] += 1
                        parking_data[car]['departure'] += 1
                    garage.pop(index)
                    if waiting:
                        next_car = waiting.pop(0)
                        garage.append(next_car)
                        print(f"Car {next_car} from waiting list entered the garage.")
                    else:
                        pass
                else:
                    garage.pop(index)
                print(f"Car {plate} departed. Total cars: {len(garage)}")
            else:
                print("Car doesn't exist in garage!")

        elif choice == 'g':
            plate = input("Enter plate number: ").upper()
            if plate in parking_data:
                print(f"Plate {plate}: Arrivals: {parking_data[plate]['arrival']}, Departures: {parking_data[plate]['departure']}")
            else:
                print("Car not found!")

        elif choice == 's':
            print("\nCurrent cars in garage:")
            for car in garage:
                print(f"- {car}")
            print(f"Waiting list: {waiting}")

        elif choice == 'e':
            break


# Main Menu
while True:
    print("\n========= PUP PARKING GARAGE SYSTEM =========")
    print("1. Case Study 1 - Simulate Stack (LIFO)")
    print("2. Case Study 2 - Simulate Queue (FIFO)")
    print("3. Case Study 3 - Simulate Dictionary with Garage and Waiting")
    print("4. Exit")
    print("Loading...")
    time.sleep(1)
    option = input("Enter your choice: ")

    if option == '1':
        stack_garage()
    elif option == '2':
        queue_garage()
    elif option == '3':
        database_garage()
    elif option == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
