import os
import chess
from stockfish import Stockfish

class Actor:
    def __init__(self, computer=False):
        self.raw_board = None
        self.board = chess.Board()
        self.computer = computer
        self.stockfish = Stockfish('/usr/games/stockfish')
        self.first_time = True
        self.white_view = True
        self.turn = 'w'

    def handle_board(self, board, castling_rights):
        if (self.first_time):
            fen = ""
            for r in range(8):
                count = 0
                for c in range(8):
                    if (board[r, c] == "  "):
                        count += 1
                        continue
                    else:
                        if (count > 0):
                            fen += str(count)
                            count = 0
                        piece = board[r, c][1]
                        if (board[r, c][0] == 'w'):
                            piece = piece.upper()
                        fen += piece
                if (count > 0):
                    fen += str(count)
                fen += "/"
            fen = fen[:-1]

            if not self.white_view:
                fen = fen[::-1]

            fen += f" {self.turn} {castling_rights} - 0 1"
            try:
                self.board.set_fen(fen)
                self.raw_board = board
            except ValueError as e:
                print(e)
                print(f"incorrect fen: {fen}")
                return
            self.first_time = False
            return

        start_square = None
        end_square = None

        for r in range(8):
            for c in range(8):
                if (self.raw_board[r, c] != board[r, c]):
                    if (self.raw_board[r, c] == "  "):
                        start_square = chess.square(c, r)
                    else:
                        end_square = chess.square(c, r)

        if None not in (start_square, end_square):
            print(f"start_square: {start_square}")
            print(f"end_square: {end_square}")

        self.raw_board = board




