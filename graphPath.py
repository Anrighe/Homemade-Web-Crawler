import networkx as nx
import matplotlib.pyplot as plt

f = open("crawlerPath.txt", "r")
content = f.read()
visited = eval(content)

G = nx.DiGraph()

# Creating the nodes and the edges
valueNodes = list(visited.values())

keyNodes = list(visited.keys())

nodes = keyNodes + valueNodes
nodes = list(dict.fromkeys(nodes))

edges = visited.items()

G.add_nodes_from(nodes)

for value, key in visited.items():
    G.add_edge(key, value)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=nodes)
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, arrowsize=1, width=1)

plt.show()

