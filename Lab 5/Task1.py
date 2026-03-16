import collections

graph = {
    0: [1, 4],
    1: [0, 4, 3, 2],
    2: [1, 3],
    3: [1, 4, 2],
    4: [0, 1, 3]
}

def bfsTraversal(graph, start):
    visited = set()
    queue = collections.deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

print("BFS Traversal starting from node 0:")
bfsTraversal(graph, 0)