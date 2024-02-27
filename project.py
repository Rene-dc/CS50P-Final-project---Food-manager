import csv
import sys
from tabulate import tabulate
from datetime import date

# Stores all food from CSV at program opening
FOOD = []
HEADERS = ["Food", "Expiry date"]

# number of days before expiry
ALERT_LIMIT = 3

FILE = "food.csv"

def main():
    """
    Food Manager :
    Adds and removes food + expiry date from food csv file
    Alerts when food is about to expire
    """

    help ="""\nhelp -> shows list of commands
show -> displays all food from db + alerts when today - expiry < 5 days and shows expiry date
add -> add food + limit date to db -> reprompts till answer is no or n
remove -> remove food from db -> reprompts till answer is no or n
expiry -> shows food which expiry date is in less than number of days
exit -> saves all food in csv and exits\n"""

    # 1. Welcome user
    welcome()

    # 2. Load data from food.csv
    load_data(FILE)

    # 3. Alert user for food that expires in less than ALERT_LIMIT days
    alert_result = alert(ALERT_LIMIT, FOOD)
    if alert_result != None:
        print(f"\nATTENTION ! These goods will expire in {ALERT_LIMIT} days or less\n\n")
        print(alert_result, "\n")

    # 4. User can manipulate db
    command = what_to_do()
    while command != "exit":
        match command :
            case "help":
                print(help)
            case "show":
                all = print_all(FOOD)
                if all != []:
                    print(all)
                else:
                    print("No food saved")
            case "add":
                add(FOOD)
            case "remove":
                remove(FOOD)
            case "expiry":
                expiry_results = expiry(FOOD)
                if expiry_results != None:
                    print(expiry_results)
                else:
                    print("No food found")

            case _:
                print("\nCommand was not understood. Type 'help' to show list of valid commands\n")
        command = what_to_do()

    # 5. Save data and end program when user types 'exit'
    save_and_exit(FILE, FOOD)


def welcome():
    print("\n-----------------------------------------------------")
    print("\n               Welcome to Food Manager               \n")
    print("-----------------------------------------------------\n")


def load_data(csv_file):
    try:
        with open(csv_file) as file:
            reader = csv.reader(file)
            for row in reader:
                FOOD.append([row[0], row[1]])
    except FileNotFoundError:
        sys.exit("Could not find food.csv")
    return 0


def alert(expiry_delay, data):
    expires_soon_food = []
    for item in data:
        delta = date.fromisoformat(item[1]) - date.today()
        if delta.days <= expiry_delay:
            expires_soon_food.append(item)

    if expires_soon_food != []:
        return tabulate(sorted(expires_soon_food, key=lambda item : date.fromisoformat(item[1])), headers=HEADERS, tablefmt="grid")
    else:
        return None


def print_all(data):
    if data != []:
        return tabulate(sorted(FOOD, key=lambda item : date.fromisoformat(item[1])), headers=HEADERS, tablefmt="grid")
    else:
        return None


def add(data):
    item = input("Add item: ").strip().capitalize()
    while item == "":
        item = input("Add item: ")

    while True:
        try:
            expiry_date = input("Date (YYYY-MM-DD): ")
            _ = date.fromisoformat(expiry_date)
        except ValueError:
            print("date format must be YYYY-MM-DD")
            continue
        break

    data.append([item, expiry_date])


def remove(data):
    print_all(data)
    item_to_remove = input("Remove item: ").strip().capitalize()
    for item in data:
        if item[0] == item_to_remove:
            data.remove(item)
            print(f"{item_to_remove} successfully removed")
            return 0
    print(f"{item_to_remove} was not found")
    return 1


def expiry(data):
    while True:
        try:
            days = int(input("Number of days before expiry: "))
            if days < 1:
                raise ValueError
        except ValueError:
            continue
        break
    return alert(days, data)


def what_to_do():
    return input("What do you wanna do ? ").strip().lower()


def save_and_exit(csv_file, data):
    try:
        with open(csv_file, "w") as f:
            writer = csv.writer(f)
            for row in sorted(data, key=lambda item : date.fromisoformat(item[1])):
                writer.writerow([row[0], row[1]])
    except FileNotFoundError:
        sys.exit(f"Could not write food.csv")

    print("\n-----------------------------------------------------")
    print("\n            Thanks for using Food Manager            ")
    print("                     See you soon !                    \n")
    print("-----------------------------------------------------\n")
    sys.exit()


if __name__ == "__main__":
    main()
