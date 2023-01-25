from . import Operation
from .View import read_console

def update_console():
    read_console()
    while True:
        selection_update = int(input("Select the number of contacts you want to udpate: "))
        contact_data = Operation.read(index=selection_update)

        if contact_data:
            break
        else:
            print("Please enter the number correctly")
    
    data_break = contact_data.split(',')
    id = data_break[0]
    Name = data_break[1]
    Number = data_break[2] 
    Address = data_break[3]
    Email =  data_break[4][:-1]

    while True:
        # data want to update
        print(f"\nList contact data Number {selection_update}")
        print(f"1. Name\t\t: {Name:.20}")
        print(f"2. Number\t: {Number:.20}")
        print(f"3. Address\t: {Address:.20}")
        print(f"4. Email\t: {Email:.20}")

        # selection data want to update
        user_option = input("Choose what data you want to update/change[1/2/3/4]: ")
        match user_option:
            case "1":
                Name = input("Name\t\t: ")
            case "2":
                Number = input("Number\t: ")
            case "3":
                Address = input("Address\t: ")
            case "4":
                Email = input("Email\t: ").lower()
            case _:
                print("Please enter a valid Number")

        print(f"\nNew contact data Number {selection_update} after update")
        print(f"1. Name\t\t: {Name:.20}")
        print(f"2. Number\t: {Number:.20}")
        print(f"3. Address\t: {Address:.20}")
        print(f"4. Email\t: {Email:.20}")

        yn = input(f"\nAre you done updating the data? (y/n): ").lower()
        match yn:
            case "y": break
            case "n": continue
            case _:
                print("Sorry, please enter the option correctly!")
    
    Operation.update(selection_update,id,Name,Number,Address,Email)