import networkx as nx
import math

def is_pareto_efficient(valuations: list[list[float]], allocation: list[list[float]] ) -> bool:
    G = build_graph(valuations, allocation)
    try:
        nx.find_negative_cycle(G,0, weight="weight") #Throws error if there is no negative cycle.
        return False
    except:
        return True

def build_graph(valuations: list[list[float]], allocation: list[list[float]] ) -> nx.DiGraph: #Builds Clique
    G = nx.DiGraph()
    player_num = len(valuations)
    G.add_nodes_from(range(player_num))
    for i in range(player_num):
        for j in range(player_num):
            if i != j:
                selected_weight =(math.log10(get_min_ratio(i, j, valuations, allocation)))
                G.add_edge(i, j, weight=selected_weight)
    return G

def get_min_ratio(i, j, valuations, allocation):
    min_val = float('inf')
    for k in range(len(allocation[i])):
        if allocation[i][k] == 0 or allocation[j][k] == 0:
            continue
        curr_val = (valuations[i][k] * allocation[i][k]) / (valuations[j][k] * allocation[j][k])
        if curr_val < min_val:
            min_val = curr_val
    return min_val


valuations = [[10,20,30,40], [40,30,20,10]]
allocation = [[0,0.7,1,1], [1,0.3,0,0]]
print(is_pareto_efficient(valuations, allocation))