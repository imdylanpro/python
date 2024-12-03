# Dylan Nelson
# November 27, 2024
# tax_bracket_dictionaries.py

'''Calculates the weekly tax witholding for a customer.'''

def main():
    
    # Here the tax rates are defined with a dictionary.
    tax_rates = {
        '< 500' : 10,
        '>= 500 < 1500' : 15,
        '>= 1500 < 2500' : 20,
        '>= 2500' : 30,
                 }
    
    # User input is gathered here and converted into a float value.
    user_income = float(input('What is your weekly income? '))

    # Here the user_income is compared against the values that we defined in 
    #   the dictionary. If elif else because it can reduce the amount of checks
    #   needed.
    if user_income >= 2500:
        user_tax = tax_rates['>= 2500']
    elif user_income >= 1500:
        user_tax = tax_rates['>= 1500 < 2500']
    elif user_income >= 500:
        user_tax = tax_rates['>= 500 < 1500']
    else:
        user_tax = tax_rates['< 500']

    # Calulates the user taxes paid and income after taxes.
    taxes_paid = user_income * (0.01 * user_tax) 
    money_after_taxes = user_income - taxes_paid

    # Print out the users weekly tax rate.
    print(f'Your weekly tax rate for this week is {user_tax}%.')
    # Tells the user exactly how much they paid in taxes and have left. 
    #   Rounding to the 2nd digit. 
    print(f'You paid ${round(taxes_paid, 2)} in taxes, and you have ' 
          f'${round(money_after_taxes, 2)} left.')

if __name__ == '__main__': 
    main()