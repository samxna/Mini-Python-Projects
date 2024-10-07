# Samina Ahmed | 220023354 | 04/2023
# IN0007 Lab 2 Assessment | Q3

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findPerimeter(self):
        a, b, c = self.sides
        Perimeter = a+b+c
        print('The perimeter of the triangle is %0.2f' %Perimeter)       

print("\n")
tri = Triangle() # Create an instance (object) of a triangle class.
tri.inputSides() # Prompting the user to input the sides of triangle.
tri.dispSides() # Displaying the sides of the triangle.
tri.findPerimeter() # Calculate and print the perimeter of the triangle.
print("\n")


