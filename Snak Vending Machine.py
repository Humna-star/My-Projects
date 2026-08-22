#Part:1 A Function that works out change and sends it back with return
def calculate_change(paid, price):
    change = paid - price
    return change

#Part:2 Set the snak price and greet the customer
snak_price = 25
print("===== SNAK VINDING MACHINE =====")
print(f"This snak costs ${snak_price} units")
print("Accepted prices are 1, 5, 10, 25\n")

total_interest = 0
coin_inserted = 0

#Part:3 Keep accepting coins to the running total
while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))

    #Part:4 Reject any coins that is not a valid value
    if coin !=1 and coin !=5 and coin !=10 and coin !=25: 
        print("Invalid coin. Please insert a valid coin (1, 5, 10, 25).")
        continue
    
    #Part:5 Add the valid to the running total
    total_interest += coin
    coin_inserted += 1
    print(f"Inserted: {coin}. Total so far: {total_interest} units.")

    #Part:6 Stop asking for coins once enough has been inserted
    if total_interest >= snak_price:
        print("Enough money inserted!\n")
        break

#Part:7 Work out the change using the value returned by calculate_change
change_due = calculate_change(total_interest, snak_price)

print("Dispensing your snak...")

#Part:8 Nothing extra to do when the change is zero
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units.")

#Part:9 Print a short summary of the purchase
print("\n===== PURCHASE SUMMARY =====")
print(f"Snak price: {snak_price}")
print(f"Coins inserted: {coin_inserted}")
print(f"Total paid: {total_interest}")
print(f"Change given: {change_due}")
print("========================================")
print("Thank you for your purchase! Enjoy your snak!")
#End of program