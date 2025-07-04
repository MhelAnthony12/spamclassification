def main(): 
    #User Input and Object Creation
    name = input("Enter your name: ")
    current = 2025
    year = int(input("Enter your birth year: "))
    age = current - year  

    # Create a Person object
    person = Person(name, age)
    
    # Display the person's details
    person.myfunc()


# Class Definition
class Person:
  
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method for calculating age 
    def calculate_age(self, current):
        return current - (2025 - self.age) 

    # Method for Processing Data
    def myfunc(self):
        print("Name:", self.name)
        print("Age:", self.age)


#  Output and Display
if __name__ == "__main__":
    main()
