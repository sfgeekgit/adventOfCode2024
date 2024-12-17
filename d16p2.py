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


def find_lowest_cost(map, start, goal):
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

                # skip 180 degree turn
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

def find_all_lowest_cost_paths(map, start, goal, lowest_cost):
    # Queue for nodes to explore: (cost, node, direction, path_so_far)
    queue = [(0, start, facing, [start])]
    
    # List to store all paths with the lowest cost
    all_paths = []

    # Dictionary to track costs for each (node, direction) combination
    costs = {(start, tuple(facing)): 0}
    
    #paths_found = 0

    while queue:
        current_cost, current_node, current_facing, current_path = queue.pop(0)

        # If we're beyond the lowest cost, skip this path
        if current_cost > lowest_cost:
            continue

        # If the goal is reached with the lowest cost, store the path
        if current_node == goal and current_cost == lowest_cost:
            #paths_found += 1
            all_paths.append(current_path)
            continue

        # Explore neighbors
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            if (0 <= neighbor[0] < len(map) and 
                0 <= neighbor[1] < len(map[0]) and 
                map[neighbor[0]][neighbor[1]] != '#'):
                

                current_index = directions.index(current_facing)
                new_index = directions.index(direction)
                turn_steps = abs(new_index - current_index)
                if turn_steps > 2:
                    turn_steps = 4 - turn_steps

                if turn_steps == 2:
                    continue

                turn_cost = turn_steps * turn_90_cost
                move_cost = move_1_cost
                new_cost = current_cost + move_cost + turn_cost

                # Only continue if this path could lead to the lowest cost
                if new_cost <= lowest_cost:
                    state = (neighbor, tuple(direction))
                    
                    # If we haven't seen this state, or we can reach it with same cost
                    if (state not in costs or new_cost <= costs[state]):
                        costs[state] = new_cost
                        new_path = current_path + [neighbor]
                        queue.append((new_cost, neighbor, direction, new_path))

    print(f"Queue exhausted. Processed {len(costs)} states.")
    print(f"Final queue size: {len(queue)}")

    # Find all nodes that appear in any of the lowest-cost paths
    all_nodes = set()
    for path in all_paths:
        all_nodes.update(path)

    return all_paths, all_nodes

# First, find the lowest cost
lowest_cost = find_lowest_cost(map, tuple(enter), tuple(exit))

# Then, find all paths with the lowest cost
paths, common_nodes = find_all_lowest_cost_paths(map, tuple(enter), tuple(exit), lowest_cost)

print(f"Path cost from enter to exit: {lowest_cost}")
print(f"Number of paths with lowest cost: {len(paths)}")
#print(f"Common nodes in all lowest cost paths: {common_nodes}")
#print(f"{paths=}")
print(f"{len(common_nodes)=}")