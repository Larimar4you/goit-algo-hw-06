import networkx as nx
import matplotlib.pyplot as plt


# Створюємо граф
G = nx.Graph()
stops = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(stops)

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F"),
]
G.add_edges_from(edges)

# візуалізація
plt.figure()
nx.draw(G, with_labels=True, node_color="lightblue", node_size=800)
plt.title("Transport Network Graph")
plt.savefig("analysis/graph.png")
# зберігаємо зображення у папку analysis
plt.show()

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Degree of nodes:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
