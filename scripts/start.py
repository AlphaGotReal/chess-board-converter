#! /usr/bin/python3

import os
import sys
import cv2

from stockfish import Stockfish

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.vision.setup import BoundarySetupScreen
from utils.vision.screen import LiveScreenRecorder
from utils.chess.board import ChessBoard

def main(args=None):
#     computer = Stockfish(path="/usr/games/stockfish")
#     return computer
    
    setup_screen = BoundarySetupScreen()
    setup_screen.run()
    
    dimensions: dict|None = None
    try:
        dimensions = setup_screen.parse_corners()
    except AssertionError as e:
        print(e)
        return 

    board = ChessBoard()

    recorder = LiveScreenRecorder(dimensions, echo=False)
    for frame in recorder:
        board._test(frame)

if __name__ == "__main__":
    _debug = main(sys.argv)

