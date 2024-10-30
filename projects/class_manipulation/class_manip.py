# Dylan Nelson
# October 28, 2024
# class_manip.py

"""This program will take a class and store its attributes into a dictionary. 
Allowing the values to be saved and retrieved from a file. Once retrieved the 
values from the dictionary will then be able to be transferred back into a 
version of a class. This porgram will essentially allow for the serialization 
of classes to be stored in files."""

from pathlib import Path

# TODO Create a simple class.
class Dog:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def woof(self):
        print(f"{self.name} says woof!")

# TODO Store the class into a dictionary. Attribute name = keyword, 
#   Attribute value = Value.
def store_class_in_dict(imported_obj_list):
    """Provide a list of objects that are desired to store. Stores the values of a class into a dictionary"""
    print(imported_obj_list)
    # Parse through the contents of the object list
    # for i in imported_obj_list:
    #     # Produces a dictionary of the attributes of the object.
    #     attrs = vars(i)
    #     obj_type = type(i)
    #     num_of_attrs = len(attrs)
    #     print(f"{i} has {attrs} attributes, is a {obj_type}, " 
    #           f"and has {num_of_attrs} number of attributes.")
    # str_attrs = f'{str(attrs)}'
    # print(str_attrs)
    # print(type(str_attrs))
    # print(len(attrs))
    # for i in attrs.items():
        # print(str(i))
        # print(type(i))
        # for t in i:
            # print(type(t))
# TODO Save the class value into a file.

# TODO Retrieve the class values from a file.

# TODO Assign the retrieved values to be the attributes of the class.

if __name__ == "__main__":
    dog1 = Dog('Rex', "Grey")
    dog2 = Dog('Konk', "Gold")
    object_list = [dog1, dog2]
    store_class_in_dict(object_list)