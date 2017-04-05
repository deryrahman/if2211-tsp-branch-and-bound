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

# Lower bound
def lower_bound(matrix):
    table_two_minimum = []
    sum = 0
    for row in matrix:
        m1, m2 = float('inf'), float('inf')
        for x in row:
            if x <= m1:
                m1, m2 = x, m1
            elif x < m2:
                m2 = x
        sum+=m1+m2
        table_two_minimum.append([m1,m2])
    return sum, table_two_minimum

# Calculate cost
def cost(node, matrix):
    sum = 0
    remain = list(set(range(len(matrix)))-set(node))
    for i in range(1,len(node)-1):
        sum+=matrix[node[i]][node[i+1]]+matrix[node[i]][node[i-1]]
    if not node[0]==node[-1]:
        sum+=matrix[node[0]][node[1]]+matrix[node[-1]][node[-2]]
        m1=0
        m2=0
        if remain :
            m1 = float('inf')
            m2 = float('inf')
            for i in remain:
                if matrix[node[0]][i]<m1:
                    m1 = matrix[node[0]][i]
                if matrix[node[-1]][i]<m2:
                    m2 = matrix[node[-1]][i]
        sum+=m1+m2

    if sum == 0: # if still in first node
        remain+=[node[0]]
    for i in remain:
        m1, m2 = float('inf'), float('inf')
        for j in range(len(matrix)):
            if matrix[i][j] <= m1:
                m1, m2 = matrix[i][j], m1
            elif matrix[i][j] < m2:
                m2 = matrix[i][j]
        sum+=m1+m2

    return float(sum)/2

def node_child(node_state,matrix):
    return list(set(range(len(matrix)))-set(node_state))


# Solve TSP recursively
def solve(q,matrix,state_num):
    cost_res = 0
    node_state_res = []
    B = float('inf')
    while(not q.empty()):
        cur_state = q.get()
        curr_cost = cur_state[0]
        node_state = cur_state[1]
        node_target = node_child(node_state,matrix)

        if not node_target:
            if not node_state[0]==node_state[-1]:
                node_next = node_state + [node_state[0]]
                cost_next = curr_cost+matrix[node_state[-1]][node_state[0]]
                q.put((cost_next,node_next))
            else :
                if curr_cost<B :
                    node_state_res = node_state
                    cost_res = curr_cost
                B = curr_cost
                store = []
                while not q.empty():
                    temp = q.get()
                    if abs(temp[0] - B)<=0.1:
                        store.append(temp)
                for elem in store:
                    q.put(elem)

        state_num += len(node_target)
        for i in node_target:
            node_next = node_state + [i]
            cost_next = cost(node_next,matrix)
            if cost_next<=B:
                q.put((cost_next, node_next))

    node_state_res = [elem + 1 for elem in node_state_res]
    return cost_res, node_state_res, state_num


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
low_bound = cost([node_init],matrix)
state_num = 1
q.put((low_bound, [node_init]))

# Solve TSP :)
result = solve(q,matrix,state_num)
print result

# create graph after TSP algorithm
create_graph(matrix_final,result[1])