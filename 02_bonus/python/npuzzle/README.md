[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/fxbabin/npuzzle.png)](https://travis-ci.org/fxbabin/npuzzle)

# npuzzle

Npuzzle is a 42 project where you have to propose a solver for any npuzzle (most known npuzzles are 8-puzzles and 15-puzzles). This project was realized with [terngkub](https://github.com/terngkub).

The npuzzle is a game consisting in moving a blank tile in order to reorder all the tiles of the puzzle. The order wanted at the end is called the goal and it can change depending on the problem. For the npuzzle project the goal was a spiral version of the basic goal (which is linear).

starting 8-puzzle             |  goal 8-puzzle
:-------------------------:|:-------------------------:
<img src="imgs/start_8puzzle.png" alt="drawing" width="200"/>  |  <img src="imgs/goal_8puzzle.png" alt="drawing" width="200"/>

The program must work on any size. But factually, the program will limited by the memory of the system depending on the algorithm used.

## Usage



Usage:
```
python3 main.py [-A astar|uniform|greedy] [-H hamming|relaxed|manhattan|linear] [-g] -f puzzle_file
```

Examples:
```
python3 main.py -f puzzles/solvable.npuzzle
python3 main.py -A greedy -H hamming -f puzzles/solvable.npuzzle
```
## Output example

<img src="imgs/npuzzle_result.png" alt="drawing" width="400"/>

## Graphical user interface

<img src="imgs/nuzzle_gui.png" alt="drawing" width="400"/>

## Benchmarking

The benchmarking part was done using the time bash command (we used user time as elapsed can vary a lot if other processes are runing at the same time)

### Unsolvable puzzles results (size: 3, 100 occurences)

| average (s) | minimum (s) | maximum (s) | standard deviation (s) |
| -------- | -------------- | ----- | --- |
| 0.0408 | 0.04 | 0.045 | 0.0007 |

### Solvable puzzles results (size: 3, 100 occurences)

#### A*
 Heuristic | average (s) | minimum (s) | maximum (s) | standard deviation (s) |
| --------- | ----------- | ----------- | ----------- | ---------------------- |
| hamming   | 0.1205 | 0.041 | 0.848 | 0.1298 |
| relaxed adjency | 0.1201 | 0.041 | 1.082 | 0.1647 |
| manhattan | 0.1402 | 0.041 | 0.182 | 0.0193 |
| linear conflict | 0.0522 | 0.041 | 0.227 | 0.0261 |

#### Greedy
| Heuristic | average (s) | minimum (s) | maximum (s) | standard deviation (s) |
| --------- | ----------- | ----------- | ----------- | ---------------------- |
| hamming | 0.0507 | 0.041 | 0.068 | 0.0057 |
| relaxed adjency | 0.0509 | 0.041 | 0.088 | 0.0072 |
| manhattan | 0.0498 | 0.041 | 0.063 | 0.0048 |
| linear conflict | 0.0445 | 0.041 | 0.05 | 0.002 |

#### uniform cost

| Heuristic | average (s) | minimum (s) | maximum (s) | standard deviation (s) |
| --------- | ----------- | ----------- | ----------- | ---------------------- |
| hamming | 0.456 | 0.042 | 2.242 | 0.4887 |
| relaxed adjency | 0.4415 | 0.042 | 2.14 | 0.4713 |
| manhattan | 0.4392 | 0.041 | 2.174 | 0.4687 |
| linear conflict | 0.4371 | 0.041 | 2.111 | 0.4654 |

## Bonus

3 bonus were done on this project:
- implementation of the linear_conflict heuristic from the original paper (other explanations on internet were not complete enough to implement it correctly)
- benchmarking tool to measure the performances of the algorithms / heuristics
- graphical interface to see all the movements needed to solve the npuzzle

Mark: (121/121)
