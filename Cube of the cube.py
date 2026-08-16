#define function to calculate cube
def cube(num):
    return num*num*num

#define a function which will execute the cube if the user enters a number divisible by 3
def by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False

#display the result
print(by_three(9))
print(by_three(5785543434))