#move generation & legal check
from chess import board
from chess.board import col_map
 
def _piece_can_reach(board, start_row, start_col, end_row, end_col):

    if board[start_row][start_col] == "_ ":
        return False
    if start_row == end_row and start_col == end_col:
        return False

    if board[end_row][end_col] != "_ " and board[end_row][end_col][0] == board[start_row][start_col][0]:
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
        elif board[end_row][end_col] != "_ ":
            if board[start_row][start_col][0] == "w":
                if start_row - 1 == end_row and (start_col + 1 == end_col or start_col - 1 == end_col):
                    return True
                return False
            else:
                if start_row + 1 == end_row and (start_col + 1 == end_col or start_col - 1 == end_col):
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
        Knight_moves = [
        (start_row + 2, start_col - 1),
        (start_row + 2, start_col + 1),
        (start_row - 2, start_col - 1),
        (start_row - 2, start_col + 1),
        (start_row + 1, start_col - 2),
        (start_row + 1, start_col + 2),
        (start_row - 1, start_col - 2),
        (start_row - 1, start_col + 2),
        ]
 
        if (end_row, end_col) in Knight_moves:
            return True
        return False
    if board[start_row][start_col][1] == "B":
        if abs(start_row - end_row) == abs(start_col - end_col):
            if start_row < end_row and start_col < end_col:
                for i in range(1, end_row - start_row):
                    if board[start_row + i][start_col + i] != "_ ":
                        return False
                return True
            if start_row < end_row and start_col > end_col:
                for i in range(1, end_row - start_row):
                    if board[start_row + i][start_col - i] != "_ ":
                        return False
                return True
            if start_row > end_row and start_col < end_col:
                for i in range(1, start_row - end_row):
                    if board[start_row - i][start_col + i] != "_ ":
                        return False
                return True
            if start_row > end_row and start_col > end_col:
                for i in range(1, start_row - end_row):
                    if board[start_row - i][start_col - i] != "_ ":
                        return False
                return True
        return False
    if board[start_row][start_col][1] == "Q":
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
        if abs(start_row - end_row) == abs(start_col - end_col):
            if start_row < end_row and start_col < end_col:
                for i in range(1, end_row - start_row):
                    if board[start_row + i][start_col + i] != "_ ":
                        return False
                return True
            if start_row < end_row and start_col > end_col:
                for i in range(1, end_row - start_row):
                    if board[start_row + i][start_col - i] != "_ ":
                        return False
                return True
            if start_row > end_row and start_col < end_col:
                for i in range(1, start_row - end_row):
                    if board[start_row - i][start_col + i] != "_ ":
                        return False
                return True
            if start_row > end_row and start_col > end_col:
                for i in range(1, start_row - end_row):
                    if board[start_row - i][start_col - i] != "_ ":
                        return False
                return True
        return False
    if board[start_row][start_col][1] == "K":
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            enemy_king = "b" if board[start_row][start_col][0] == "w" else "w"
            enemy_king += "K"
            for r in range(end_row - 1, end_row + 2):
                for c in range(end_col - 1, end_col + 2):
                    if 0 <= r <= 7 and 0 <= c <= 7:
                        if board[r][c] == enemy_king:
                            return False
            return True
        return False
    return False
def is_in_check(board, color):
    #find the king, then see if any enemy piece can reach it
    king_row, king_col = None, None
    for r in range(8):
        for c in range(8):
            if board[r][c] == color + "K":
                king_row, king_col = r, c
 
    if king_row is None:
        return False
 
    enemy_color = "b" if color == "w" else "w"
    for r in range(8):
        for c in range(8):
            piece = board[r][c]

            if piece[0:1] != enemy_color:
                continue

            if piece[1] == "P":
                if piece[0] == "w":
                    if (king_row, king_col) == (r - 1, c - 1) or (king_row, king_col) == (r - 1, c + 1):
                        return True
                else:
                    if (king_row, king_col) == (r + 1, c - 1) or (king_row, king_col) == (r + 1, c + 1):
                        return True
            else:
                if _piece_can_reach(board, r, c, king_row, king_col):
                    return True
    return False
 
def is_Legal(board, start, end):
    #Converting start to grid points EX: a2 is (6, 0)
    start_col = col_map[start[0]]
    start_row = 8 - int(start[1])
    #Converting end to grid points EX: d4 is (4, 3)
    end_col = col_map[end[0]]
    end_row = 8 - int(end[1])
 
    if not _piece_can_reach(board, start_row, start_col, end_row, end_col):
        return False
 
    #simulate the move and make sure our own king isn't left in check
    mover_color = board[start_row][start_col][0]
    new_board = [row[:] for row in board]
    new_board[end_row][end_col] = new_board[start_row][start_col]
    new_board[start_row][start_col] = "_ "
 
    if is_in_check(new_board, mover_color):
        return False
 
    return True

def make_move(board, start, end):
    start_col = col_map[start[0]]
    start_row = 8 - int(start[1])

    end_col = col_map[end[0]]
    end_row = 8 - int(end[1])

    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = "_ "

    return board

def get_all_moves(board, color):
    moves = []

    files = "abcdefgh"

    for r in range(8):
        for c in range(8):

            piece = board[r][c]

            if piece != "_ " and piece[0] == color:

                start = files[c] + str(8-r)

                for r2 in range(8):
                    for c2 in range(8):

                        end = files[c2] + str(8-r2)

                        if is_Legal(board, start, end):
                            moves.append((start, end))

    return moves


print(get_all_moves(board.board, "w"))