from math import sqrt


class State:

    def __init__(self, setting, puzzle, parent):
        self.setting = setting
        self.puzzle = puzzle
        self.parent = parent
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        self.cost = self.setting.cost_function(self.g, puzzle)

    def move_piece(self, src, dst):
        if self.parent and self.puzzle[src] == self.parent.puzzle[dst]:
            return (None)
        puzzle = list(self.puzzle)
        puzzle[dst] = puzzle[src]
        puzzle[src] = 0
        state = State(self.setting, tuple(puzzle), self)
        return (state)

    def get_next_state(self):
        i = self.puzzle.index(0)
        row = int(i / self.setting.size)
        col = i % self.setting.size
        next = []
        if row > 0:
            up = self.move_piece(i - self.setting.size, i)
            if up:
                next.append(up)
        if row < self.setting.size - 1:
            down = self.move_piece(i + self.setting.size, i)
            if down:
                next.append(down)
        if col > 0:
            left = self.move_piece(i - 1, i)
            if left:
                next.append(left)
        if col < self.setting.size - 1:
            right = self.move_piece(i + 1, i)
            if right:
                next.append(right)
        return (next)

    def get_path(self):
        path = []
        curr = self
        while curr:
            path.append(curr.puzzle)
            curr = curr.parent
        path.reverse()
        return (path)
