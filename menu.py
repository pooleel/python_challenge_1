menu = [
    ("Hamburger", 5.50),
    ("Cheeseburger", 6.50),
    ("Hot Dog", 3.75),
    ("Gumbo", 5.00),
    ("Red Beans and Rice", 4.50),
    ("Fries", 2.50),
    ("Salad", 4.00),
    ("Club Sandwich", 6.00),
    ("Cheese Steak", 12.00),
    ("Ice Cream", 3.25)
]

# Print the menu
print("Welcome to the Cajun Food Truck! Here's the menu:\n")
print("No.   Item              Price")
print("--------------------------------")
for i in range(len(menu)):
    print(f"{i+1}.   {menu[i][0]:<15} $ {menu[i][1]:.2f}")
print("\n")

# Initialize variables to track orders and total cost
order_list = []
total_cost = 0

# Start the ordering process
while True:
    # Prompt user for their choice
    try:
        choice = int(input("Enter the number of the item you want to order (1-10, or 0 to finish): "))
        if choice == 0:
            break  # Exit the loop if the user is done ordering
        elif 1 <= choice <= 10:
            quantity = int(input(f"How many {menu[choice-1][0]}s would you like? "))
            if quantity > 0:
                order_list.append((menu[choice-1][0], menu[choice-1][1], quantity))
                total_cost += menu[choice-1][1] * quantity
                print(f"Added {quantity} {menu[choice-1][0]}(s) to your order.\n")
            else:
                print("Invalid quantity. Please enter a positive number.\n")
        else:
            print("Invalid choice. Please choose a number between 1 and 10.\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

# Print the final receipt
print("\nThank you for your order! Here is your receipt:\n")
print("Item              Qty     Price")
print("--------------------------------")
for item, price, quantity in order_list:
    print(f"{item:<15} {quantity:<7} $ {price * quantity:.2f}")
print("--------------------------------")
print(f"Total: $ {total_cost:.2f}")
print("\nHave a great day!")
