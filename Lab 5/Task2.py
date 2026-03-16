import collections

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

def bfsSearch(graph, start, goal):
    visited = set()
    queue = collections.deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        if vertex == goal:
            print("\nGoal node G reached!")
            return
            
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

print("BFS Search from A to G:")
bfsSearch(tree, 'A', 'G')