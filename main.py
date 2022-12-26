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
            case "1": print("Show the contacts")
            case "2": print("Add the contact")
            case "3": print("Update the contact")
            case "4": print("Delete the contact")
            case "5": quit()
            case default:
                print("Sorry, please enter the option correctly!")
                countdown(3)
                continue
        
        yn = input(f"Continue accessing the book? (y/n): ").lower()
        match yn:
            case "y": continue
            case "n": end()