import networkx as nx
import matplotlib.pyplot as plt

visited = {}
f = open("crawlerPath.txt" , "r")
content = f.read()
visited = eval(content)
#print(visited) # debug

G = nx.DiGraph()

# Creating all the nodes
valueNodes = list(visited.values())
#print("valueNodes: " + str(valueNodes)) # debug

keyNodes = list(visited.keys())
#print("keyNodes: " + str(keyNodes)) # debug

nodes = keyNodes + valueNodes
nodes = list(dict.fromkeys(nodes))
#print("Nodes: " + str(nodes)) # debug

edges = visited.items()


G.add_nodes_from(nodes)
#print(list(G.nodes))


#G.add_edge('https://www.w3schools.com', 'https://www.w3schools.com/images/w3schools_logo_436_2.png')

for value, key in visited.items():
    G.add_edge(key, value)


pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=nodes)
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, arrowsize=1, width=1)


plt.show()

