# MyCollection.py

class MyCollection:
    def __init__(self):
        self.movies = []
        self.games = []
        self.best_movie = None
        self.best_game = None

    # 1. Show all movies
    def show_movies(self):
        print("My Movies:")
        for m in self.movies:
            print("- " + m)

    # 2. Show all games
    def show_games(self):
        print("My Games:")
        for g in self.games:
            print("- " + g)

    # 3. Add a movie or game
    def add_item(self, kind, name):
        if kind == "movie":
            self.movies.append(name)
        elif kind == "game":
            self.games.append(name)
        else:
            print("Choose 'movie' or 'game'.")

    # 4. Remove a movie or game
    def remove_item(self, kind, name):
        if kind == "movie":
            if name in self.movies:
                self.movies.remove(name)
            else:
                print("Movie not found.")
        elif kind == "game":
            if name in self.games:
                self.games.remove(name)
            else:
                print("Game not found.")
        else:
            print("Choose 'movie' or 'game'.")

    # 5. Set favorite movie or game
    def set_favorite(self, kind, name):
        if kind == "movie":
            if name in self.movies:
                self.best_movie = name
            else:
                print("Movie not in list.")
        elif kind == "game":
            if name in self.games:
                self.best_game = name
            else:
                print("Game not in list.")
        else:
            print("Choose 'movie' or 'game'.")
