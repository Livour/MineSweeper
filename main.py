from tkinter import Canvas, Tk

from Field import Field
from zoom_util import zoom

WIDTH = 750
HEIGHT = 750
CELL = 15
ROWS = HEIGHT // CELL
COLUMNS = WIDTH // CELL


def on_key_press(event, field: Field):
    if event.keysym == "Return":
        field.new_game()


def on_canvas_press(event, canvas: Canvas):
    canvas.scan_mark(event.x, event.y)


def on_canvas_drag(event, canvas: Canvas):
    canvas.scan_dragto(event.x, event.y, gain=1)


def main():
    frame = Tk()
    frame.title("OurSweeper")
    canvas = Canvas(frame, width=WIDTH, height=HEIGHT)
    canvas.pack()

    field = Field(canvas, ROWS, COLUMNS, CELL)

    frame.bind("<Key>", lambda event: on_key_press(event, field))
    frame.bind("<MouseWheel>", lambda event: zoom(event, canvas))
    frame.bind("<ButtonPress-2>", lambda event: on_canvas_press(event, canvas))
    frame.bind("<B2-Motion>", lambda event: on_canvas_drag(event, canvas))
    frame.mainloop()


if __name__ == "__main__":
    main()
