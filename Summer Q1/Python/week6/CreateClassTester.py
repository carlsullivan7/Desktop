# test_my_collection.py

from MyCollection import MyCollection  # Make sure the filename is MyCollection.py

# Create a collection object
my_stuff = MyCollection()

# Add movies and games
my_stuff.add_item("movie", "Black Panther")
my_stuff.add_item("movie", "The Batman")
my_stuff.add_item("game", "Madden NFL 24")
my_stuff.add_item("game", "Spider-Man 2")

# Show all items
print("\n--- Movies ---")
my_stuff.show_movies()

print("\n--- Games ---")
my_stuff.show_games()

# Set favorite movie and game
my_stuff.set_favorite("movie", "The Batman")
my_stuff.set_favorite("game", "Spider-Man 2")

# Remove one movie and one game
my_stuff.remove_item("movie", "Black Panther")
my_stuff.remove_item("game", "Madden NFL 24")

# Show updated lists
print("\n--- Updated Movies ---")
my_stuff.show_movies()

print("\n--- Updated Games ---")
my_stuff.show_games()

# Show favorite picks
print("\n--- Favorites ---")
print("Favorite Movie:", my_stuff.best_movie)
print("Favorite Game:", my_stuff.best_game)
