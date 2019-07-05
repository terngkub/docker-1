import tkinter as tk


class Graphic:

    def __init__(self, npuzzle):
        self.size = npuzzle.goal.size
        self.max_num = self.size * self.size - 1
        self.solution = npuzzle.solution.get_path()
        self.complexity_time = npuzzle.complexity_time
        self.complexity_size = npuzzle.complexity_size
        self.total_step = npuzzle.solution.g
        self.curr_step = 0
        self.piece_pixel = 300 / self.size - 10
        self.render()

    def render(self):
        self.add_window()
        self.add_board()
        self.add_pieces()
        self.add_buttons()
        self.add_data()
        self.root.mainloop()

    def add_window(self):
        self.root = tk.Tk()
        self.root.title(str(self.max_num) + " Puzzle")
        self.window = tk.Frame(self.root, padx=50, pady=50)
        self.window.pack()

    def add_board(self):
        container = tk.Frame(self.window)
        container.grid(row=0, column=0, columnspan=3)
        self.board = tk.Frame(container, background='gray30', padx=5, pady=5)
        self.board.pack()

    def add_pieces(self):
        self.pieces = []
        self.labels = []
        for i, val in enumerate(self.solution[self.curr_step]):
            r = int(i / self.size)
            c = i % self.size
            if val == 0:
                self.pieces.append(tk.Frame(self.board,
                                            background='grey30',
                                            width=self.piece_pixel,
                                            height=self.piece_pixel))
                self.pieces[i].grid(row=r, column=c, padx=5, pady=5)
                self.labels.append(tk.Label(self.board,
                                            text="",
                                            background='grey30'))
                self.labels[i].grid(row=r, column=c)
            else:
                self.pieces.append(tk.Frame(self.board,
                                            background='grey80',
                                            width=self.piece_pixel,
                                            height=self.piece_pixel))
                self.pieces[i].grid(row=r, column=c, padx=5, pady=5)
                self.labels.append(tk.Label(self.board,
                                            text=str(val),
                                            background='grey80'))
                self.labels[i].grid(row=r, column=c)

    def add_buttons(self):
        tk.Frame(self.window, height=20).grid(row=1, column=0, columnspan=3)
        tk.Button(self.window, text="prev",
                  command=self.prev, padx=20,
                  pady=10).grid(row=2, column=0, sticky=tk.E)
        self.curr_step_label = tk.Label(self.window, text=str(self.curr_step))
        self.curr_step_label.grid(row=2, column=1)
        tk.Button(self.window, text="next", command=self.next,
                  padx=20, pady=10).grid(row=2, column=2, sticky=tk.W)

    def add_data(self):
        message = "Complexity in time: {}\n".format(self.complexity_time)
        message += "Complexity in size: {}\n".format(self.complexity_size)
        message += "Number of move: {}\n".format(self.total_step)
        tk.Frame(self.window, height=20).grid(row=3, column=0, columnspan=3)
        msg = tk.Message(self.window, width=310, text=message)
        msg.grid(row=4, column=0, columnspan=3, sticky=tk.W)

    def prev(self):
        if self.curr_step == 0:
            return
        self.curr_step -= 1
        self.update_screen()

    def next(self):
        if self.curr_step == self.total_step:
            return
        self.curr_step += 1
        self.update_screen()

    def update_screen(self):
        self.set_pieces()
        self.set_curr_step()
        self.root.update()

    def set_pieces(self):
        for i, val in enumerate(self.solution[self.curr_step]):
            if val == 0:
                self.pieces[i].config(background='grey30')
                self.labels[i].config(text="", background='grey30')
            else:
                self.pieces[i].config(background='grey80')
                self.labels[i].config(text=str(val), background='grey80')

    def set_curr_step(self):
        self.curr_step_label.config(text=str(self.curr_step))
