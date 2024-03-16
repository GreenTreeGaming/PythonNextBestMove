import chess
import chess.engine
import chess.pgn

engine = chess.engine.SimpleEngine.popen_uci("C:/Users/obbys/Downloads/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe")

board = chess.Board()

player_color = chess.BLACK

EVALUATION_TIME = 0.1
MOVE_TIME = 2.0

while not board.is_game_over():
    print("Current position:")
    print(board)

    evaluation = engine.analyse(board, chess.engine.Limit(time=EVALUATION_TIME))
    print(f"Advantage: {evaluation['score']}")

    if board.turn == player_color:
        if player_color == chess.BLACK:
            move_san = input("Enter your move (in SAN format): ")
            try:
                move = board.parse_san(move_san)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Invalid move, please try again.")
                    continue
            except ValueError:
                print("Invalid move, please try again.")
                continue
        else:
            result = engine.play(board, limit=chess.engine.Limit(time=MOVE_TIME))
            best_move = result.move
            print("Stockfish's move:", board.san(best_move))
            board.push(best_move)
    else:
        if player_color == chess.WHITE:
            move_san = input("Enter your opponent's move (in SAN format): ")
            try:
                move = board.parse_san(move_san)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Invalid move, please try again.")
                    continue
            except ValueError:
                print("Invalid move, please try again.")
                continue

        else:
            result = engine.play(board, limit=chess.engine.Limit(time=MOVE_TIME))
            best_move = result.move
            print("Stockfish's move:", board.san(best_move))
            board.push(best_move)

    player_color = not player_color

finalGame = chess.pgn.Game.from_board(board)
with open('output.png', 'a') as the_file:
    print(finalGame, file=the_file, end="\n\n")

engine.quit()
