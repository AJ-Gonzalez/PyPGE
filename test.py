#!/usr/bin/python3

from tkinter import Tk, Button, Frame, IntVar, Checkbutton, LEFT


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[]):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=LEFT)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


if __name__ == "__main__":
    root = Tk()
    frameX = 10
    frameY = 10
    ls = ['' for i in range(10)]
    lng = Checkbar(root, ls)
    lng.pack()

    def allstates():
        print(list(lng.state()))

    Button(root, text="Quit", command=root.quit).pack()
    Button(root, text="Peek", command=allstates).pack()
    root.mainloop()
