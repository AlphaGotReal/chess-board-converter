import os
import cv2

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

        self.images: dict = {}

        for img in imgs:
            path = f"{ROOT_DIR}/{img}.png"
            self.images[img] = (path, cv2.imread(path))
            self.images[img][1] = cv2.resize(self.images[img][1], (width//8, height//8))
        
    def _display(self, img):
        path, image = self.images[img]
        cv2.imshow(path, image)
        cv2.waitKey(0)

    def _test(self, frame):
        return 
        # match white rook template 
        cv2.imshow("res", res)
        cv2.waitKey(1)

    def from_screen(self, frame):
        pass


