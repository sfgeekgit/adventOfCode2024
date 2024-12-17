import heapq

filename = "test16b.txt"
filename = "input16.txt"

map = []
exit = []
enter = []
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
facing = directions[0]  # begin facing right

move_1_cost = 1 
turn_90_cost = 1000 

with open(filename, "r") as file:
    for line in file:
        map.append(line.strip())
        if "E" in line:
            exit = [len(map) - 1, line.index("E")]
        if "S" in line:
            enter = [len(map) - 1, line.index("S")]


def dijkstra_with_turns(map, start, goal):
    # Priority queue for open nodes
    open_list = []
    heapq.heappush(open_list, (0, start, facing))

    best_cost = {tuple(start): 0}

    while open_list:
        current_cost, current_node, current_facing = heapq.heappop(open_list)

        if current_node == goal:
            return current_cost

        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            if (0 <= neighbor[0] < len(map) and 
                0 <= neighbor[1] < len(map[0]) and 
                map[neighbor[0]][neighbor[1]] != '#'):
                

                current_index = directions.index(current_facing)
                new_index = directions.index(direction)
                turn_steps = abs(new_index - current_index)
                if turn_steps > 2:
                    turn_steps = 4 - turn_steps  # Adjust for wrap-around

                # skip the 180 turn
                if turn_steps == 2:
                    continue

                turn_cost = turn_steps * turn_90_cost
                move_cost = move_1_cost

                new_cost = current_cost + move_cost + turn_cost

                # If this path to the neighbor is better, update and push to the queue
                if tuple(neighbor) not in best_cost or new_cost < best_cost[tuple(neighbor)]:
                    best_cost[tuple(neighbor)] = new_cost
                    heapq.heappush(open_list, (new_cost, neighbor, direction))

    return None  # Return None if no path is found

path_cost = dijkstra_with_turns(map, tuple(enter), tuple(exit))
print(f"Path cost from enter to exit: {path_cost}")