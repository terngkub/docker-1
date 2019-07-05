import argparse
import sys
from pathlib import Path
import heuristic
import re
from goal import Goal


class Setting:

    def __init__(self):
        self.algorithm = ''
        self.heuristic = ''
        self.file = ''
        self.check_arguments(sys.argv[1:])
        self.start = []
        self.size = 0
        self.puzzle_parsing(self.file)
        self.goal = Goal(self.size)
        self.h = self.choose_heuristic_function()
        self.cost_function = self.create_cost_function()
        self.create_cost_function()
        goal_solvability = self.is_solvable(self.goal.puzzle)
        start_solvability = self.is_solvable(self.start)
        if goal_solvability is False:
            start_solvability = not start_solvability
        if start_solvability is False:
            raise Exception("Error: Puzzle is unsolvable")

    def check_arguments(self, args=None):
        """
        Check the input arguments of the program
            :param args=None: arguments of the program
        """
        possible_algorithms = ['astar', 'greedy', 'uniform']
        possible_heuristics = ['hamming', 'relaxed', 'manhattan', 'linear']
        parser = argparse.ArgumentParser(description='Npuzzle program.')
        parser.add_argument('-A', '--algorithm', help='algorithm',
                            required=False, default='astar')
        parser.add_argument('-H', '--heuristic', help='heuristic function',
                            required=False, default='linear')
        parser.add_argument('-f', '--file', help='input npuzzle file',
                            required=True)
        parser.add_argument('-g', '--graphic', help='graphic',
                            required=False, action='store_true')
        res = parser.parse_args(args)

        if res.algorithm not in possible_algorithms:
            print('Error : Wrong Algorithm !\n\nPossible Algorithm values:')
            for e in possible_algorithms:
                print(e)
            sys.exit(-1)
        if res.heuristic not in possible_heuristics:
            print('Error : Wrong Heuristic !\n\nPossible Heuristic values:')
            for e in possible_heuristics:
                print(e)
            sys.exit(-1)
        if not Path(res.file).is_file():
            raise Exception("Error : File \'{}\' is not a file !"
                            .format(res.file))
        self.algorithm = res.algorithm
        self.heuristic = res.heuristic
        self.file = res.file
        self.graphic = res.graphic

    def puzzle_parsing(self, npuzzle_filename: str):
        """
        docstring here
            :param npuzzle_filename:str: filename for npuzzle file
        """
        with open(npuzzle_filename, 'r') as in_file:
            has_line_nb = False
            for line in in_file:
                line = line.strip()
                if line[0] == '#':
                    continue
                line_split = re.sub(' +', ' ', line).split(' ')
                if len(line_split) == 1:
                    self.size = int(line_split[0])
                    has_line_nb = True
                    break
            if self.size < 3:
                raise Exception("Error : size less than 3")
            if has_line_nb is False:
                raise Exception("Error : could not find size")
            for line in in_file:
                line = line.strip()
                for letter in line:
                    if letter not in "0123456789 \n":
                        raise Exception("Error : \'{}\' wrong character "
                                        "in puzzle line".format(letter))
                line_split = re.sub(' +', ' ', line).split(' ')
                if len(line_split) != self.size:
                    raise Exception("Error : line size differs from the "
                                    "indicated size of puzzle")
                for letter in line_split:
                    self.start.append(int(letter))

    def is_solvable(self, puzzle):
        permutations = 0
        i = 0
        zero_line_nb = 0
        for curr_tile in puzzle:
            for tile in puzzle[i+1:]:
                if curr_tile > tile and tile != 0:
                    permutations += 1
            if curr_tile == 0:
                zero_line_nb = (self.size - 1) - int(i / self.size)
            i += 1
        if self.size % 2 == 0:
            if zero_line_nb % 2 == 0:
                if permutations % 2 == 0:
                    return (False)
            else:
                if permutations % 2 != 0:
                    return (False)
        else:
            if permutations % 2 != 0:
                return (False)
        return (True)

    def choose_heuristic_function(self):
        if self.heuristic == 'hamming':
            return (heuristic.hamming)
        elif self.heuristic == 'relaxed':
            return (heuristic.relaxed_adjacency)
        elif self.heuristic == 'manhattan':
            return (heuristic.manhattan)
        elif self.heuristic == 'linear':
            return (heuristic.linear_conflict)

    def create_cost_function(self):
        if self.algorithm == 'astar':
            return (lambda g, puzzle: g + self.h(puzzle, self.goal))
        elif self.algorithm == 'uniform':
            return (lambda g, puzzle: g)
        elif self.algorithm == 'greedy':
            return (lambda g, puzzle: self.h(puzzle, self.goal))
