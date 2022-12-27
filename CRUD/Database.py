from . import Operation

DB_NAME = "contactbook.txt"
TEMPLATE = {
    "id":"XXXX",
    "name":255*" ",
    "number":255*" ",
    "address":255*" ",
    "email":255*" "
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database available, init done.")
    except:
        print("Database not found, please create a new database")
        Operation.create_first_data()