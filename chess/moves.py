#move generation & legal check
from chess import board


def is_Legal(board, start, end):
    #Converting start to grid points EX: a2 is (6, 0)
    start_col = col_map[start[0]]
    start_row = 8 - int(start[1])
    #Converting end to grid points EX: d4 is (4, 3)
    end_col = col_map[end[0]]
    end_row = 8 - int(end[1])

    if board[start_row][start_col] == "_ ":
        return False
    elif board[end_row][end_col] != "_ ":
        return False
    elif start_row == end_row and start_col == end_col:
        return False

    if board[start_row][start_col][1] == "P":
        return True
    if board[start_row][start_col][1] == "R":
        return True
    if board[start_row][start_col][1] == "N":
        return True
    if board[start_row][start_col][1] == "B":
        return True
    if board[start_row][start_col][1] == "Q":
        return True
    if board[start_row][start_col][1] == "K":
        return True

    return True