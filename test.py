class Person:
    def __init__(self,name = 'Hoang',age = 27) -> None:
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.age = age

    def toString(self):
        print(f'{self.name} age is {self.age}')

class People:
    def __init__(self) -> None:
        self.firstPerson = Person()
        name = input("Please enter second person's name: ")
        age = int(input("Please enter second person's age: "))
        self.secondPerson = Person(name, age)