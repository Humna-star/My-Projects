#Using a try and except
try:
    number = int(input("Enter a Number: "))
    print("The number entered is", number)
#using value error
except ValueError as ex:
    print("Exception: ", ex)