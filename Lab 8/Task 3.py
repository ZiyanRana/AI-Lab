GOAL_STATE = (1, 2, 3, 5, 8, 6, 0, 7, 4)

def count_misplaced(current_state):
    count = 0
    for i in range(len(current_state)):
        if current_state[i] != 0 and current_state[i] != GOAL_STATE[i]:
            count += 1
    return count

def get_moves(state):
    moves = []
    state_list = list(state)
    blank = state_list.index(0)
    row, col = divmod(blank, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_blank = r * 3 + c
            new_state = state_list[:]
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            moves.append(tuple(new_state))
    return moves

def solve_puzzle(start):
    open_list = [(count_misplaced(start), 0, start, [])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, current, path = open_list.pop(0)

        if current == GOAL_STATE:
            return path + [current]

        visited.add(current)

        for move in get_moves(current):
            if move not in visited:
                new_g = g + 1
                new_f = new_g + count_misplaced(move)
                open_list.append((new_f, new_g, move, path + [current]))

start_state = (1, 2, 3, 5, 6, 0, 7, 8, 4)
result = solve_puzzle(start_state)

for step in result:
    print(step[0:3])
    print(step[3:6])
    print(step[6:9])
    print("---")