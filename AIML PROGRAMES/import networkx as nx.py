import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

def best_first_search(G, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))
    while not frontier.empty():
        _, node, path = frontier.get()
        if node == goal:
            return path
        for neighbor in G[node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                priority = abs(ord(neighbor) - ord(goal))
                frontier.put((priority, neighbor, new_path))
    return None

G = nx.Graph([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'),
              ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K'),
              ('H', 'L'), ('I', 'L'), ('J', 'L'), ('K', 'L')])

path = best_first_search(G, 'A', 'L')
print("Path:", ' -> '.join(path) if path else "No path found")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
if path:
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[path[0], path[-1]], node_color=['g', 'r'], node_size=600)
plt.show()