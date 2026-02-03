
# Question 1: Robot Return to Origin

def robot_returns_to_origin(moves):
    # Initialize starting position
    x = 0
    y = 0

    # TODO: Loop through each move and update x, y
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "L":
            x -= 1
        elif move == "R":
            x += 1

    # TODO: Return True if back at origin, False otherwise
    if x == 0 and y == 0:
        return True
    else:
        return False

# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))