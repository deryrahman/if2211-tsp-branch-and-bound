import math
import networkx as nx
import matplotlib.pyplot as plt


def create_digraph(matrix, result=None):

    if result is None:
        result = []
    G = nx.MultiDiGraph()
    G.add_nodes_from(range(1,len(matrix)+1))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not math.isinf(float(matrix[i][j])) :
                G.add_edge(i+1,j+1,length=matrix[i][j])

    pos = nx.shell_layout(G)
    edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])

    # edlist = []
    # for ed in G.edges():
    #     edlist.append(ed)
    result = [(result[i],result[i+1]) for i in range(len(result)-1)]
    # result.extend([elem[::-1] for elem in result])
    # edlist = list(set(edlist)-set(result))
    #
    # for el in result:
    #     edge_labels.pop(el, None)
    #
    # print edge_labels

    # nx.draw(G, pos, node_color = 'red', node_size=500)
    nx.draw_networkx_labels(G,pos, font_color='white', font_size=5)
    nx.draw_networkx_nodes(G,pos,node_size=80, node_color = 'black')
    nx.draw_networkx_edges(G,pos,width=0.15, edge_color="red")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.9, font_size=4)
    # plt.figure(figsize=(20, 20))
    if(result):
        nx.draw_networkx_edges(G, pos, result, width=1, edge_color="green")
    plt.axis('off')
    if(not result):
        plt.savefig("../output/initial_graph.pdf")
    else:
        plt.savefig("../output/final_graph.pdf")

def create_graph(matrix, result=None):

    if result is None:
        result = []
    G = nx.MultiGraph()
    G.add_nodes_from(range(1,len(matrix)+1))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not math.isinf(float(matrix[i][j])) :
                G.add_edge(i+1,j+1,length=matrix[i][j])

    pos = nx.shell_layout(G)
    edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])

    # edlist = []
    # for ed in G.edges():
    #     edlist.append(ed)
    result = [(result[i],result[i+1]) for i in range(len(result)-1)]
    # result.extend([elem[::-1] for elem in result])
    # edlist = list(set(edlist)-set(result))
    #
    # for el in result:
    #     edge_labels.pop(el, None)
    #
    # print edge_labels

    # nx.draw(G, pos, node_color = 'red', node_size=500)
    nx.draw_networkx_labels(G,pos, font_color='white', font_size=5)
    nx.draw_networkx_nodes(G,pos,node_size=80, node_color = 'black')
    nx.draw_networkx_edges(G,pos,width=0.15, edge_color="red")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.9, font_size=4)
    # plt.figure(figsize=(20, 20))
    if(result):
        nx.draw_networkx_edges(G, pos, result, width=1, edge_color="green")
    plt.axis('off')
    if(not result):
        plt.savefig("../output/initial_graph.pdf")
    else:
        plt.savefig("../output/final_graph.pdf")