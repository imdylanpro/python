# Dylan Nelson
# January 08, 2025
# automobile_home_class.py

def main():
    cars()
    homes()   

def cars():
    car1 = Automobile(make='ford', model='f150', year=2020, color='black',
                      vin=12345678, purch_price=10000, list_price=25000,)
    car2 = Automobile(make='mazda', model='3', year=2007, color='white',
                      vin=12345679, purch_price=1000, list_price=5000)
    
    print('car1 Information: ')
    car1.get_car_info_customer()
    print(f'The profit margin for car1 is {car1.calc_profit_margin()}.')

    print('car2 Information: ')
    car2.get_car_info_employee()
    print(f'The profit margin for car2 is {car2.calc_profit_margin()}.')
    
def homes():
    home1 = Home(home_sqrft=3000, yard_sqrft=400, address='123 happy lane',
                 city='los angeles', num_rooms=8, num_bathrooms=4, 
                 purch_price=500000, list_price=2000000)
    home2 = Home(home_sqrft=2500, yard_sqrft=700, address='123 baker street',
                 city='boise', num_rooms=4, num_bathrooms=2, 
                 purch_price=150000, list_price=500000)    

class Automobile():

    def __init__(self, make, model, year, color, vin, purch_price, list_price, 
                 trim='s'):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin
        self.list_price = list_price
        self.purch_price = purch_price
        self.trim = trim

    def calc_profit_margin(self):
        profit = self.list_price - self.purch_price
        return profit
    
    def get_car_info_customer(self):
        '''Prints generic car information for a customer.'''
        print(f'The car is a {self.year} {self.make} {self.model} in '
             f'{self.color} with {self.trim} trim. The listing price is '
             f'{self.list_price}.')
        
    def get_car_info_employee(self):
        '''Prints a more detailed amount of car information for an employee.'''
        print(f'The car is a {self.year} {self.make} {self.model} in '
             f'{self.color} with {self.trim} trim. The VIN number is '
             f'{self.vin}. The listing price is {self.list_price}, the '
             f'purchase price was {self.purch_price}.')

class Home():

    def __init__(self, home_sqrft, yard_sqrft, address, city, num_rooms, 
                 num_bathrooms, list_price, purch_price):
        self.home_sqrft = home_sqrft
        self.yard_sqrft = yard_sqrft
        self.address = address
        self.city = city
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.list_price = list_price
        self.purch_price = purch_price

    def calc_profit_margin(self):
        profit = self.list_price - self.purch_price
        return profit
    
    def report_home_size(self):
        '''Reports the size of the home.'''
        home_size = ''
        if self.num_rooms < 2:
            home_size = 'small'
        elif self.num_rooms < 5:
            home_size = 'medium'
        else:
            home_size = 'large'
        return home_size

if __name__ == '__main__':
    main()