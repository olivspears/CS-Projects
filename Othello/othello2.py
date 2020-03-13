turn = "b"
twoplayer = True
white_pos = []
black_pos = []
white_counter = len(white_pos)
black_counter = len(black_pos)

board = " | A | B | C | D | E | F | G | H |\n1|   |   |   |   |   |   |   |   |\n2|   |   |   |   |   |   |   |   |\n3|   |   |   |   |   |   |   |   |\n4|   |   |   |   |   |   |   |   |\n5|   |   |   |   |   |   |   |   |\n6|   |   |   |   |   |   |   |   |\n7|   |   |   |   |   |   |   |   |\n8|   |   |   |   |   |   |   |   |"
print(board)

print(board[70])

board[155] = "o"
board[159] = "x"
print(board)
