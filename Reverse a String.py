#Input a word or sentence
string=input("Please Enter your own String")

string2 =('')
#Loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe original String: ", string)
print("The reverse String: ",string2)