item = ["pencil", "eraser", "notebook", "ruler", "marker"]
stock_count = [10, 0, 75, 30, 20]

inventory = {item: count for item, count in zip(item, stock_count)}
print("Full Inventory:",inventory)

in_stock_items = {item for item in item if inventory[item] > 0}
print("Items in Stock:", in_stock_items)

choosen_item = input("Which item do you want to buy?")

if choosen_item not in inventory or inventory[choosen_item] == 0:
    print(choosen_item, "is out of stock! Stopping the checker")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price"))

marked_up_prices = list(map(lambda price: price + markup, prices))
print("Marked-up Prices:", marked_up_prices)

item_index = item.index(choosen_item)
choosen_price = marked_up_prices[item_index]
print("The price of", choosen_item, "after markup is:", choosen_price)

inventory[choosen_item] = inventory[choosen_item] - 1
print(choosen_item, "purchased! Remaining stock:", inventory[choosen_item])

print()
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("Item brought ", choosen_item)
print("Price paid ", choosen_price)      
print("Updated Inventory", inventory) 
print("==============================================")