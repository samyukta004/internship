inventory = {}

def add_product():
    try:
        pid = int(input("Enter product ID: "))
        if pid in inventory:
            print("Product ID already exists!\n")
            return

        name = input("Enter product name: ").strip()
        if not name:
            print("Product name cannot be empty!\n")
            return

        price = float(input("Enter product price: "))
        if price <= 0:
            print("Price must be greater than zero!\n")
            return

        stock = int(input("Enter stock quantity: "))
        if stock < 0:
            print("Stock cannot be negative!\n")
            return

        inventory[pid] = {
            "name": name,
            "price": price,
            "stock": stock
        }

        print("Product added successfully!\n")

    except ValueError:
        print("Invalid input! Please enter correct data types.\n")


