BOARD_DIMENSION = 3

def new_board():
    """
    Create and return a new 2D board of size BOARD_DIMENSION x BOARD_DIMENSION (3x3).
    Board initialised with 'None' values corresponding to empty state.

    Returns:
        List of list : 2D list representing the board, each element within it is None

    Example:
        >>> new_board()
        [[None, None, None], [None, None, None], [None, None, None]]
    """ 
    board = []
    for i in range(BOARD_DIMENSION):
            row = [None] * BOARD_DIMENSION
            board.append(row)
    return board


def render(board):
    """
    Render the Tic Tac Toe board with visual seperator that appears on the terminal

    Args:
        Board (list of list) => Tic Tac Toe board to print

    Example: 
        >>> board = new_board()
        >>> board[0][1] = "X"
        >>> board[1][1] = "O"
        >>> render(board)

          | X |  
        ---------
          | O |  
        ---------
          |   |  

    """
    seperator_line = '-' * (BOARD_DIMENSION * 4 + 1)
    print (seperator_line)
    for i, row in enumerate(board):
        print ('| ' + ' | '.join([' ' if cell is None else cell for cell in row]) + ' |')
        print(seperator_line)
    print()

def get_move():
    """
    Prompt player to enter move coordinates

    Returns:
        2 element tuple representing row and column of chosen move

    Example: 
        >>> move = get_move()
        >>> print(f"You chose move: {move}")
        >>> Enter your move (row and column) separated by a space: 
        e.g: 1 2
        
        You chose move: (1, 2)
    """
    while True:
        try:
            move = input("Enter your move (row and column) separated by a space: ").split()
            if len(move) != 2:
                raise ValueError("You must enter exactly two values.")
            row, col = int(move[0]), int(move[1])
            if not (0 <= row < BOARD_DIMENSION and 0 <= col < BOARD_DIMENSION):
                raise ValueError(f"Coordinates must be between 0 and {BOARD_DIMENSION - 1}.")
            return (row, col)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def make_move(player, board, movement):
    """
    Executes move in game by updating board
    Will not print the board, instead updates board and seperately passes updated board into render

    Parameters:
        Player making move
        Board (current state)
        Coordinates of move

    Returns:
        New board with given move added

    Raises:
        ValueError => if move invalid (either out of bounds or cell is occupied)

    Example:
    board = new_board()

    move_coords = (2, 0)
    player = "X"
    board = make_move(player, board, move_coords)
    render(board)

    move_coords_2 = (1, 1)
    board = make_move("O", board, move_coords_2)
    render(board)

    move_coords_2 = (1, 1)
    board = make_move("X", board, move_coords_2)
    render(board)

    
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    | X |   |   |
    -------------

    -------------
    |   |   |   |
    -------------
    |   | O |   |
    -------------
    | X |   |   |
    -------------

    ValueError: Can't make move (1, 1), square already taken.
    """
    if not is_valid_move(board, movement):
        raise ValueError(f"Can't make move {movement}, square already taken.")
    
    row, col = movement
    board[row][col] = player
    return board

def is_valid_move(board, movement):
    """
    Validates move to prevent event of player choosing cell that is already occupied

    Parameters:
        Board => Current state of board
        Movement => Coordinates of move in format (r, c)

    Returns:
        Bool => True if move is valid, otherwise False
    """
    row, col = movement
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] is None
    return False




