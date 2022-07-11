class Employee:
    """Raising salary of each Employee"""

    def __init__(self, first_name, last_name, annual_salary='5000'):
        """Initalize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        """Give a raise to employee"""
        years = input("How many years work here?: ")
        update_salary = years * int(annual_salary)
        print(f"Will be raised next year for {update_salary}")
        

               
