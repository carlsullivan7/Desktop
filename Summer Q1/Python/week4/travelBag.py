# List of items in your room
room_items = ["shirt", "shoes", "ps5", "charger", "laptop"]

# Empty list for your travel bag
travel_bag = []

# Show available items
print("Items in your room:")
for i in range(len(room_items)):
    print(f"{i}: {room_items[i]}")

# Let the user choose items by index
while True:
    choice = input("Enter the index of the item to pack (or 'done' to finish): ")

    if choice == "done":
        break








    if choice.isdigit():
        index = int(choice)
        if 0 <= index < len(room_items):
            item = room_items.pop(index)
            travel_bag.append(item)
            print(f"Packed: {item}")
        else:
            print("Invalid index.")
    else:
        print("Please enter a number or 'done'.")

    # Show remaining items
    print("Remaining items:")
    for i in range(len(room_items)):
        print(f"{i}: {room_items[i]}")

# Create a tuple for the final luggage and empty the travel bag
luggage = tuple(travel_bag)
travel_bag.clear()

# Show final luggage
print("\nYour packed luggage:")
for item in luggage:
    print("-", item)

print("Total items packed:", len(luggage))