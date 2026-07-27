#chessboard (8x8 grid)
board = [0] * 8

for i in range(len(board)):
    board[i] = ["_ "] * 8

def print_board(board):
    for i, row in enumerate(board):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

white_pieces_map = {
    "wP": [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7)],
    "wN": [(7,1), (7,6)],
    "wB": [(7,2), (7,5)],
    "wR": [(7,0), (7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map = {
    "bP": [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)],
    "bN": [(0,1), (0,6)],
    "bB": [(0,2), (0,5)],
    "bR": [(0,0), (0,7)],
    "bQ": [(0,3)],
    "bK": [(0,4)]
}

col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

def put_pieces(board):
    for pieces in (white_pieces_map, black_pieces_map):
        for piece, squares in pieces.items():
            for x, y in squares:
                board[x][y] = piece

put_pieces(board)
print_board(board)

def move_piece(board, start, end):
    #Converting start to grid points EX: a2 is (6, 0)
    start_col = col_map[start[0]]
    start_row = 8 - int(start[1])
    #Converting end to grid points EX: d4 is (4, 3)
    end_col = col_map[end[0]]
    end_row = 8 - int(end[1])
    #Moving the pieces from the starting point to the ending point
    #Replacing the starting points with an "_"
    piece = board[start_row][start_col]
    board[start_row][start_col] = "_ "
    board[end_row][end_col] = piece

    print_board(board)

move_piece(board, "a2", "d4")
print_board(board)
