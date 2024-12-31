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
    setup_screen = BoundarySetupScreen()
    setup_screen.run()

    dimensions: dict|None = None
    try:
        dimensions = setup_screen.parse_corners()
    except AssertionError as e:
        print(e)
        return

    if (dimensions is None):
        print("aborted")
        return

    board = ChessBoard(dimensions)

    recorder = LiveScreenRecorder(dimensions, echo=True)
    for frame in recorder:
        fen = board.from_screen(frame)
        # print(fen)

if __name__ == "__main__":
    _debug = main(sys.argv)

