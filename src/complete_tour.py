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


# Update matrix from f to t
def cost(node, matrix):
    size = len(matrix)
    sum=0
    if len(node) == 1:
        for i in range(size):
            m1, m2 = float('inf'), float('inf')
            for j in range(size):
                if matrix[i][j] <= m1:
                    m1, m2 = matrix[i][j], m1
                elif matrix[i][j] < m2:
                    m2 = matrix[i][j]
            sum += m1 + m2
        return float(sum)/2
    else :
        for i in range(size):
            m1, m2 = float('inf'), float('inf')
            if i in node[:-1]:
                m1 = matrix[i][node[node.index(i)+1]]
                curr_j = node[node.index(i)+1]
                for j in range(size):
                    if j==curr_j: continue
                    if m2 > matrix[i][j]:
                        m2 = matrix[i][j]
            else:
                for j in range(size):
                    if matrix[i][j] <= m1:
                        m1, m2 = matrix[i][j], m1
                    elif matrix[i][j] < m2:
                        m2 = matrix[i][j]
            sum+=m1+m2
        return float(sum)/2


# Return list of unvisited node
def node_child(node_state,matrix):
    l = []
    size = len(matrix)
    for i in range(size):
        if i in node_state: continue
        l += [i]
    return l


# Solve TSP recursively
def solve(q,matrix,state_num):
    cur_state = q.get()
    curr_cost = cur_state[0]
    node_state = cur_state[1]
    node_target = node_child(node_state,matrix)
    if len(node_target) == 0:
        if node_state[-1]==node_state[0]:
            prev_state = []
            i = 0
            while(not q.empty()):
                temp = q.get()
                if temp[0]<=curr_cost:
                    prev_state += [temp]
                    i+=1
            for elem in prev_state:
                q.put(elem)
            if not q.empty():
                return solve(q,matrix,state_num)
            else:
                node_state = [elem + 1 for elem in node_state]
                return curr_cost, node_state, state_num
        else:
            node_next = node_state + [node_state[0]]
            cost_next = cost(node_next,matrix)
            q.put((cost_next, node_next))
            return solve(q,matrix,state_num)
    else:
        state_num+=len(node_target)
        print [elem + 1 for elem in node_target]
        for i in node_target:
            node_next = node_state + [i]
            cost_next = cost(node_next,matrix)
            q.put((cost_next, node_next))
        return solve(q,matrix,state_num)


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
c0 = cost([node_init],matrix)
state_num = 1
q.put((c0, [node_init]))

# Solve TSP :)
result = solve(q,matrix,state_num)
print result

# create graph after TSP algorithm
create_graph(matrix_final,result[1])