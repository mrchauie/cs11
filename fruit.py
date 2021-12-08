import random

class Fruit:
    def __init__(self):
        # The instance attributes in Fruit are private!

        # Nobody knows if the fruit has a worm in it!
        self.__hasWorm = random.choice([True, False])

        # Override this! 
        self.__id = None

# Apple inherits from Fruit
class Apple(Fruit):
    def __init__(self, name):

        # Initialize the Apple with all the attributes and methods of Fruit
        super().__init__()

        # This instance attribute is public.
        # It can be accessed everywhere
        self.name = name

        # Override the Fruit id
        self.__id = random.randint(1000,100000)

    # getter / accessor
    def getID(self):
        return self.__id

    # setter / mutator
    def setName(self, name):
        self.name = name

    # Python does not accept method overloading (but other languages like Java does)
    # Python will use the method that is declared the "latest" in the code
    # This setName() will be used and not the previous one
    def setName(self, name, country = 'Canada'):
        self.name = name + " " + country

# Create a new Apple object
a = Apple('Gala')
a.setName('Red delicious')
print(a.name)