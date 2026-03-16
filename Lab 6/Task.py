tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'N': [],
    'M': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}

def dfsStack(graph, start, goal):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            
            if vertex == goal:
                print("\nGoal node G reached!")
                return
            
            for neighbour in reversed(graph[vertex]):
                if neighbour not in visited:
                    stack.append(neighbour)

print("DFS Search (using Stack) from A to G:")
dfsStack(tree, 'A', 'G')