from tkinter import Canvas, Tk

from Field import Field

WIDTH = 750
HEIGHT = 750
CELL = 15
ROWS = HEIGHT // CELL
COLUMNS = WIDTH // CELL

ZOOM_IN_AMOUNT = 1.10
ZOOM_OUT_AMOUNT = 0.90
MIN_ZOOM = 0.8
MAX_ZOOM = 5.0
CURRENT_ZOOM = 1.0


def zoom_out(event, canvas: Canvas):
    global CURRENT_ZOOM
    if CURRENT_ZOOM * ZOOM_OUT_AMOUNT > MIN_ZOOM:
        CURRENT_ZOOM *= ZOOM_OUT_AMOUNT
        canvas.scale("all", event.x, event.y, ZOOM_OUT_AMOUNT, ZOOM_OUT_AMOUNT)


def zoom_in(event, canvas):
    global CURRENT_ZOOM
    if CURRENT_ZOOM * ZOOM_IN_AMOUNT < MAX_ZOOM:
        CURRENT_ZOOM *= ZOOM_IN_AMOUNT
        canvas.scale("all", event.x, event.y, ZOOM_IN_AMOUNT, ZOOM_IN_AMOUNT)


def zoom(event, canvas):
    if event.delta > 0:
        zoom_in(event, canvas)
    elif event.delta < 0:
        zoom_out(event, canvas)


def on_key_press(event, field: Field):
    if event.keysym == "Return":
        field.new_game()


def main():
    frame = Tk()
    canvas = Canvas(frame, width=WIDTH, height=HEIGHT)
    canvas.pack()

    field = Field(canvas, ROWS, COLUMNS, CELL)

    frame.bind("<Key>", lambda event: on_key_press(event, field))
    frame.bind("<MouseWheel>", lambda event: zoom(event, canvas))
    frame.mainloop()


if __name__ == "__main__":
    main()
