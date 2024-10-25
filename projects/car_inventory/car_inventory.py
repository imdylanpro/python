# Dylan Nelson
# October 25, 2024
# car_inventory.py

from pathlib import Path
import json

class car:
    """Creates an instance of a car."""

    def __init__(self, make, model, year, sell_price, purchase_price,
                 id_number):
        """Enstantiates a car with the attributes defined by the user."""
        self.make = make
        self.model = model
        self.year = year
        self.sell_price = sell_price
        self.purchase_price = purchase_price
        self.id_number = id_number

def store_in_file(filepath, list_to_store):
    """Stores a car list into a file."""

    storage_string = fetch_from_file(filepath)

    # Create a for loop to access each item in the list of car objects
    for i in list_to_store:
        # storage_string = ''
        attrs = vars(i)
        # Access each item in the car object
        for j in attrs.items():
            storage_string += f'{j}'
        contents = json.dumps(storage_string)
        filepath.write_text(contents)
        # print(storage_string)

def fetch_from_file(filepath):
    """Fetches information from a filepath"""

    contents = filepath.read_text()
    # Checks if the contents are empty and if they are not then loads the .json
    #   information. If empty data is attempted to be loaded a crash happens.
    if contents != '':
        contents = json.loads(contents)
    
    return contents

def define_cars():
    car1 = car("Mazda", "3s", 2007, 5000, 2500, 0)
    car2 = car("GMC", "Sierra", 2017, 10000, 5000, 1)
    car3 = car("Ford", "F150", 2023, 21000, 10000, 2)
    car_list = [car1, car2, car3]
    return car_list

def main_function():
    path = Path(r"C:\DN_Python\projects\python\projects\car_inventory" + 
            r"\data_files\car_inventory.txt")
    
    car_list = define_cars()
    store_in_file(path, car_list)
    contents = fetch_from_file(path)
    print(contents)

if __name__ == "__main__":
    main_function()