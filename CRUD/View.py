from . import Operation

def read_console():
    data_file = Operation.read()
    index = "No"
    name = "Name"
    number = "Number"
    address = "Address"
    email = "Email"

    # styling for view database
    # header
    print("_" * 150 + "\n")
    print(f"{index:4}  |   {name:30}    |   {number:20}  |   {address:40}  |   {email:20}")
    print("_" * 150 + "\n")

    # database
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        id = data_break[0]
        name = data_break[1]
        number = data_break[2]
        address = data_break[3]
        email = data_break[4]
        print(f"{index+1:4}  |   {name:.30}    |   {number:.20}  |   {address:.40}  |   {email:19}", end='')

    # footer
    print("_" * 150 )