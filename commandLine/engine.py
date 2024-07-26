


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


# Test [Function Works] : print (new_board())

