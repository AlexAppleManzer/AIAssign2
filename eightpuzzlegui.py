
from tkinter import *
from grid import Grid

class ScrollText:
    # class adapted from dev blog  https://knowpapa.com/scroll-text/'

    count = 0

    def __init__(self, frame):

        # add a frame and put a text area into it
        self.text = Text(frame, width=30)
        self.text.insert(END, "step\tcommand\n")

        # add a vertical scroll bar to the text area
        scroll = Scrollbar(frame)
        self.text.configure(yscrollcommand=scroll.set)

        # pack everything
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)

    def write_text(self, text):
        self.text.configure(state=NORMAL)
        self.text.insert(END, "%d\t" % self.count + text + "\n")
        self.text.configure(state=DISABLED)
        self.count += 1

class EightPuzzleGUI:

    def __init__(self):
        self.root = Tk()
        self.title = Label(self.root, text="Best:    Top 5:", font=("Courier", 30))
        self.title.grid(row=0, column=0, columnspan=2)
        self.mainFrame = Frame(self.root, width=500, height=500, borderwidth=5, relief=RIDGE)
        self.mainFrame.grid(row=1, column=0, rowspan=3, columnspan=2)
        self.rightFrame1 = Frame(self.root, width=100, height=100, borderwidth=5, relief=RIDGE)
        self.rightFrame1.grid(row=0, column=2)
        self.rightFrame2 = Frame(self.root, width=100, height=100, borderwidth=5, relief=RIDGE)
        self.rightFrame2.grid(row=1, column=2)
        self.rightFrame3 = Frame(self.root, width=100, height=100, borderwidth=5, relief=RIDGE)
        self.rightFrame3.grid(row=2, column=2)
        self.rightFrame4 = Frame(self.root, width=100, height=100, borderwidth=5, relief=RIDGE)
        self.rightFrame4.grid(row=3, column=2)
        self.rightFrame5 = Frame(self.root, width=100, height=100, borderwidth=5, relief=RIDGE)
        self.rightFrame5.grid(row=4, column=2)

    def draw_grid(self, grid, frame, size):
        for widget in frame.winfo_children():
            widget.destroy()
        txt = Label(frame, text=str(grid), font=("Courier", size))
        txt.grid(row=0, column=0, sticky=N+E+S+W)

    def draw_moves(self, moves):
        self.rightFrame1.destroy()
        self.rightFrame2.destroy()
        self.rightFrame3.destroy()
        self.rightFrame4.destroy()
        self.rightFrame5.destroy()
        self.rightFrame1 = Frame(self.root)
        self.rightFrame1.grid(row=1, column=2, rowspan=3)
        scrollt = ScrollText(self.rightFrame1)
        for move in moves:
            scrollt.write_text(str(move))


