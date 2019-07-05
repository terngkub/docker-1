from goal import Goal
from priority_queue import PriorityQueue
from state import State


class NPuzzle:

    def __init__(self, setting):
        self.goal = setting.goal
        self.complexity_time = 0
        self.complexity_size = 1
        self.actual_size = 1
        self.opened = PriorityQueue()
        self.opened.push(State(setting, tuple(setting.start), None))
        self.opened_hash = {}
        self.closed = set()
        if setting.start == self.goal.puzzle_list:
            self.solution = self.opened.pop()
        else:
            self.solution = self.solve()

    def solve(self):
        while not self.opened.is_empty():
            curr = self.opened.pop()
            self.closed.add(curr)
            next = curr.get_next_state()
            self.complexity_time += 1
            self.actual_size += len(next)
            if self.actual_size > self.complexity_size:
                self.complexity_size = self.actual_size
            for s in next:
                if s.puzzle == self.goal.puzzle:
                    return (s)
                if s.puzzle in self.closed:
                    self.actual_size -= 1
                    continue
                if s.puzzle in self.opened_hash:
                    e = self.opened_hash[s.puzzle]
                    if s.g < e.g:
                        s.parent = e.parent
                        s.g = e.g
                        s.cost = e.cost
                    self.actual_size -= 1
                else:
                    self.opened.push(s)
                    self.opened_hash[s.puzzle] = s
        return (None)

    def report(self):
        if self.solution:
            print("Complexity in time:", self.complexity_time)
            print("Complexity in size:", self.complexity_size)
            print("Number of moves:", self.solution.g)
            print("Solution:")
            for step in self.solution.get_path():
                print(step)
        else:
            print("Error : The puzzle is unsolvable")
