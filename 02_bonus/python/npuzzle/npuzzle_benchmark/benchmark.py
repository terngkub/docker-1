import os
from tqdm import tqdm
import argparse
import sys
import time
import numpy as np
import subprocess


class Benchmark:

    def __init__(self):
        self.occurences = 0
        self.size = 0
        self.iterations = 0
        self.check_arguments(sys.argv[1:])
        self.generate_puzzles()
        self.testing_puzzle(solvable="unsolvable", heuristic="hamming")
        # self.testing_puzzle(solvable="solvable", heuristic="hamming")
        # self.testing_puzzle(solvable="solvable", heuristic="relaxed")
        self.testing_puzzle(solvable="solvable", heuristic="manhattan")
        # self.testing_puzzle(solvable="solvable", heuristic="linear")

    def check_arguments(self, args=None):
        parser = argparse.ArgumentParser(description='Npuzzle benchmarking '
                                                     'program.')
        parser.add_argument('-O', '--occurences', help='occurences of '
                            'solvable/unsolvable npuzzles',
                            required='True', default=5)
        parser.add_argument('-S', '--size', help='npuzzle size',
                            default=5)
        parser.add_argument('-I', '--iterations', help='npuzzle iterations '
                            'for generation', default=100)
        res = parser.parse_args(args)
        self.occurences = int(res.occurences)
        self.size = int(res.size)
        self.iterations = int(res.iterations)

    def generate_puzzles(self):
        os.system("mkdir -p tests")
        print('''
Benchmarking of solvable and unsolvable npuzzles parameters:

    Occurences : '''+str(self.occurences)+'''
    Iterations : '''+str(self.iterations)+'''
    Size : '''+str(self.size)+'''
        ''')
        print("Generating solvable and unsolvable puzzles ...")
        for i in tqdm(range(self.occurences)):
            os.system("python2.7 puzzle_generator.py -s -i " +
                      str(self.iterations)+" "+str(self.size) +
                      " > tests/solvable_"+str(i)+".txt")
            os.system("python2.7 puzzle_generator.py -u -i " +
                      str(self.iterations)+" "+str(self.size) +
                      " > tests/unsolvable_"+str(i)+".txt")

    def testing_puzzle(self, solvable="solvable", heuristic="manhattan"):
        unsolvable_outputs = []
        print("Testing "+solvable+" puzzles for "+heuristic+" heuristic ...")
        for i in tqdm(range(self.occurences)):
            param = "time python ../main.py -H " + heuristic + \
                    " -f tests/"+solvable+"_" + str(i) + ".txt"
            command = subprocess.run([param], shell=True, capture_output=True)
            unsolvable_outputs.append(command)
        unsolvable_times = []
        for elem in unsolvable_outputs:
            time = elem.stderr.split()[-3].decode("utf-8")
            time_split = time.split('m')
            time_out = float(time_split[0]) * 60 + float(time_split[1][:-1])
            unsolvable_times.append(time_out)
        unsolvable_times = np.array(unsolvable_times)
        for elem in unsolvable_outputs:
            if ((elem.stdout[:7]).decode("utf-8") == "Error :" and
                    solvable == "solvable"):
                print(elem.stdout)
        print('''
Results for '''+solvable+''' npuzzles:

    average_time : '''+str(np.around(unsolvable_times.mean(), decimals=4))+''' seconds
    minimum_time : '''+str(np.around(unsolvable_times.min(), decimals=4))+''' seconds
    maximum_time : '''+str(np.around(unsolvable_times.max(), decimals=4))+''' seconds
    standard deviation : '''+str(np.around(unsolvable_times.std(), decimals=4))+''' seconds

        ''')
