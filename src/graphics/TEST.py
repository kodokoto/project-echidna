import networkx as nx
import matplotlib.pyplot as plt
from typing import List

def create_graph(grid: List[List[str]]) -> nx.Graph:
    graph = nx.Graph()
    rows = len(grid)
    cols = len(grid[0])

    spawn_node = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 'empty':
                node_name = grid[i][j]
                graph.add_node(node_name)

                if node_name == 'spawn':
                    spawn_node = node_name

                if i > 0 and grid[i-1][j] != 'empty':
                    graph.add_edge(node_name, grid[i-1][j])
                if i < rows - 1 and grid[i+1][j] != 'empty':
                    graph.add_edge(node_name, grid[i+1][j])
                if j > 0 and grid[i][j-1] != 'empty':
                    graph.add_edge(node_name, grid[i][j-1])
                if j < cols - 1 and grid[i][j+1] != 'empty':
                    graph.add_edge(node_name, grid[i][j+1])

    if spawn_node:
        return nx.bfs_tree(graph, spawn_node)

    return None

# Example usage:
grid = [
    ['A', 'B', 'C', 'empty'],
    ['D', 'spawn', 'E', 'F'],
    ['G', 'empty', 'H', 'empty'],
    ['I', 'empty', 'empty', 'empty']
]

graph = create_graph(grid)
if graph:
    print("Graph created successfully!")
    print("Nodes:", graph.nodes())
    print("Edges:", graph.edges())

    # Draw the graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
    plt.axis('off')
    plt.show()
else:
    print("Could not find the 'spawn' node.")
