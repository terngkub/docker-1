import operator


def hamming(puzzle, goal):
    count = -1
    for i, j in zip(puzzle, goal.puzzle):
        if i != j:
            count += 1
    return (count)


def relaxed_adjacency(puzzle, goal):
    count = 0
    tmp = list(puzzle[:])
    goal_zero = goal.puzzle_list.index(0)
    while not tmp == goal.puzzle_list:
        puzzle_zero = tmp.index(0)
        if puzzle_zero == goal_zero:
            index = None
            for idx, (i, j) in enumerate(zip(tmp, goal.puzzle_list)):
                if i != j:
                    index = idx
                    break
            tmp[puzzle_zero], tmp[index] = tmp[index], tmp[puzzle_zero]
        else:
            x = goal.puzzle_list[puzzle_zero]
            x_index = tmp.index(x)
            tmp[puzzle_zero], tmp[x_index] = tmp[x_index], tmp[puzzle_zero]
        count += 1
    return (count)


def manhattan(puzzle, goal):
    distance = 0
    for i, val in enumerate(puzzle):
        if val == 0:
            continue
        row = int(i / goal.size)
        col = i % goal.size
        if goal.hash[val][0] != row:
            distance += abs(row - goal.hash[val][0])
        if goal.hash[val][1] != col:
            distance += abs(col - goal.hash[val][1])
    return (distance)


def get_conflict(puzzle, goal, size):
    count = [0] * size
    conflict = []
    for i in range(size):
        conflict.append([])
    for j in range(1, size):
        if puzzle[j] == 0 or puzzle[j] not in goal:
            continue
        for k in range(j):
            if puzzle[k] == 0 or puzzle[k] not in goal:
                continue
            if goal.index(puzzle[j]) >= goal.index(puzzle[k]):
                continue
            count[j] += 1
            count[k] += 1
            conflict[j].append(k)
            conflict[k].append(j)
    return (count, conflict)


def calculate_lc(puzzle_row, goal_row, size):
    lc = 0
    count, conflict = get_conflict(puzzle_row, goal_row, size)
    sum_count = sum(count)
    while sum_count > 0:
        max_index, _ = max(enumerate(count), key=operator.itemgetter(1))
        sum_count -= count[max_index] * 2
        count[max_index] = 0
        for i in conflict[max_index]:
            count[i] -= 1
        lc += 1
    return (lc)


def generate_rows_cols(puzzle_list, size):
    rows = []
    cols = []
    for i in range(size):
        tmp = puzzle_list[i * size:(i + 1) * size]
        rows.append(tmp)
        tmp = []
        for y in range(size):
            tmp.append(puzzle_list[i + (y * size)])
        cols.append(tmp)
    return rows, cols


def linear_conflict(puzzle, goal):
    rows, cols = generate_rows_cols(puzzle, goal.size)
    total_lc = 0
    for i, row in enumerate(rows):
        total_lc += calculate_lc(row, goal.rows[i], goal.size)
    for i, col in enumerate(cols):
        total_lc += calculate_lc(col, goal.cols[i], goal.size)
    cost = manhattan(puzzle, goal) + total_lc * 2
    return (cost)
