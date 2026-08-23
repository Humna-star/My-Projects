try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    result = num1 / num2
    print("result is", result)

#Using multiple except blocks for different types of error

except ZeroDivisionError:
    print("Division by Zero is Error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers seprated by comma like this: 1, 2")

except:
    print("Wrong Input.")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")