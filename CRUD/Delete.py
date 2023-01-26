from . import Operation
from .View import read_console

def delete_console():
    read_console()
    while True:
        selection_delete = int(input("Select the number of contact you want to delete: "))
        contact_data = Operation.read(index=selection_delete)

        if contact_data:
            data_break = contact_data.split(',')
            id = data_break[0]
            Name = data_break[1]
            Number = data_break[2] 
            Address = data_break[3]
            Email =  data_break[4][:-1]
            
            # data want to delete
            print(f"\nList contact data Number {selection_delete}")
            print(f"1. Name\t\t: {Name:.20}")
            print(f"2. Number\t: {Number:.20}")
            print(f"3. Address\t: {Address:.20}")
            print(f"4. Email\t: {Email:.20}")

            yn = input(f"\nAre you sure deleting the selected data? (y/n): ").lower()
            match yn:
                case "y": 
                    Operation.delete(selection_delete)
                    break
                case "n": continue
                case _:
                    print("Sorry, please enter the option correctly!")
        else:
            print("Please enter the number correctly")
    
    print("Congratulations, your selected contact data has been deleted")