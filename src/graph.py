import math
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(matrix, result=None, digraph=False):

    if result is None:
        result = []
    if digraph:
        G = nx.MultiDiGraph()
    else :
        G = nx.MultiGraph()
    G.add_nodes_from(range(1,len(matrix)+1))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not math.isinf(float(matrix[i][j])) :
                G.add_edge(i+1,j+1,length=matrix[i][j])

    pos = nx.shell_layout(G)
    edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])

    result = [(result[i],result[i+1]) for i in range(len(result)-1)]
    nx.draw_networkx_labels(G,pos, font_color='white', font_size=5)
    nx.draw_networkx_nodes(G,pos,node_size=80, node_color = 'black')
    nx.draw_networkx_edges(G,pos,width=0.3, edge_color="red")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.9, font_size=4)
    if(result):
        nx.draw_networkx_edges(G, pos, result, width=1, edge_color="green")
    plt.axis('off')
    if(not result):
        plt.savefig("../output/initial_graph.svg")
    else:
        plt.savefig("../output/final_graph.svg")