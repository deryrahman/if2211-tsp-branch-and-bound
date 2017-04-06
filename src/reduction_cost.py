#!/usr/bin/env python
import Queue as Q
import math

import time

from graph import *
from copy import deepcopy


# Convert to inf if reading INF string from file
def to_int(x):
    if x == 'INF':
        return float('inf')
    else:
        return int(x)


# Reduce matrix, and return total reducing
def reducing(matrix):
    reduced = 0
    size = len(matrix)
    # reducing row
    for i in range(size):
        min_row = min(float(col) for col in matrix[i])
        if not math.isinf(min_row):
            reduced += min_row
        else:
            continue
        for j in range(size):
            matrix[i][j] -= min_row

    # reducing col
    for j in range(size):
        min_col = float('inf')
        for i in range(size):
            if matrix[i][j] < min_col: min_col = int(matrix[i][j])
        if not math.isinf(min_col):
            reduced += min_col
        else:
            continue
        for i in range(size):
            matrix[i][j] -= min_col

    return reduced


# Print matrix for debugging
# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print '%3s' % matrix[i][j],
#         print


# Update matrix from f to t
def bound(f, t, matrix):
    a = matrix[f][t]
    matrix[t][f] = float('inf')
    size = len(matrix)
    matrix[f] = [float('inf') for col in matrix[f]]
    for j in range(size):
        matrix[j][t] = float('inf')
    r = reducing(matrix)
    return a + r


# Return list of unvisited node
def node_child(matrix):
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not math.isinf(matrix[i][j]):
                l += [i]
    l = list(set(l))
    return l


# Solve TSP recursively
def solve(q,state_num):
    cur_state = q.get()
    reducing_state = cur_state[0]
    node_state = cur_state[1]
    matrix_state = cur_state[2]
    node_target = node_child(matrix_state)
    if len(node_target) == 1:
        node_state.append(node_state[0])
        node_state = [elem + 1 for elem in node_state]
        return reducing_state, node_state, state_num
    else:
        state_num+=len(node_target)-1
        for i in node_target:
            if i == node_state[-1]: continue
            matrix_temp = deepcopy(matrix_state)
            total = reducing_state + bound(node_state[-1], i, matrix_temp)
            q.put((total, node_state + [i], matrix_temp))
        return solve(q,state_num)


# Read user input
filename = raw_input("Masukan nama file : ")
node_init = int(raw_input("Masukan node awal : "))

# Read file and make a matrix
matrix = open("../data/" + filename, "r").read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]
matrix = [[to_int(column) for column in row] for row in matrix]

# create initial graph
create_graph(matrix,[],True)
matrix_final = deepcopy(matrix)

# Node 1..N is 0..N-1
node_init -= 1

# Add reducing state to priority queue
q = Q.PriorityQueue()
c0 = reducing(matrix)
state_num = 1
q.put((c0, [node_init], matrix))

start_time = time.time()
# Solve TSP :)
result = solve(q,state_num)
print("Total bobot tereduksi : %.2f" % result[0])
print "Jalur yang ditempuh : ",
print result[1]
print("Simpul yang dibangkitkan : %d" % result[2])
print("Waktu yang diperlukan : %.6s detik" % (time.time() - start_time))

# create graph after TSP algorithm
create_graph(matrix_final,result[1],True)