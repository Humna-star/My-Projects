#Take input
print("Hale Pyramid Pattern of Stars (*)")
n = int(input("Enter the number of rows: "))

#Outer loop to handle number of rows
for i in range(n):
    #Inner loop to handle number of columns
    for j in range(i + 1):
        #display result
        print("*", end="")
    print()  # Move to the next line after each row