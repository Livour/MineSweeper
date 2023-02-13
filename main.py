from tkinter import *

from Cell import Cell
from Field import generate_field, Field

WIDTH = 750
HEIGHT = 750
CELL = 15
ROWS = int(HEIGHT / CELL)
COLUMNS = int(WIDTH / CELL)


def on_key_press(event, field: Field):
    if event.keysym == "Return":
        field.new_game()


def main():
    frame = Tk()
    canvas = Canvas(frame, width=WIDTH, height=HEIGHT)
    canvas.pack()

    field = Field(canvas, ROWS, COLUMNS, CELL)

    frame.bind("<Key>", lambda event: on_key_press(event, field))
    frame.mainloop()


if __name__ == "__main__":
    main()
