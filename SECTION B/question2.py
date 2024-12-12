# 2(i)
#Enter the student details and marks from the keyboard
Student_name=input("Enter your name: ")
Student_number=input("Enter your number: ")
Programming=int(input("Enter your programming marks: "))
Data_science=int(input("Enter your data science marks: "))
Computer_applications=int(input("Enter your computer applications marks: "))

Average_mark=(Programming + Data_science + Computer_applications) / 3
print(f"The average mark is {Average_mark:.3f}") 

# 2(ii)
#A program that asks the user for the number of miles Driven and gallons used
milesDriven=float(input("Enter the of Miles Driven: "))
gallonsOfGasUsed=float(input("Enter the gallons of gas used: "))

if gallonsOfGasUsed != 0:
    MPG = milesDriven / gallonsOfGasUsed
    print(f"The car's miles per gallon (MPG) is: {MPG}")


# 2(iii)
#A python program that prints all numbers from 1-100 that are not divisible by 2
for number in range (1,101):
    if number % 2 !=0:
        print(number)


 

