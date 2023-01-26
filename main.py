import os
import time
import CRUD as CRUD

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Try again in", timer, end="\r")
        time.sleep(1)
        t -= 1

def end():
    print("Thank you for accessing the book, see you later")
    quit()

if __name__ == "__main__":
    operation_system = os.name

    match operation_system:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("-----------------------------------\n")
    print("| WELCOME TO JAKI's CONTACT BOOKS |")
    print("\n-----------------------------------")

    print(f"1. Show the contacts")
    print(f"2. Add the contact")
    print(f"3. Update the contact")
    print(f"4. Delete the contact")
    print(f"5. Quit")

    # check the database
    CRUD.init_console()

    while True:
        match operation_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("-----------------------------------\n")
        print("| WELCOME TO JAKI's CONTACT BOOKS |")
        print("\n-----------------------------------")

        print(f"1. Show the contacts")
        print(f"2. Add the contact")
        print(f"3. Update the contact")
        print(f"4. Delete the contact")
        print(f"5. Quit")

        option = input("Please enter a number (1-5) ")
        match option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            case "5": quit()
            case _:
                print("Sorry, please enter the option correctly!")
                countdown(3)
                continue
        while True:
            yn = input(f"Continue accessing the book? (y/n): ").lower()
            match yn:
                case "y": break
                case "n": end()
                case _:
                    print("Sorry, please enter the option correctly!")