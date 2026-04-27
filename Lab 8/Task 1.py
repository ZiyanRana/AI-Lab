heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni']
}

def greedy_best_first_search(start, goal):
    open_list = [start]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        for node in open_list:
            if heuristics[node] < heuristics[current_node]:
                current_node = node

        if current_node == goal:
            return True

        open_list.remove(current_node)
        closed_list.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
    return False

greedy_best_first_search('Arad', 'Bucharest')