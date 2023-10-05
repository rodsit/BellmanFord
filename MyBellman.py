# This will run in a terminal or VS etc. No extra pages needed 
# I made it in Python 3.11.5
# The matlab graphic is 3D so rotate it with mouse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

arr =np.empty(10)
arb =np.empty(10)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w]) 

    def bellman_ford(self, src):
        # Initialize distance from source to all other vertices as infinity
        distance = [float("inf")] * self.V
        distance[src] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Check for negative weight cycles
        for u, v, w in self.graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the shortest distances
        for i in range(self.V):
            print(f"Vertex {i} is at distance {distance[i]} from the source")
            arr[i] = distance[i]
            arb[i] = i
            
g = Graph(5)
vectors = np.array([[0, 1, 1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, 3]])
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, 3)
g.bellman_ford(0)
# matlab
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)
ax.scatter(vectors[:, 0], vectors[:, 1], vectors[:, 2], 'r.')
ax.text(0, 0, -4, "Vertex {} at Distance {}\nVertex {} at Distance {}\nVertex {} at Distance {}\nVertex {} at Distance {}\nVertex {} at Distance {}".format(arb[0],arr[0],arb[1],arr[1],arb[2],arr[2],arb[3],arr[3], arb[4],arr[4]), verticalalignment='bottom', horizontalalignment='right' , fontsize=10, color='blue')
ax.set_xlabel('X', fontsize='large', fontweight='bold')
ax.set_ylabel('Y', fontsize='large', fontweight='bold')
ax.set_zlabel('Z', fontsize='large', fontweight='bold')
ax.set_title('Bellman-Ford Algorithm')
plt.show()
