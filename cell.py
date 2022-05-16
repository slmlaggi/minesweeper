import sys
from tkinter import Button, Label
import random
import settings
import ctypes as ct
import time as t


##########################################


class Cell:
    all = []
    cellCount = settings.CELLCOUNT
    cellCountLabelObj = None

##########################################

    def __init__(self, x, y, isMine=False) -> None:
        self.isMine = isMine
        self.isOpened = False
        self.isFlagged = False
        self.cellButton = None
        self.x = x
        self.y = y

        Cell.all.append(self)

##########################################

    def createButton(self, loc):
        button = Button(
            loc,
            width=5,
            height=int(2.5),
        )

        button.bind('<Button-1>', self.leftClickActions)
        button.bind('<Button-3>', self.rightClickActions)
        self.cellButton = button


##########################################


    @staticmethod
    def createCellCountLabel(loc):
        lbl = Label(
            loc,
            bg=('mediumseagreen'),
            fg=('#5c2b22'),
            text="Cells left: {}".format(Cell.cellCount),
            width=12,
            height=4,
            font=('Lato', 30, "bold")
        )
        Cell.cellCountLabelObj = lbl


##########################################

    def leftClickActions(self, event):
        if self.isMine:
            self.showMine()

        else:
            if self.surroundedCellsMinesLen == 0:
                for cellObj in self.surroundedCells:
                    cellObj.showCell()

            self.showCell()

            if Cell.cellCount == settings.MINESCOUNT:
                ct.windll.user32.MessageBoxW(
                    0, 'Congrats, you won the game!', 'Game over!', 0)
                t.sleep(3)
                sys.exit()

        self.cellButton.unbind('<Button-1>')
        self.cellButton.unbind('<Button-3>')

##########################################

    def rightClickActions(self, event):
        if not self.isFlagged:
            self.cellButton.configure(
                bg='darkorchid'
            )
            self.isFlagged = True
        else:
            self.cellButton.configure(
                bg='SystemButtonFace'
            )
            self.isFlagged = False

    def getCellByAxis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


##########################################


    @property
    def surroundedCells(self):
        cells = [
            self.getCellByAxis(self.x - 1, self.y - 1),
            self.getCellByAxis(self.x - 1, self.y),
            self.getCellByAxis(self.x - 1, self.y + 1),
            self.getCellByAxis(self.x, self.y - 1),
            self.getCellByAxis(self.x, self.y + 1),
            self.getCellByAxis(self.x + 1, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y),
            self.getCellByAxis(self.x + 1, self.y + 1)
        ]

        cells = [
            cell for cell in cells if cell is not None]
        return cells


##########################################


    @property
    def surroundedCellsMinesLen(self):
        i = 0

        for cell in self.surroundedCells:
            if cell.isMine:
                i += 1

        return i


##########################################

    def showCell(self):
        if not self.isOpened:
            Cell.cellCount -= 1
            self.cellButton.configure(
                text=self.surroundedCellsMinesLen)
            if Cell.cellCountLabelObj:
                Cell.cellCountLabelObj.configure(
                    text=f"Cells Left: {Cell.cellCount}")

            self.cellButton.configure(
                bg='SystemButtonFace'
            )
        self.isOpened = True

##########################################

    def showMine(self):
        self.cellButton.configure(bg='red')
        ct.windll.user32.MessageBoxW(
            0, 'You clicked on a mine!', 'Game over!', 0)
        t.sleep(3)
        sys.exit()


##########################################


    @staticmethod
    def randMines():
        pickCell = random.sample(
            Cell.all, settings.MINESCOUNT
        )
        print(pickCell)
        for pickCell in pickCell:
            pickCell.isMine = True


##########################################

    def __repr__(self) -> str:
        return "Cell({}, {})".format(self.x, self.y)


##########################################

"""
    Welp ggs thats the project
    Dam
"""
