print("Welcome to Inventory System")

inventory = {
    101: {"name": "Laptop", "price": 55000, "stock": 8},
    102: {"name": "Mouse", "price": 500, "stock": 25},
    103: {"name": "Keyboard", "price": 1200, "stock": 5}
}



print("\nLow Stock Alert:")
for pid, details in inventory.items():
    if details["stock"] <= 10:
        print(f"{details['name']} is LOW in stock ({details['stock']} units)")

print("\nHigh Stock Alert:")
for pid, details in inventory.items():
    if details["stock"] >= 20:
        print(f"{details['name']} has HIGH stock ({details['stock']} units)")
