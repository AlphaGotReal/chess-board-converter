import tkinter as tk

class BoundarySetupScreen:
    def __init__(self):
        self.root = tk.Tk()

        # basic config
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="crosshair")
        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.2)

        # key bindings
        self.root.bind("<Escape>", lambda event : self.root.destroy())
        self.root.bind("<ButtonPress-1>", self.handle_start)
        self.root.bind("<B1-Motion>", self.handle_drag)
        self.root.bind("<ButtonRelease-1>", self.handle_end)

        # data holders
        self.start_corner: tuple|None = None
        self.end_corner: tuple|None = None
        self.rectangle = None

    def handle_start(self, event):

        if (self.rectangle is not None):
            self.rectangle.destroy()

        self.start_corner = (event.x, event.y)
        self.rectangle = tk.Frame(self.root, bg="black")
        self.rectangle.place(x=self.start_corner[0], y=self.start_corner[1], width=0, height=0)

    def handle_drag(self, event):

        assert(self.start_corner is not None, "button press it started")
        assert(self.rectangle is not None, "rectangle is not defined")

        width = event.x - self.start_corner[0]
        height = event.y - self.start_corner[1]
        self.rectangle.place(width=abs(width), height=abs(height))
        if width < 0:
            self.rectangle.place(x=event.x)
        if height < 0:
            self.rectangle.place(y=event.y)

    def handle_end(self, event):
        self.end_corner = (event.x, event.y)

    def parse_corners(self):

        assert(self.start_corner is not None, "bruh??")
        assert(self.end_corner is not None, "bruh??")

        top = min(self.start_corner[1], self.end_corner[1])
        left = min(self.start_corner[0], self.end_corner[0])
        width = abs(self.start_corner[0] - self.end_corner[0])
        height = abs(self.start_corner[1] - self.end_corner[1])

        return {
            "top": top,
            "left": left,
            "width": width,
            "height": height
        }

    def run(self):
        self.root.mainloop()


