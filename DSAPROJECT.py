# PUP Parking Garage Simulation
# Case Study 1 (STACK - LIFO)
# Case Study 2 (QUEUE - FIFO)

import time
from datetime import datetime

MAX_CAPACITY = 10

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


# Main Menu
while True:
    print("\n========= PUP PARKING GARAGE SYSTEM =========")
    print("1. Case Study 1 - Simulate Stack (LIFO)")
    print("2. Case Study 2 - Simulate Queue (FIFO)")
    print("3. Exit")
    print("Loading...")
    time.sleep(1)
    option = input("Enter your choice: ")

    if option == '1':
        stack_garage()
    elif option == '2':
        queue_garage()
    elif option == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
