grid = new_grid()

loop forever:
# TODO : Establish current players moves
current_player

# current state of grid
render(grid)

# players next move
new_pos = get_move()

# Make the move
make_move(grid, new_pos, current_player)

# Make check of game state
winner = get_winner(board)

# Case : there is a winner
if winner not None:
    print "Winner : %s!" % winner
    break

# Case Tie
if grid_full(grid):
    print "Draw!"
    break


