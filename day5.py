inventory = {}

def add_product():
    pid = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    inventory[pid] = {
        "name": name,
        "price": price,
        "stock": stock
    }
    print("Product added successfully!\n")


def update_product():
    pid = int(input("Enter product ID to update: "))
    if pid in inventory:
        stock = int(input("Enter new stock quantity: "))
        inventory[pid]["stock"] = stock
        print("Stock updated successfully!\n")
    else:
        print("Product not found!\n")


def view_products():
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\n------ INVENTORY ------")
    for pid, details in inventory.items():
        print(f"ID: {pid}")
        print(f"Name: {details['name']}")
        print(f"Price: ₹{details['price']}")
        print(f"Stock: {details['stock']}")
      



while True:
    print("1. Add Product")
    print("2. Update Product Stock")
    print("3. View Products")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        view_products()
    elif choice == "4":
        print("Exiting Inventory System")
        break
    else:
        print("Invalid choice!\n")
