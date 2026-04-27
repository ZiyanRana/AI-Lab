heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

weighted_graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101, 'Craiova': 138},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

def a_star(start, goal):
    g_costs = {start: 0} 
    parents = {start: None}
    open_list = [start]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        for node in open_list:
            f_node = g_costs[node] + heuristics[node]
            f_current = g_costs[current_node] + heuristics[current_node]
            if f_node < f_current:
                current_node = node

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]

        open_list.remove(current_node)
        closed_list.append(current_node)

        for neighbor, weight in weighted_graph.get(current_node, {}).items():
            new_g_cost = g_costs[current_node] + weight

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                parents[neighbor] = current_node
                if neighbor not in open_list:
                    open_list.append(neighbor)
    
    return None

print(a_star('Arad', 'Bucharest'))