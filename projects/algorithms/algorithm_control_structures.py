# Dylan Nelson
# October 31, 2024
# algorithm_control_structures.py

def is_even(num_input):
    """Return a true if even, false if odd."""
    result = num_input % 2
    if result == 0:
        is_even_num = True
    else:
        is_even_num = False
    return is_even_num

def add_even_numbers(input_list, input_value):
    """Adds all the values of an input list together and returns the 
    results."""

    print("Adding all even numbers.")
    total = input_value
    for i in input_list:
        if is_even(i):
            value = total
            total = total + i
            print(f"{i} + {value} = {total}")

    return total

def subtract_odd_numbers(input_list, input_value):
    """add all the values of an input list together and minus the odd values, 
    then return the output."""

    print("Subtracting all odd numbers.")
    total = input_value
    for i in input_list:
        if not is_even(i):
            value = total
            total = total - i
            print(f"{value} - {i} = {total}")

    return total

if __name__ == "__main__":
    list1 = [5, 10, -2, -3, 7, 8, 12]
    first_value = add_even_numbers(list1, 0)
    print(subtract_odd_numbers(list1, first_value))