from chess import board
from chess.moves import get_all_moves, make_move
from chess.engine import choose_move

def print_board():
    board.print_board(board.board)



def ai_turn():

    moves = get_all_moves(
        board.board,
        "b"
    )

    move = choose_move(
        board.board,
        "b",
        moves
    )

    print("AI move:", move)

    make_move(
        board.board,
        move[0],
        move[1]
    )



def main():

    print("Robotic Chess Starting")

    print_board()


    while True:

        start = input("Human move from: ")
        end = input("Human move to: ")


        legal = get_all_moves(
            board.board,
            "w"
        )


        if (start,end) not in legal:
            print("Illegal")
            continue


        make_move(
            board.board,
            start,
            end
        )


        print_board()


        ai_turn()


        print_board()



if __name__ == "__main__":
    main()