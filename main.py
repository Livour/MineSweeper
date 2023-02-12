from tkinter import *

from Cell import Cell
from Field import generate_field, Field

WIDTH = 750
HEIGHT = 750
CELL = 15
ROWS = int(HEIGHT / CELL)
COLUMNS = int(WIDTH / CELL)


def main():
    frame = Tk()
    canvas = Canvas(frame, width=WIDTH, height=HEIGHT)
    canvas.pack()

    Field(canvas, ROWS, COLUMNS, CELL)

    frame.mainloop()


if __name__ == "__main__":
    main()
