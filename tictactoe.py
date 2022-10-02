
board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

user = True # When true it refers to x

turns = 0

# Iterate throught the board and print it
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()
# Quit the game
def quit(user_input):
    if user_input.lower() == 'q': 
        print("Thanks for playing")
        return True
    else:
        return False
# Check if the input is valid
def check_input(user_input):
    # Check if number
    if not isnum(user_input): return False
    user_input = int(user_input)
    # Check if its 1-9
    if not bounds(user_input): return False
    return True
# Check if the input is a number
def isnum(user_input):
    if not user_input.isnumeric():
        print('This is not a valid number')
        return False
    else:
        return True
# Check if the input is in the right range
def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: 
        return True
# Check if a spot is taken
def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != '_':
        print('This position is already taken.')
        return True
    else:
        return False
# Take the user input and return a column and a row to add to the board
def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)
# Using the coordinates to add to the board
def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user
# Switcht the current user
def current_user(user):
    if user: 
        return 'x'
    else:
        return 'o'
# Check if there is any win in the rows
def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                    complete_row = False
                    break
        if complete_row: 
            return True
    return False
# Check if there is any win in the columns
def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False
# Check if there is any win in the diagonals
def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False
# Check if there is any winner in the rows, columns or diagonals
def iswin(user, board):
    if check_row(user, board):
         return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False
    
# Keep playing until all the spots are taken or there is a winnder
while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please enter a position 1 - 9 or 'q' to quit: ")
    if quit(user_input):
        break

    if not check_input(user_input):
        print('Please try again.')
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)

    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)

    if iswin(active_user, board):
        print(f"{active_user.upper()} Won!")
        break
    turns += 1
    if turns == 9: print('Tie')
    user = not user # Switch player