from collections import defaultdict

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Function to construct the graph from user input
def construct_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        src, dest = map(int, input("Enter source and destination of edge (space-separated): ").split())
        graph[src].append(dest)
        graph[dest].append(src)  # Assuming undirected graph

    return graph

# Main function
if __name__ == "__main__":
    graph = construct_graph()
    start_node = int(input("Enter the start node for BFS: "))
    print("BFS traversal:")
    bfs(graph, start_node)