
import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, node1, node2, cost):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append((node2, cost))
    
    def heuristic(self, node, goal):
        # Example heuristic: Manhattan distance
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)
    
    def astar(self, start, goal):
        # Priority queue for open nodes
        open_nodes = []
        heapq.heappush(open_nodes, (0, start))
        # Keep track of cost from start to each node
        cost_from_start = {start: 0}
        # Keep track of parent nodes for reconstructing the path
        parents = {start: None}
        
        while open_nodes:
            current_cost, current_node = heapq.heappop(open_nodes)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parents[current_node]
                return path[::-1]
            
            for neighbor, cost in self.edges.get(current_node, []):
                new_cost = cost_from_start[current_node] + cost
                if neighbor not in cost_from_start or new_cost < cost_from_start[neighbor]:
                    cost_from_start[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(open_nodes, (priority, neighbor))
                    parents[neighbor] = current_node
        
        return None

# Function to take user input for constructing the graph
def construct_graph():
    graph = Graph()
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        node1, node2, cost = map(int, input("Enter source, destination, and cost of edge (space-separated): ").split())
        graph.add_edge(node1, node2, cost)
        graph.add_edge(node2, node1, cost)  # Assuming undirected graph
    
    return graph

# Main function
if __name__ == "__main__":
    graph = construct_graph()
    start_node = tuple(map(int, input("Enter the start node (x y): ").split()))
    goal_node = tuple(map(int, input("Enter the goal node (x y): ").split()))
    path = graph.astar(start_node, goal_node)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found.")