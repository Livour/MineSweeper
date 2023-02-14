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


def main():
    frame = Tk()
    frame.title("OurSweeper")
    canvas = Canvas(frame, width=WIDTH, height=HEIGHT)
    canvas.pack()

    field = Field(canvas, ROWS, COLUMNS, CELL)

    frame.bind("<Key>", lambda event: on_key_press(event, field))
    frame.bind("<MouseWheel>", lambda event: zoom(event, canvas))
    frame.mainloop()


if __name__ == "__main__":
    main()
