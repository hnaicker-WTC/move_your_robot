'''
Creates an object 'node' that carries parameters attached to each node that will be used to prioritise a path.
'''

class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


def astar_search(obstacles, edge):
    '''
    A* search algorithm that generates a path of a list of coordinates to a specific edge.
    :param: obstacles - either obstacles or specified maze
    :param: edge - top/bottom/left/right
    return: path to edge- list of tuples 
    '''
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node
    start_node = Node((0,0), None)
    
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if at_the_edge(edge, current_node.position):
            
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #path.append(start) 
            # Return reversed path
            return path[::-1]
        # Separate the current node position into x,y
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # Loop neighbors
        for adjacent_node in neighbors:
            
            # Check if the node is an obstacle
            if is_position_blocked(adjacent_node[0], adjacent_node[1], obstacles):
                continue
            # Create a neighbor node
            neighbor = Node(adjacent_node, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue

            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = calculate_heuristic_off_edge(neighbor, edge) 
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(should_add_to_open(open, neighbor) == True):
                # Add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


def at_the_edge(edge, position):
    if edge == 'top' and position[1] == 200:
        return True
    elif edge == 'bottom' and position[1] == -200:
        return True
    elif edge == 'right' and position[0] == 100:
        return True
    elif edge == 'left' and position[0] == -100:
        return True
    else:
        return False


def calculate_heuristic_off_edge(neighbor, edge):
    '''
    Calculates the lowest heuristic from specified edge
    :param: neighbor - tuple
    :param: edge
    return: heuristic value-integer
    '''

    heuristic = 0

    if edge == 'top':
        heuristic = abs(neighbor.position[1] - 200)
    elif edge == 'bottom':
        heuristic = abs(neighbor.position[1] + 200)
    elif edge == 'left':
        heuristic = abs(neighbor.position[0] + 100)
    elif edge == 'right':
        heuristic = abs(neighbor.position[0] - 100)

    return heuristic


def should_add_to_open(open, neighbor):
    '''
    Checks if a neighbor coord should be added to open list
    :param: open - list
    :param: neighbor - tuple
    return: False if neighbor coord already exists in open list and neighbor has a higher cost otherwise True
    '''
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True


def is_position_blocked(x, y, obstacles):
    '''
    Checks to see if destined x and y coords cross over any of
    the obstacle coords.
    :param: x
    :param: y
    :return: True if there is an obstacle 
    '''
    obstacle_present = False

    for obstacle in obstacles:
        if x in range(obstacle[0], obstacle[0] + 5) and y in range(obstacle[1], obstacle[1] + 5):
            obstacle_present = True
    
    # print("is position blocked, ", x, y, obstacles, obstacle_present)

    return obstacle_present