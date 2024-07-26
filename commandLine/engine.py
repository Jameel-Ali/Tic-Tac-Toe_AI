BOARD_DIMENSION = 3


def new_board():
    """
    Create and return a new 2D board of size BOARD_DIMENSION x BOARD_DIMENSION (5x5).
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
    Render the Tic Tac Toe board with visual seperators that appear on the terminal

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

