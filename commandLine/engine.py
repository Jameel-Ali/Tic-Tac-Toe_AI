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
    seperator_line = '-' * (BOARD_DIMENSION * 4 - 3)
    for i, row in enumerate(board):
        print (' | '.join([' ' if cell is None else cell for cell in row]))
        if i < BOARD_DIMENSION - 1:
            print(seperator_line)

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

move = get_move()
print(f"You chose move: {move}")