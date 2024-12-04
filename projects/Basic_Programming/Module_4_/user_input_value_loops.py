# Dylan Nelson
# December 02, 2024
# user_input_value_loops.py

def main():

    # Create a list that will house the numbers input by the user.
    numbers = []
    for i in range(5):
        user_number = int(input('Please enter a number. '))
        numbers.append(user_number)

    # Calculates the total, average, maximum, and minimum of the numbers.
    total_of_numbers = (numbers[0] + numbers[1] + numbers[2] + numbers[3] 
                        + numbers[4])
    average_of_numbers = (total_of_numbers) / len(numbers)
    maximum_of_numbers = max(numbers)
    minimum_of_numbers = min(numbers)

    # Create a list that will calculate interest for every number within 
    #   "numbers" list. Need to utilize another for loop to iterate the 
    #   interest for each number in the list.
    interest_numbers = []
    for i in range(len(numbers)):
        interest_value = numbers[i] + numbers[i]*0.2
        interest_numbers.append(interest_value)

    # Print out all the calculated results.
    print('Total of all numbers is:', total_of_numbers)
    print('Average of all numbers is:', average_of_numbers)
    print('Maximum of all numbers is:', maximum_of_numbers)
    print('Minimum of all numbers is:', minimum_of_numbers)
    print('List with interest on values is:', interest_numbers)

if __name__ == '__main__': main()