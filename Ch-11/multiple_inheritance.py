# Base class 1
class Father:
    def skills(self):
        print("Father has carpentry skills.")

# Base class 2
class Mother:
    def skills(self):
        print("Mother has cooking skills.")

# Derived class inheriting from both Father and Mother
class Child(Father, Mother):
    def show_skills(self):
        print("The child has skills from both parents.")

# Create an instance of Child
c = Child()

# Call method from the first parent (Father) due to method resolution order (MRO)
c.skills()
