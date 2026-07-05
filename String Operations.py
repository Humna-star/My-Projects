#Input a Word
text = str(input("Enter a String: "))

#Reverse String
#Using Step Values as -1 to iterate in reverse
revText = text[::-1]
text = revText

print("Reverse of given String is:")
print(text)
