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

# def run(robot_name, obstacles, environment):
#     print("I am in maze run run()")
#     return "",""

# A* search
def astar_search(obstacles, edge):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node((0,0), None)
    goal_node = Node(find_edge_node(edge), None)
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
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #path.append(start) 
            # Return reversed path
            return path[::-1]
        # Unzip the current node position
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # Loop neighbors
        for next in neighbors:
            
            # Check if the node is an obstacle
            if is_position_blocked(next[0], next[1], obstacles):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(should_add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


def find_edge_node(edge):
    



# Check if a neighbor should be added to open list
def should_add_to_open(open, neighbor):
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