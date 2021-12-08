class Student:
    def __init__(self, name, id, gender, height):
        self.name = name
        self.id = id
        self.gender = gender
        self.height = height

    def playgame(self):
        print(f'{self.name} is playing mario')
    

# creates a new student call bob
bob = Student('bob', 1, 'male', 170)
jill = Student('jill', 2, 'female', 155)

bob.playgame()
jill.playgame()