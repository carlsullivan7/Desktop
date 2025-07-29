import pgzrun

# Game grid settings
GRID_WIDTH = 14
GRID_HEIGHT = 10
GRID_SIZE = 50

# Window size
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

# Game state
has_key = False

# Map layout (each row must be 14 characters)
MAP = [
    "WWWWWWWWWWWWWW",
    "W     K      W",
    "W WWWW WWWW DW",
    "W W        W W",
    "W W WWWW W W W",
    "W W    W W W W",
    "W WWWW W W W W",
    "W   P  W   W W",
    "W WWWWWWWW W W",
    "WWWWWWWWWWWWWW"
]

# Map validation
assert len(MAP) == GRID_HEIGHT
for row in MAP:
    assert len(row) == GRID_WIDTH, "MAP width mismatch: " + row

# Convert grid (x, y) to screen pixel coordinates
def get_screen_coords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# Setup player
def setup_game():
    global player, player_grid_x, player_grid_y
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if MAP[y][x].upper() == "P":
                player.pos = get_screen_coords(x, y)
                player_grid_x = x
                player_grid_y = y

# Draw floor tiles
def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", get_screen_coords(x, y))

# Draw walls, door (if locked), and key
def draw_scenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            pos = get_screen_coords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D" and not has_key:
                screen.blit("door", pos)
            elif square == "K":
                screen.blit("key", pos)

# Handle movement
def try_move(dx, dy):
    global player_grid_x, player_grid_y, has_key
    new_x = player_grid_x + dx
    new_y = player_grid_y + dy

    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        tile = MAP[new_y][new_x]

        if tile == "W":
            return
        if tile == "D" and not has_key:
            return

        # Move player
        player_grid_x = new_x
        player_grid_y = new_y
        player.pos = get_screen_coords(player_grid_x, player_grid_y)

        # Collect key
        if tile == "K":
            has_key = True
            MAP[new_y] = MAP[new_y][:new_x] + " " + MAP[new_y][new_x + 1:]

# Keyboard controls
def on_key_down(key):
    if key == keys.LEFT or key == keys.A:
        try_move(-1, 0)
    elif key == keys.RIGHT or key == keys.D:
        try_move(1, 0)
    elif key == keys.UP or key == keys.W:
        try_move(0, -1)
    elif key == keys.DOWN or key == keys.S:
        try_move(0, 1)

# Main draw loop
def draw():
    screen.clear()
    draw_background()
    draw_scenery()
    player.draw()

# Setup and run
setup_game()
pgzrun.go()
