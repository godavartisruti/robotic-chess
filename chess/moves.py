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
    if start_row == end_row and start_col == end_col:
        return False

    if board[start_row][start_col][1] == "P":
        if board[end_row][end_col] == "_ ":
            if board[start_row][start_col][0] == "w":
                if start_row - 1 == end_row and start_col == end_col:
                    return True
                if start_row == 6 and start_row - 2 == end_row and start_col == end_col:
                    if board[start_row - 1][start_col] == "_ ":
                        return True
                return False
            else:
                if start_row + 1 == end_row and start_col == end_col:
                    return True
                if start_row == 1 and start_row + 2 == end_row and start_col == end_col:
                    if board[start_row + 1][start_col] == "_ ":
                        return True
                return False
        if board[end_row][end_col] != "_ ":
            if board[start_row][start_col][0] == "w":
                if start_row + 1 == end_row and (start_col + 1 == end_col or start_col - 1 == end_col):
                    return True
                return False
            else:
                if start_row - 1 == end_row and (start_col + 1 == end_col or start_col - 1 == end_col):
                    return True
                return False

    if board[start_row][start_col][1] == "R":
        if start_row == end_row:
            if start_col < end_col:
                for i in range(start_col + 1, end_col):
                    if board[start_row][i] != "_ ":
                        return False
                return True
            else:
                for i in range(end_col + 1, start_col):
                    if board[start_row][i] != "_ ":
                        return False
                return True
        if start_col == end_col:
            if start_row < end_row:
                for i in range(start_row + 1, end_row):
                    if board[i][start_col] != "_ ":
                        return False
                return True
            else:
                for i in range(end_row + 1, start_row):
                    if board[i][start_col] != "_ ":
                        return False
                return True
    if board[start_row][start_col][1] == "N":
        return False
    if board[start_row][start_col][1] == "B":
        return False
    if board[start_row][start_col][1] == "Q":
        return False
    if board[start_row][start_col][1] == "K":
        return False

    return True