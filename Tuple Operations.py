#Create a tupple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#create a tuple
print(tuplex)
#tuple are immutable so you cannot add new elements
#using merge of tuple with the + operator you can add an elements and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#count the number of occurrences of items 50 from the tuple
tuplex = (50, 10, 60, 70, 50)
print(tuplex.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 4, 8, 9, 4)
#use tupe [start:stop] the start index is inclusive and the stop index
_slice = tuplex[1:5]
#it's exclusive
print(_slice)
#if the slice index is not defined, is taken from the beg inning of the tiple
_slice = tuplex[:5]
print(_slice)