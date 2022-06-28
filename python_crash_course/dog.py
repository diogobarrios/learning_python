class Dog:  # capitalized names refer to classes in Pyhon
    """A simple attempt to model a dog."""
    # Within the class, we define the methods:
    # (which outside of classes they are called functions)

    def __init__(self, name, age):
        # init mehod will be called automatically by Python.
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)  # instance 1
your_dog = Dog('Lucy', 3)  # instance 2

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
