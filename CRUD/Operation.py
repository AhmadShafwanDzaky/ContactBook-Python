from . import Database
from .Util import random_string

def create_first_data():
    Name = input("Name\t: ")
    Number = input("Number\t: ")
    Address = input("Address\t: ")
    Email = input("Email\t: ")

    
    data = Database.TEMPLATE.copy()
    data["id"] = random_string(6)
    data["name"] = Name + Database.TEMPLATE["name"][len(Name):]
    data["number"] = Number + Database.TEMPLATE["number"][len(Number):]
    data["address"] = Address + Database.TEMPLATE["address"][len(Address):]
    data["email"] = Email + Database.TEMPLATE["email"][len(Email):]

    data_str = f'{data["id"]}, {data["name"]}, {data["number"]}, {data["address"]}, {data["email"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Error writing")


def create(Name, Number, Address, Email):
    data = Database.TEMPLATE.copy()
    
    data["id"] = random_string(6)
    data["name"] = Name + Database.TEMPLATE["name"][len(Name):]
    data["number"] = Number + Database.TEMPLATE["number"][len(Number):]
    data["address"] = Address + Database.TEMPLATE["address"][len(Address):]
    data["email"] = Email + Database.TEMPLATE["email"][len(Email):]

    data_str = f'{data["id"]}, {data["name"]}, {data["number"]}, {data["address"]}, {data["email"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Error create data")


def read():
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            return content
    except:
        print("Error reading")
        return False