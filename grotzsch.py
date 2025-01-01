
import networkx as nx
from matplotlib import pyplot as plt

class TriangleFreeGraph:
    def __init__(self, graph=None):
        """Initialize: Set up a graph or create an empty graph"""
        self.graph = graph if graph else nx.Graph()

    def is_triangle_free(self):
        """Make sure the graph is triangular"""
        for cycle in nx.cycle_basis(self.graph):
            if len(cycle) == 3:
                return False
        return True

    def three_color(self):
        """Color the graph with 3 colors"""
        if not self.is_triangle_free():
            raise ValueError("Graph does not have a triangle; 3-color cannot be applied.")
        
        # Try 3-color with greedy coloring algorithm
        coloring = nx.coloring.greedy_color(self.graph, strategy="largest_first")
        max_color = max(coloring.values())
        
        if max_color >= 3:
            raise ValueError("Coloring results exceed 3 colors; this may not be a plane graph without a triangle.")
        
        return coloring

    def visualize(self, coloring):
        """Visualize Graphs"""
        color_map = ["red", "blue", "green"]
        node_colors = [color_map[coloring[node]] for node in self.graph.nodes()]
        nx.draw(self.graph, with_labels=True, node_color=node_colors)
        plt.show()

def main():
    # Create Graph
    n = 7 
    G = nx.cycle_graph(n)  # a circular graph consisting of n nodes
    G.add_edge(0, 3)       # Additional edges that do not create a triangle

    # Create a TriangleFreeGraph object
    graph_checker = TriangleFreeGraph(G)

    # Make sure you don't have a triangle
    if graph_checker.is_triangle_free():
        print("Graph has no triangle.")
        
        # 3-Color Execution
        try:
            coloring = graph_checker.three_color()
            print("Coloring Results:", coloring)
            
            # Visualization
            graph_checker.visualize(coloring)
        except ValueError as e:
            print("Error:", e)
    else:
        print("The graph has a triangle. 3-color is impossible.")

if __name__ == "__main__":
    main()

