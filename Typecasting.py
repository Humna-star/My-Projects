#Assigning Different Variables
name = "John"
age = 25
is_student = True
weight = 70.5

#Printing Different Variables and their Data Types
print("Name:", name,)
print("Data Type of Name:", type(name)) #str

print("Age:", age)
print("Data Type of Age:", type(age)) #int

print("is_student:", is_student)
print("Data Type of is_student:", type(is_student)) #bool

print("Weight:", weight)
print("Data Type of Weight:", type(weight)) #float

#Tye Casting to convert the Data Types of Variables
print("\n After Type Casting...")

age= str(age)
print(age)
print("Data Type of Age is:", type(age)) #str

weight = int(weight)
print(weight)
print("Data Type of Weight is:", type(weight)) #int
