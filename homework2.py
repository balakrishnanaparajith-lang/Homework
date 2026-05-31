#Question 2. Create a shopping cart program using a Cart class where users can add or remove products stored in dictionaries.
# Use loops, conditionals, functions, and sets to calculate bills and apply discounts.


cart = {}
def add_product():
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    cart[name] = price
    print(f"{name} added to cart.")
def remove_product():
    name = input("Enter product name to remove: ")
    if name in cart:
        del cart[name]
        print(f"{name} removed.")
    else:
        print("Product not found.")
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\n  ")
    for name, price in cart.items():
        print(f"{name} : £{price}")

def calculate_bill():
    total = sum(cart.values())
    if total > 500:
        discount = 0.20
    elif total > 303:
        discount = 0.10
    elif total > 109:
        discount = 0.05
    else:
        discount = 0
    final_amount = total - (total * discount)
    print(f"\nTotal: £{total}")
    print(f"Discount: {discount*100}%")
    print(f"Final Amount: £{final_amount}")
while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Calculate Bill")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        view_cart()
    elif choice == 4:
        calculate_bill()
    elif choice == 5:
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice.")
