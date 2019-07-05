import heapq
from state import State


class PriorityQueue:

    def __init__(self):
        self.pq = []
        self.id = 0

    def push(self, s):
        t = (s.cost, self.id, s)
        heapq.heappush(self.pq, t)
        self.id += 1

    def pop(self):
        t = heapq.heappop(self.pq)
        return (t[2])

    def is_empty(self):
        if not self.pq:
            return (True)
        return (False)

    def index(self, s):
        for t in self.pq:
            if s.puzzle == t[2].puzzle:
                return t[2]
        return None
