# Assignment Operator (=) 

feild1 = 120
feild2 = 85
feild3 = 150
feild4 = 95
feild5 = 110

# Arithmetic Operator Addition (+)
total = feild1 + feild2 + feild3 + feild4 + feild5

#average = total / 5
# division

average = total / 5

print("Total harvest:", total, "kg")

print("Average per field :", average, "kg")

price_per_kg = 15
#multiplication (*)
earnings = total * price_per_kg
print("Total earnings : Rs.", earnings)

#floor division (//)
bags = total // 25

# modulus (%)
leftover = total % 25

print("Full bags packed :", bags)

print("Leftover grain :", leftover, "kg")

# Comparison Operator (<, >, <=, >=, ==,)
last_year = 500

print("Better than last year? :", total > last_year)

print("At least as good? :", total >= last_year)

print("Same as last year? :", total == last_year)

# use shorthand operators (+=, -=, *=, /=, %=)
total += 50
print("After bonus crop :", total, "kg")
total -= 20
print("After seed reserve :", total, "kg")
