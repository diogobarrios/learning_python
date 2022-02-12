# Is-A, Has-A, Objetcs and Classes

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Animal has-a name


class Dog(Animal):

    def __init__(self, name):
        self.name = name

# Cat has-a name


class Cat(Animal):

    def __init__(self, name):
        self.name = name

# Person has-a name


class Person(object):

    def __init__(self, name):
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a person


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# Fish is-a object


class Fish(object):
    pass

# Salmon is-a Fish


class Salmon(Fish):
    pass

# Halibut is-a Fish


class Halibut(Fish):
    pass

# rover is-a Dog


rover = Dog("Rover")

# satan = Cat("Satan")


satan = Cat("Satan")

# mary is-a Person


mary = Person("Mary")

# mary has-a pet


mary.pet = satan

# frank is-a employee and has-a salary


frank = Employee("Frank", 120000)

# frank has-a pet


frank.pet = rover

# flipper is a fish


flipper = Fish()

# crouse is a salmon


crouse = Salmon()

# harry is a Halibut


harry = Halibut()
