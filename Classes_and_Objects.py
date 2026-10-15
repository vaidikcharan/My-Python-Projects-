#Student class
#Create a class Student with attributes name and marks. Use __init__() 
#to initialize them and create an object for a student named "Vaidik" with marks = 85.
#Expected output: Vaidik and 85

class student():
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks

    def display(self):
        print(self.name, self.marks)

s1= student("Vaidik", 85)
s2= student("pravesh", 77)

s1.display()
s2.display()

#create a class car with attribute brand. 
#use init to initialize it and and create an object
class car():
    def __init__(self, brand):
        self.brand= brand

c1= car("BMW")
c2= car("Tesla")

print(c1.brand)
print(c2.brand)

#create a class with function for simple calculation.
class calculator():
    def add(self, a, b):
        return  a+b
c= calculator()
print(c.add(5, 10))

#create a class student storing name and then display name and greet them. 
class student():
    def __init__(self, name):
        self.name= name 

    def greet(self):
        print(f"Good Morning,{self.name}")

s= student("Vaidik")
s1= student("Pravesh")
s.greet()

#create a class using inheratance.
class animal():
    def eat(self):
        print("Animal is eating.")

class dog(animal):
    def bark(self):
        print("Dog ig barking.")

d= dog()
d.eat()
d.bark()


#Rectangle class
#Create a class Rectangle with attributes length and breadth.
#Add a method area() that returns the area of the rectangle.
#Example: length = 5, breadth = 4. Output: 20
class rectangle():
    def __init__(self, length, breadth):
        self.length= length
        self.breadth= breadth

    def area(self):
        return self.length * self.breadth


a= rectangle(5, 4)
print(f"Area of Reactangle is: {a.area()}")

#--------------------------------------------------------------
class person:
    def setvalues(self, age, name, weight, gender):
        self.age= age
        self.name= name
        self.weight= weight
        self.gender= gender 

    def showvalues(self):
        pronoun= "he" if self.gender== "Male" else "she"
        print(f"the persons name is {self.name}, {pronoun} is {self.age}, weight is {self.weight}kg.")

p1= person()
p1.setvalues(23, "pravesh", 50, "Male")
p1.showvalues()