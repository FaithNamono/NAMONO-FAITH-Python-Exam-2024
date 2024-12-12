# 4a(i)
#Object-Oriented Programming (OOP) is defined as  bundling data and functionality together in reusable units called objects.
# It enables a programmer to bundle data and functionality together in reusable units

# 4b(i)
#A class in OOP is used to create and manage objects.
# A class has attributes yet an object doesn't

# 4(ii)
#A program that counts the occurrences of each word in a given sentence
sentence="python exam"
words=sentence.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word, 0) +1
print(word_count)

# 4(iii)
#A python function that takes two parameters (a and b) and returns their sum
def sum_a_b(a,b):
    sum=a+b
    return sum

#Testing the function with values
a=3
b=4
print("The sum of a and b is",sum_a_b(a,b))

#4(iv)
# A class called car with attributes brand,name and color. 
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
        

myCar= Car("Toyota", "Harrier", "white")
print(myCar.brand, myCar.name, myCar.color)

# 4(v)
# Add a method called start_engine to the car class that prints a message saying the car has started 
#An instance of Car and call the method
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    def start_engine(self):
        print(f"The engine of the car has started.")

car = Car("Toyota", "Harrier", "White")
car.start_engine()

