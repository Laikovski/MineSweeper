import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False
        self.number = number

    def __repr__(self):
        return f'MyB {self.x} {self.y} - {self.number} - {self.is_mine}'


class MineSweeper:

    window = tk.Tk()
    ROWS = 5
    COLUMNS = 5
    MINES = 5

    def __init__(self):

        self.buttons = []
        count = 1
        for i in range(MineSweeper.ROWS):
            temp = []
            for c in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=c, width=5, height=3, number=count)
                btn.config(command=lambda button = btn: self.click(button))

                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
        else:
            clicked_button.config(text=clicked_button.number, disabledforeground='black')
        clicked_button.config(state='disabled')

    def get_widges(self):
        for i in range(MineSweeper.ROWS):
            for k in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][k]
                btn.grid(row=i, column=k)

    def drow_back(self):
        for i in self.buttons:
            print(i)

    def insert_mine(self):
        index_mine = self.generator_mines()
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_mine:
                    btn.is_mine = True

    def start_programm(self):
        self.insert_mine()
        self.get_widges()
        self.drow_back()

        MineSweeper.window.mainloop()

    @staticmethod
    def generator_mines():
        get_numbers = list(range(1, MineSweeper.ROWS * MineSweeper.COLUMNS + 1))
        shuffle(get_numbers)
        return get_numbers[:MineSweeper.MINES]



game = MineSweeper()

game.start_programm()









