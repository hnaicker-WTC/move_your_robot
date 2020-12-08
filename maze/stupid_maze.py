import random

x = 0
y = 0

def get_obstacles():
    '''
    Ensures new list of obstacles isn't 
    recalculated each time fn is called
    '''


    obstacle_list = []
    # visited_nodes = []
    negy, posy = -10, 16
    negx, posx = -10, 16

    for x in range(negx - 1, posx + 2):
        obstacle_list.append((x * 5, 20))

    for x in range(negx - 1, posx + 2):
        obstacle_list.append((20, x*5))
    
    for y in range(negy - 1, posy + 2):
        obstacle_list.append((y*5, 50))
    
    for y in range(negy - 1, posy + 2):
        obstacle_list.append((-75, y*5))

    for y in range(negy - 1, posy + 2):
        obstacle_list.append((y*5, -75))

    for y in range(negy - 1, posy + 2):
        obstacle_list.append((y*5, -120))
    
    for y in range(negy - 1, posy + 2):
        obstacle_list.append((y*5, 120))
    
    return obstacle_list


def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some maze obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))