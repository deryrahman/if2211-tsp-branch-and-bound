#!/usr/bin/env python
import Queue as Q
import math
from graph import *
from copy import deepcopy


# Convert to inf if reading INF string from file
def to_int(x):
    if x == 'INF':
        return float('inf')
    else:
        return int(x)



# Print matrix for debugging
# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print '%3s' % matrix[i][j],
#         print


# Generate lower bound from initial matrix
def lower_bound(matrix):
    sum_min = 0
    for row in matrix:
        sum_min += min(row)
    return sum_min

def bound(node_next,matrix):
    cur_weight=0
    for j in range(len(node_next) - 1):
        cur_weight += matrix[node_next[j]][node_next[j + 1]]

    print node_next[:-1]
    for i in range(len(matrix)):
        if(i in node_next[:-1]) : continue
        min=0
        for j in range(len(matrix)):
            if(j in node_next): continue
            if(min>matrix[i][j]):
                min=matrix[i][j]
        cur_weight+=min
        # if j not in node_next[:-1]:
        #     print [i for k, i in enumerate(matrix[j]) if k not in node_next[:-1]]
        #     cur_weight += min([i for k, i in enumerate(matrix[j]) if k not in node_next])
    return cur_weight

# Return list of unvisited node
def node_child(node_state,matrix):
    l = [i for i in range(len(matrix))]
    l = list(set(l)-set(node_state))
    return l


# Solve TSP recursively
def solve(q,state_num,matrix):
    cur_state = q.get()
    cur_weight = cur_state[0]
    node_state = cur_state[1]
    node_target = node_child(node_state,matrix)
    print node_target
    if len(node_target) == 0:
        node_state.append(node_state[0])
        node_state = [elem + 1 for elem in node_state]
        return cur_weight, node_state, state_num
    else:
        state_num+=len(node_target)-1
        for i in node_target:
            node_next = node_state + [i]
            cur_weight=bound(node_next,matrix)
            print node_next
            print cur_weight
            q.put((cur_weight, node_next))
        return solve(q,state_num,matrix)


# Read user input
filename = raw_input("Masukan nama file : ")
node_init = int(raw_input("Masukan node awal : "))

# Read file and make a matrix
matrix = open("../data/" + filename, "r").read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]
matrix = [[to_int(column) for column in row] for row in matrix]

# create initial graph
create_graph(matrix)
matrix_final = deepcopy(matrix)

# Node 1..N is 0..N-1
node_init -= 1

# Add reducing state to priority queue
q = Q.PriorityQueue()
c0 = lower_bound(matrix)
state_num = 1
q.put((c0, [node_init]))

# Solve TSP :)
result = solve(q,state_num,matrix)
print result
#
# # create graph after TXP algorithm
# create_graph(matrix_final,result[1])