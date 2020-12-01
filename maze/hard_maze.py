import random

x = 0
y = 0

def get_obstacles():
    '''
    Ensures new list of obstacles isn't 
    recalculated each time fn is called
    '''

    obstacles = [(-25, 15),(-20, 15),(-15, 15),(-10, 15),(-5, 15),(0, 15),(5, 15),(10, 15),(15, 15),(-25, -15),(-20, -15),(-15, -15),(-10, -15),(-5, -15),(0, -15),(5, -15)]

    return obstacles


def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some maze obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))