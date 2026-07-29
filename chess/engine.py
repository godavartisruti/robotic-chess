# AI chess engine

from chess import board
from chess.board import col_map
import random


piece_values = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
    "K": 100
}



opening_moves = {
    "w": [
        ("e2","e4"),
        ("d2","d4"),
        ("g1","f3"),
        ("c2","c4")
    ],

    "b": [
        ("e7","e5"),
        ("d7","d5"),
        ("g8","f6"),
        ("c7","c5")
    ]
}







def evaluate_board(board):

    score = 0


    for r in range(8):

        for c in range(8):

            piece = board[r][c]


            if piece == "_ ":
                continue


            value = piece_values[piece[1]]


            # material

            if piece[0] == "w":
                score += value

            else:
                score -= value



            

            if piece[1] in piece_bonus:

                bonus = piece_bonus[piece[1]][r][c]

                if piece[0] == "w":
                    score += bonus

                else:
                    score -= bonus



    



    for r,c in center:

        piece = board[r][c]

        if piece != "_ ":

            if piece[0] == "w":
                score += 0.5
            else:
                score -= 0.5



    # development bonus

    for r in range(8):

        for c in range(8):

            piece = board[r][c]

            if piece != "_ ":

                if piece[1] in ["N","B"]:

                    if piece[0] == "w":
                        score += 0.5
                    else:
                        score -= 0.5


    # king safety

    if board[7][4] != "wK":
        score -= 1

    if board[0][4] != "bK":
        score += 1



    return score






def make_test_move(board,move):

    start,end = move


    start_col = col_map[start[0]]
    start_row = 8-int(start[1])


    end_col = col_map[end[0]]
    end_row = 8-int(end[1])


    new_board = [row[:] for row in board]


    new_board[end_row][end_col] = new_board[start_row][start_col]

    new_board[start_row][start_col]="_ "


    return new_board





def piece_is_attacked(board,row,col,enemy_color):

    from moves import _piece_can_reach


    for r in range(8):

        for c in range(8):

            piece = board[r][c]


            if piece!=" _" and piece!=" _ ":

                if piece[0]==enemy_color:

                    if _piece_can_reach(board,r,c,row,col):
                        return True


    return False







def choose_move(board,color,moves):



    possible_openings = []

    for move in moves:

        if move in opening_moves[color]:

            possible_openings.append(move)


    if possible_openings:

        return random.choice(possible_openings)



    best_move=None
    best_score=None



    for move in moves:


        test_board = make_test_move(board,move)


        score = evaluate_board(test_board)



        start,end = move


        end_row = 8-int(end[1])
        end_col = col_map[end[0]]



        captured = board[end_row][end_col]


     

        if captured != "_ ":

            if color=="w":
                score += piece_values[captured[1]]*3

            else:
                score -= piece_values[captured[1]]*3



        

        start_row = 8-int(start[1])
        start_col = col_map[start[0]]

        moving_piece = board[start_row][start_col]


        enemy = "b" if color=="w" else "w"


        if piece_is_attacked(test_board,end_row,end_col,enemy):

            penalty = piece_values[moving_piece[1]]

            if color=="w":
                score -= penalty

            else:
                score += penalty




       

        if color=="w":

            if best_score is None or score>best_score:
                best_score=score
                best_move=move


        else:

            if best_score is None or score<best_score:
                best_score=score
                best_move=move



    return best_move





