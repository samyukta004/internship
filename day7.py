
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
            print("Price must be greater than 0!\n")
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
        print("Invalid input! Please enter correct values.\n")


def update_stock():
    try:
        pid = int(input("Enter product ID: "))
        if pid not in inventory:
            print("Product not found!\n")
            return

        stock = int(input("Enter new stock quantity: "))
        if stock < 0:
            print("Stock cannot be negative!\n")
            return

        inventory[pid]["stock"] = stock
        print("Stock updated successfully!\n")

    except ValueError:
        print("Invalid input!\n")


def view_products():
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\n------ INVENTORY ------")
    for pid, d in inventory.items():
        print(f"ID: {pid}")
        print(f"Name: {d['name']}")
        print(f"Price: ₹{d['price']}")
        print(f"Stock: {d['stock']}")
        print("-----------------------")

while True:
   
    print("1. Add Product")
    print("2. Update Stock")
    print("3. View Products")
    print("4. Save Inventory")
    print("5. Load Inventory")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_product()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        view_products()
    elif choice == "4":
        save_inventory()
    elif choice == "5":
        load_inventory()
    elif choice == "6":
        print("Exiting Inventory System. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1–6.\n")