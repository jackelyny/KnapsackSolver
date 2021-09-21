import copy
import sys

with open(sys.argv[1]) as f:
    first_line = f.readline().strip()  # reading the first line
    fields = first_line.split(' ')  # retrieve the two tokens
    n = int(fields[0])
    capacity = float(fields[1])
    f.seek(0, 0)  # go back to the start of the file
    lines = [line.rstrip() for line in f]  # get rid of /n
    wt = (list(map(float, lines[1].split())))  # converting string to float using map
    values = (list(map(float, lines[2].split())))


def knapsack(n, K, wt, val, j, s):
    if j == n:
        return s
    solution = s
    for k in range(j + 1, n):
        s_copy = copy.deepcopy(s)
        s_copy.append(k)
        if find_wt(wt, s_copy) <= K:
            t = knapsack(n, K, wt, val, k, s_copy)
            if find_val(val, t) > find_val(val, solution):
                solution = t
    return solution


def find_wt(wt, s):
    total_weight = 0
    for i in s:
        total_weight = total_weight + wt[i]
    return total_weight


def find_val(v, s):
    total_value = 0
    for i in s:
        total_value = total_value + v[i]
    return total_value


s = []
j = -1
sol = knapsack(n, capacity, wt, values, j, s)
print("Optimal Knapsack: ", sol)

