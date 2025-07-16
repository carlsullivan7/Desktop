# DataScenarios.py

# Scenario 1: A restaurant menu with prices for each item
print("\nScenario 1: A restaurant menu with prices for each item")
print("Best Data Structure: Dictionary - because we match food names to their prices.")

menu = {
    "Burger": 8.99,
    "Pizza": 12.50,
    "Fries": 3.99
}

for food, price in menu.items():
    print(f"{food}: ${price}")


# Scenario 2: High scores to an arcade game
print("\nScenario 2: High scores to an arcade game")
print("Best Data Structure: List - because we store a changing list of scores.")

high_scores = [9000, 8500, 7900, 7100]

for score in high_scores:
    print(f"Score: {score}")


# Scenario 3: All of the months of the year
print("\nScenario 3: All of the months of the year")
print("Best Data Structure: Tuple - because months don't change.")

months = ("January", "February", "March", "April")

for month in months:
    print(f"Month: {month}")


# Scenario 4: All the items in your backpack
print("\nScenario 4: All the items in your backpack")
print("Best Data Structure: List - because you can add or remove items anytime.")

backpack = ["Notebook", "Pen", "Charger"]

for item in backpack:
    print(f"Backpack item: {item}")


# Scenario 5: Look up student emails by their names
print("\nScenario 5: Look up student emails by their names")
print("Best Data Structure: Dictionary - so we can search by student name.")

student_emails = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com"
}

for name, email in student_emails.items():
    print(f"{name}: {email}")


# Scenario 6: A shopping cart of groceries
print("\nScenario 6: A shopping cart of groceries")
print("Best Data Structure: Set - because we don’t want duplicate items.")

cart = {"Milk", "Eggs", "Bread"}

for item in cart:
    print(f"Grocery: {item}")


# Scenario 7: A store inventory of Sp5der hoodies and their prices
print("\nScenario 7: A store inventory of Sp5der hoodies and their prices")
print("Best Data Structure: Dictionary - to link hoodie names with their prices.")

sp5der_hoodies = {
    "Sp5der Pink Web Hoodie": 120.00,
    "Sp5der Black OG Hoodie": 150.00,
    "Sp5der Yellow Star Hoodie": 135.50
}

for hoodie, price in sp5der_hoodies.items():
    print(f"{hoodie}: ${price}")
