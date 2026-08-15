# PART: 1 Define a function wit no arguments to greet the user and explain the purpose of the program
def greet_user():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade made, just for you!")

#PART: 2 Call the greet_user function
greet_user()

PART: 3
price_per_cup = float(input("Enter the price per cup of lemonade: "))
cups_sold = int(input("Enter the number of cups sold: "))

#PART: 4 Define a function that takes arguments and returns the total
def calculate_total(price, cups):
    total = price * cups
    return total

#PART: 5 Call the calculate_total and store the value in ait returns
total_cost = calculate_total(price_per_cup, cups_sold)

#PART: 6 Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Cost: ", rounded_total)

#PART: 7 Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))

#PART: 8 Define a function that takes arguments and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change

#PART: 9 Call the calculate_change function and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

#PART: 10 Define a function that returns a Thank you message based on the change due
def thank_customer(change):
    if change > 0:
        return "WOW! Big Order Thank you for your support! "
    else:
        return "Thanks for stopping by the stand"

#PART: 11 Call the thank_customer function and store the value it returns
closing_message = thank_customer(rounded_change)

#PART: 12 Print the final lemonade stand receipt
print()
print("===============================================================================")
print("===== LEMONADE STAND RECEIPT =====")
print("Price per cup: $", price_per_cup)
print("Cups sold: ", cups_sold)
print("Total Cost: $", rounded_total)
print("Amount Paid: $", amount_paid)
print("Change Due: $", rounded_change)
print(closing_message)
print("===== THANK YOU FOR VISITING THE LEMONADE STAND! =====")
print("===============================================================================")