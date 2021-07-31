import tkinter as tk
from random import shuffle

colors ={
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'red',
    4: '#00008B'
}

class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=5, height=3, *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_open = False
        self.number = number
        self.count_bomb = 0

    def __repr__(self):
        return f'{self.x}, {self.y}'


class MineSweeper:

    window = tk.Tk()
    ROWS = 10
    COLUMNS = 10
    MINES = 5

    def __init__(self):

        self.buttons = []

        for i in range(MineSweeper.ROWS + 2):
            temp = []
            for j in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button = btn: self.click(button))
                temp.append(btn)

            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.is_open = True
            clicked_button.config(text='*', background='red', disabledforeground='black')
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.is_open = True
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]

        while queue:

            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:

                x, y = cur_btn.x, cur_btn.y

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:

                        if not abs(dx - dy) == 1:
                            continue


                        next_btn = self.buttons[x + dx][y + dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROWS and 1 <= next_btn.y <= \
                                MineSweeper.COLUMNS and next_btn not in queue:
                            print(next_btn)
                            queue.append(next_btn)


    def create_widgets(self):
        for i in range(1, MineSweeper.ROWS + 1):
            for k in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][k]
                btn.grid(row=i, column=k)

    def print_buttons(self):
        for i in range(1, MineSweeper.ROWS + 1):
            for k in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][k]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end ='')
            print('')
    def insert_mine(self):
        index_mine = self.get_mines_places()
        count = 1
        for i in range(1, MineSweeper.ROWS + 1):
            for k in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][k]
                btn.number = count
                if btn.number in index_mine:
                    btn.is_mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.ROWS):
            for k in range(1, MineSweeper.COLUMNS):
                btn = self.buttons[i][k]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][k + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb
    #
    # def open_buttons(self):
    #     for i in range(MineSweeper.ROWS + 2):
    #         for j in range(MineSweeper.COLUMNS + 2):
    #             btn = self.buttons[i][j]
    #             if btn.is_mine:
    #                 btn.config(text='*', background='red', disabledforeground='black')
    #             elif btn.count_bomb in colors:
    #                 btn.config(text=btn.count_bomb, fg=colors[btn.count_bomb], disabledforeground='darkblue')


    def start_programm(self):
        # self.count_mines_in_buttons()

        self.create_widgets()
        self.insert_mine()
        self.count_mines_in_buttons()
        self.print_buttons()
        # self.open_buttons()
        MineSweeper.window.mainloop()

    @staticmethod
    def get_mines_places():
        get_numbers = list(range(1, MineSweeper.ROWS * MineSweeper.COLUMNS + 1))
        shuffle(get_numbers)
        print(get_numbers[:MineSweeper.MINES])

        return get_numbers[:MineSweeper.MINES]



game = MineSweeper()
game.start_programm()









