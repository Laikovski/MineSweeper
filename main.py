import tkinter as tk


class MyButton(tk.Button):

    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False

    def __repr__(self):
        return f'Mybuuuut {self.x} {self.y}'


class MineSweeper:

    window = tk.Tk()
    ROWS = 5
    COLUMNS = 5

    def __init__(self):

        self.buttons = []
        for i in range(MineSweeper.ROWS):
            temp = []
            for c in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=c, width=5, height=3, font = 'Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def get_widges(self):
        for i in range(MineSweeper.ROWS):
            for k in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][k]
                btn.grid(row=i, column=k)

    def drow_back(self):
        for i in self.buttons:
            print(i)

    def start_programm(self):
        self.drow_back()
        self.get_widges()
        MineSweeper.window.mainloop()


game = MineSweeper()

game.start_programm()









