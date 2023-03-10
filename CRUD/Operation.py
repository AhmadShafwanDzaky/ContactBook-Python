from . import Database
from .Util import random_string
import os

def delete(selection_deleted):
    try:
        with(open(Database.DB_NAME, 'r')) as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == selection_deleted - 1:
                    pass
                else:
                    with open(Database.DB_NAME, 'a', encoding = "utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database error")
    
    os.rename("data_temp.txt",Database.DB_NAME)
    



def update(selection_update,id,Name,Number,Address,Email):
    data = Database.TEMPLATE.copy()
    
    data["id"] = id
    data["name"] = Name + Database.TEMPLATE["name"][len(Name):]
    data["number"] = Number + Database.TEMPLATE["number"][len(Number):]
    data["address"] = Address + Database.TEMPLATE["address"][len(Address):]
    data["email"] = Email + Database.TEMPLATE["email"][len(Email):]

    data_str = f'\n{data["id"]},{data["name"]},{data["number"]},{data["address"]},{data["email"]}'
    data_length = len(data_str)

    try:
        with(open(Database.DB_NAME, 'r+', encoding="utf-8")) as file:
            file.seek(data_length*(selection_update-1))
            file.write(data_str)
    except:
        print("Error update database")

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

    data_str = f'{data["id"]},{data["name"]},{data["number"]},{data["address"]},{data["email"]}\n'
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

    data_str = f'{data["id"]},{data["name"]},{data["number"]},{data["address"]},{data["email"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Error create data")


def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            total_contacts = len(content)
            if "index" in kwargs:
                contact_index = kwargs["index"]-1
                if contact_index < 0 or contact_index > total_contacts:
                    return False
                else:
                    return content[contact_index]
            else:
                return content
    except:
        print("Error reading")
        return False