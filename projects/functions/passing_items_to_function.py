# Dylan Nelson
# October 09, 2024
# passing_items_to_function.py

# Define the variables that we will work with
def declarations():
    test_scores = [100, 99, 95, 89, 92, 97, 87, 93]
    return test_scores

# Import a variable and print it.
def import_scores(imported_variable):
    print(imported_variable)

# This statement is just meant to call the functions that we create it is
#   located at the end so that all of the other functions and variables are 
#   defined prior to starting the program.
if __name__ == '__main__':
    thelist = declarations()
    import_scores(thelist)