from . import Operation
from .View import read_console

def create_console():
    print("\n"+"=-="*20+"\n")
    print("Please enter contact information")
    Name = input("Name\t: ")
    Number = input("Number\t: ")
    Address = input("Address\t: ")
    Email = input("Email\t: ").lower()
    
    Operation.create(Name, Number, Address, Email)
    print("\nCongratulations, your contact has been saved to the contact book.\n")
    read_console()