# 1 (i)
# A python function named "circle_area" that takes the radius of a circle a sa parameter and returns the 
# area of the circle
def circle_area(radius):
    pi=3.14
    area=pi * (radius ** 2)
    return area
# Test the function with radius 4
radius = 4
print("The area of the circle is:", circle_area(radius))


# 1 (ii)
# A program that finds the sum of all odd numbers and prints the result
num=[4,7,2,9,12,15]
odd_sum = 0
for i in num:
    if i % 2 != 0:
        odd_sum+=i
print('Sum of odd numbers:', odd_sum)

# 1 (iii)
#A python function that takes two numbers as input and returns their sum, difference,product and quotient
def numbers():
    sum = first_number + second_number
    difference = first_number - second_number
    product=first_number * second_number
    quotient =first_number / second_number

    return (sum, difference, product, quotient)
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

print("The sum, difference, product, quotient of the first number and the second number is:",numbers())
  


# 1 (iv)
#Update the value of 'age'to 26 and add a new key-value pair('city','Kampala')
student_info={
    'name':'Alice',
    'age':20,
    'grade':'A'
} 

student_info['age']=26
print(student_info)

student_info['city']='Kampala'
print(student_info)
