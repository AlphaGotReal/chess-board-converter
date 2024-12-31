import os
import cv2
import numpy as np

class CastlingRights:
    def __init__(self):
        self.white_kingside: bool = True
        self.white_queenside: bool = True
        self.black_kingside: bool = True
        self.black_queenside: bool = True

    def __str__(self):
        fen = ""
        fen += "K" if self.white_kingside else ""
        fen += "Q" if self.white_queenside else ""
        fen += "k" if self.black_kingside else ""
        fen += "q" if self.black_queenside else ""
        return fen

class ChessBoard:
    def __init__(self, dimensions):

        width = dimensions["width"]
        height = dimensions["height"]

        CURR_DIR = os.path.dirname(os.path.abspath(__file__))
        PARENT_DIR = os.path.dirname(CURR_DIR)
        MAIN_DIR = os.path.dirname(PARENT_DIR)
        ROOT_DIR = f"{MAIN_DIR}/pieces"

        # reading all the piece images
        imgs = [
            "wb", "wk", "wn", "wp", "wq", "wr",
            "bb", "bk", "bn", "bp", "bq", "br"
        ]

        self.images: dict = {} # takes token and returns [path, template]

        for img in imgs:
            path = f"{ROOT_DIR}/{img}.png"
            self.images[img] = [path, cv2.imread(path, cv2.IMREAD_UNCHANGED)]
            self.images[img][1] = cv2.resize(self.images[img][1], (width//8, height//8))

        self.castling_rights = CastlingRights()
        self.turn = "w"

    def _display(self, img):
        path, image = self.images[img]
        cv2.imshow(path, image)
        cv2.waitKey(0)

    def from_screen(self, frame, from_white=True):
        board = np.zeros((8, 8), dtype=object)
        for r in range(8):
            for c in range(8):
                best: str = None
                best_score: int = -1
                scores = []
                for token in self.images:
                    img = self.images[token][1]
                    template_height, template_width, _ = img.shape
                    alpha = img[:, :, 3] / 255.0
                    mask = np.uint8(alpha > 0)
                    tile = frame[r * template_height: (r + 1) * template_height,
                                 c * template_width: (c + 1) * template_width]
                    masked_tile = cv2.bitwise_and(tile, tile, mask=mask)

                    score = ((masked_tile[:, :, :3]==img[:, :, :3]).sum()-3*(1-mask).sum())
                    scores.append(score)
                    if (best is None or best_score < score):
                        best = token
                        best_score = score
                        board[r, c] = token
                std = np.std(scores)
                if (std < 100):
                    board[r, c] = "  "

        # convert to fen notation
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

        if not from_white:
            fen = fen[::-1]

        fen += f" {self.turn} {self.castling_rights} - 0 1"

        return fen


