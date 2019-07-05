class Goal:

    def __init__(self, size):
        self.size = size
        self.len = size * size
        self.num = 1
        self.row = 0
        self.col = -1
        self.border_up = 1
        self.border_down = size - 1
        self.border_left = 0
        self.border_right = size - 1
        self.generate_puzzle()
        self.puzzle = tuple(self.puzzle_list)
        self.generate_hash()
        self.rows = []
        self.cols = []
        self.generate_rows_cols()

    def assign_num(self):
        index = self.row * self.size + self.col
        if self.num == self.len:
            self.puzzle_list[index] = 0
            return (True)
        self.puzzle_list[index] = self.num
        self.num += 1
        return (False)

    def move_right(self):
        while self.col < self.border_right:
            self.col += 1
            if self.assign_num():
                return (True)
        self.border_right -= 1
        return (False)

    def move_down(self):
        while self.row < self.border_down:
            self.row += 1
            if self.assign_num():
                return (True)
        self.border_down -= 1
        return (False)

    def move_left(self):
        while self.col > self.border_left:
            self.col -= 1
            if self.assign_num():
                return (True)
        self.border_left += 1
        return (False)

    def move_up(self):
        while self.row > self.border_up:
            self.row -= 1
            if self.assign_num():
                return (True)
        self.border_up += 1
        return (False)

    def generate_puzzle(self):
        self.puzzle_list = [None for i in range(self.len)]
        while True:
            if self.move_right():
                return
            if self.move_down():
                return
            if self.move_left():
                return
            if self.move_up():
                return

    def generate_hash(self):
        self.hash = {}
        for i, val in enumerate(self.puzzle_list):
            self.hash[val] = (int(i / self.size), i % self.size)

    def generate_lc_hash(self):

        self.lc_hash = {}
        for val in self.puzzle_list:
            row = self.hash[val][0]
            col = self.hash[val][1]
            tmp_1 = self.puzzle_list[row * self.size:(row + 1) * self.size]
            tmp_2 = []
            for y in range(self.size):
                tmp_2.append(self.puzzle_list[col + (y * self.size)])
            self.lc_hash[val] = (tmp_1, tmp_2)
            print(self.lc_hash[val])

    def generate_rows_cols(self):
        for i in range(self.size):
            tmp = self.puzzle_list[i * self.size:(i + 1) * self.size]
            self.rows.append(tmp)
        for i in range(self.size):
            tmp = []
            for y in range(self.size):
                tmp.append(self.puzzle_list[i + (y * self.size)])
            self.cols.append(tmp)
