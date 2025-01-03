import mss
from PIL import Image
import numpy as np
import time

class LiveScreenRecorder:
    def __init__(self, dimensions, echo=True):
        self.echo = echo
        self.dimensions = dimensions
        self.screen_capture = mss.mss()

    def __iter__(self):
        if (self.echo):
            self.prev_time = time.time_ns()
        return self

    def __next__(self):

        if (self.echo):
            now = time.time_ns()
            print(f"FPS = {1e9/(now - self.prev_time)}", end='\r')
            self.prev_time = now

        image = self.screen_capture.grab(self.dimensions)
        frame = np.array(image)
        return frame

