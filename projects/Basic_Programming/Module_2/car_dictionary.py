# Dylan Nelson
# November 21, 2024
# car_dictionary.py

# Here we ask a few questions from the user to collect information about their
#   vehicle. We also type cast the input values to be displayed later.
print('Hi there, we are going to collect some information about your vehicle.')
car_brand = str(input('What is the vehicles brand? '))
car_model = str(input('What is the vehicles model? '))
car_year = int(input('What year is the vehicle? '))
start_odometer = int(input('What is the starting odometer reading? '))
end_odometer = int(input('What is the ending odometer reading? '))
mpg_estimate = float(input('What is the estmated miles per gallon? '))

# Here we actually store the information gathered into a dictionary.
car1 = {
    'brand' : car_brand,
    'model' : car_model,
    'year' : car_year,
    'starting odometer reading' : start_odometer,
    'ending odometer reading' : end_odometer,
    'estimated miles per gallon' : mpg_estimate
}

# Print out the contents of car 1.
print(car1)

# This portion will print out the data types of the values in car1 dictionary.
for k, v in car1.items():
    print(v, end = ' ')
    print(type(v))