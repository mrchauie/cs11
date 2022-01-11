import random

class Fruit:
    def __init__(self):
        self._hasWorm = random.choice([True, False])

    def _isWormed(self):
        return self._hasWorm

class Apple(Fruit):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def _isWormed(self):
        print('DOES THIS APPLE HAVE A WORM>!!??!!>!>!>!!>>!')
        return self._hasWorm

class Grape(Fruit):
    def __init__(self, name, colour, number):

        # Initialize the Grape with all the attributes and methods of Fruit
        super().__init__()
        self.name = name
        self.__colour = colour
        self.__number = number
    
    def getColour(self):
        return self.__colour

class FruitBasket:
    def __init__(self):
        self.__fruits = []
        self.__addFruit()

    def __addFruit(self):
        for i in range(10):
            if random.randint(0,100) < 50:
                self.__fruits.append(Apple('Fuji'))
            else:
                self.__fruits.append(Grape('Kyoho', 'Purple', random.randint(20,50)))

    def getFruits(self):
        return self.__fruits
    
    def getFruitbyIndex(self, index):
        return self.__fruits[index]


fb = FruitBasket()
for index in range(len(fb.getFruits())):
    print(fb.getFruitbyIndex(index).name)
