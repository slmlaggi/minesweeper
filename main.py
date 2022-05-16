from tkinter import *
import settings
import utils
from cell import Cell


##########################################


root = Tk()
##########################################

# Settings override
root.configure(bg="mediumseagreen")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)
root.state('zoomed')

##########################################

# Frame classes setup
topFrame = Frame(
    root,
    bg="mediumseagreen",
    width=settings.WIDTH,
    height=utils.heightPercent(25)
)

topFrame.place(
    x=0,
    y=0
)

##########################################

gameTitle = Label(
    topFrame,
    bg='mediumseagreen',
    fg='#5c2b22',
    text='Minesweeper',
    font=('Lato', 42, 'Bold')
)

gameTitle.place(
    x=utils.widthPercent(27.27),
    y=0
)

##########################################

leftFrame = Frame(
    root,
    bg="mediumseagreen",
    width=utils.widthPercent(25),
    height=utils.heightPercent(75)
)

leftFrame.place(
    x=0,
    y=utils.heightPercent(25)
)

##########################################

centerFrame = Frame(
    root,
    bg="mediumseagreen",
    width=utils.widthPercent(75),
    height=utils.heightPercent(75)
)

centerFrame.place(
    x=utils.widthPercent(25),
    y=utils.heightPercent(25)
)

##########################################

# Making cells

for x in range(settings.GRIDSIZE):
    for y in range(settings.GRIDSIZE):
        c = Cell(x, y)
        c.createButton(centerFrame)
        c.cellButton.grid(
            column=x,
            row=y
        )

Cell.createCellCountLabel(leftFrame)
Cell.cellCountLabelObj.place(
    x=0,
    y=0
)

Cell.randMines()

##########################################

root.mainloop()
