#Take Input from user
rows = int(input("Please Enter the total number of rows: "))
number = 1 #initialize by 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
    for j in range(1, i + 1):
        #display result
        print(number, end=' ')
        number = number + 1 
    print()  # Move to the next line after each row