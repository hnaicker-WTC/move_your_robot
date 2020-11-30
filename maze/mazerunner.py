class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()): #change position to tuple?
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


def astar_search(map, start, end):
    
    # Create lists for unmapped nodes and mapped nodes
    unmapped = []
    mapped = []
    # Create a start node and an goal node
    start_node = Node(start, None) #start = (0,0)
    goal_node = Node(end, None) 
    # Add the start node
    unmapped.append(start_node)
    
    # Loop until the unmapped list is empty
    while len(unmapped) > 0:
        # Sort the unmapped list to get the node with the lowest cost first
        unmapped.sort()
        # Get the node with the lowest cost
        current_node = unmapped.pop(0)
        # Add the current node to the mapped list
        mapped.append(current_node)
        
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
            # Get value from map
            map_value = map.get(next)
            # Check if the node is a wall
            if(map_value == '#'):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the mapped list
            if(neighbor in mapped):
                continue
            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in unmapped list and if it has a lower f value
            if(add_to_unmapped(unmapped, neighbor) == True):
                # Everything is green, add neighbor to unmapped list
                unmapped.append(neighbor)
    # Return None, no path is found
    return None

def add_to_unmapped(unmapped, neighbor):
    for node in unmapped:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

