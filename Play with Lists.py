L = [4, 5, 1, 2, 9, 7, 10, 8, 3, 6]
print("Original List:", L)
#Variable to store the sum of 
#the list
sum = 0
#Finding the sum 
for i in L:
    sum += i
#divide the total elements by
#number of elements 
avg = sum / len(L)

print("Sum =", sum)
print("average =", avg)

#Sorting the elements of the list
L.sort()
print(L)
#Printing the first element
print("Smallest element is:", L[0])

#Printing the last element
print("Largest element is:", L[-1])
print(L[1:10]) #slice
