# Dylan Nelson
# October 30, 2024
# cake.py

class Cake:
    """Creates an object of a cake."""

    def __init__(self, icing_flavor, cake_flavor, diameter, price):
        """Instantiates the cake object with the attributes of a cake."""
        self.icing_flavor = icing_flavor
        self.cake_flavor = cake_flavor
        self.diameter = diameter
        self.price = price
        self.cake_slices = -1

    def describe_cake(self):
        """Prints out the attributes of the cake back to the user."""
        print(f"The cake is {self.cake_flavor.lower()} flavored. " 
              f"The cake icing is {self.icing_flavor.lower()} flavored. "
              f"The cake is {self.diameter} inches in diameter. "
              f"The cake costs ${self.price}. ")

    def cut_cake(self, cut_slices):
        """Cuts the cake into a number defined by the input."""
        if cut_slices > 1:
            self.cake_slices = cut_slices
            print(f"You cut the cake into {self.cake_slices} pieces.")
        else:
            print("You need to cut the cake into at least 2 slices, no less.")
        
    def eat_cake(self):
        """Eats a piece of the cake, decrementing the amount of slices by 1."""
        if self.cake_slices == -1:
            print("You haven't cut the cake yet!")
        elif self.cake_slices == 0:
            print("The cake is all gone.")
        else:
            self.cake_slices -= 1 
            print(f"You ate a piece of cake, there are {self.cake_slices} "
                  f"pieces left.")
            
if __name__ == "__main__":
    cake1 = Cake("Chocolate", "Strawberry", 2, 5)
    cake1.describe_cake()
    cake1.eat_cake()
    cake1.cut_cake(2)
    cake1.eat_cake()
    cake1.eat_cake()
    cake1.eat_cake()