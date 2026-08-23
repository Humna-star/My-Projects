valid = False
while not valid:
     #using nested while Loop
    try:
        n=int(input("Enter a number:"))
        #Enter a even number
        while n%2==0:

         print("Buy")
        valid = True
    except  ValueError:
       print("Invalid")