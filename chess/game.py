# controls the game loop
# Human vs AI Chess Game

from chess import board

from chess.moves import get_all_moves, make_move
from chess.engine import choose_move




def check_game_over(color):

    moves = get_all_moves(
        board.board,
        color
    )

    if len(moves) == 0:

        print("\nNo legal moves.")

        if color == "w":
            print("AI wins!")
        else:
            print("You win!")

        return True


    return False




def human_turn():

    print("\nYour turn")


    while True:

        start = input("Move from (or quit): ")

        if start.lower() == "quit":
            return False


        end = input("Move to: ")


        if legal_move(
            start,
            end,
            "w"
        ):

            make_move(
                board.board,
                start,
                end
            )


            history.append(
                (start,end)
            )


            return True


        else:

            print(
                "Illegal move. Try again."
            )




def ai_turn():

    print("\nAI thinking...")


    moves = get_all_moves(
        board.board,
        "b"
    )


    if len(moves) == 0:

        return False



    move = choose_move(
        board.board,
        "b",
        moves
    )


    print(
        "AI plays:",
        move[0],
        "->",
        move[1]
    )


    make_move(
        board.board,
        move[0],
        move[1]
    )


    history.append(
        move
    )


    return True




def start_game():


    print(
        "Starting Human vs AI Chess"
    )


    board.print_board(
        board.board
    )



    while True:


        if not human_turn():

            print(
                "Game ended."
            )

            break



        board.print_board(
            board.board
        )


        print_history()



  

        if check_game_over("b"):

            break



     

        if not ai_turn():

            print(
                "AI has no moves."
            )

            break



        board.print_board(
            board.board
        )


   




        if check_game_over("w"):

            break




