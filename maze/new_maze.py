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
    negy, posy = -18, 18
    negx, posx = -6, 6

    negy2, posy2 = -23, 23
    negx2, posx2 = -9, 9

    negy3, posy3 = -30, 30
    negx3, posx3 = -15, 15

    for x in range(negx - 1, posx + 2):
        for y in range(negy - 1, posy + 2):
            if (x == negx - 1 or x == posx + 1 or 
                y == negy - 1 or y == posy + 1):
                obstacle_list.append((x * 5, y * 5))
    obstacle_list.remove(((random.randrange(negx + 1, posx - 1)) * 5, (negy - 1) * 5))
    obstacle_list.remove(((random.randrange(negx + 1, posx - 1)) * 5, (posy + 1) * 5))
    obstacle_list.remove(((negx - 1) * 5,(random.randrange(negy + 1, posy - 1)) * 5))
    obstacle_list.remove(((posx + 1) * 5,(random.randrange(negy + 1, posy - 1)) * 5))
    
    for x in range(negx2 - 1, posx2 + 2):
        for y in range(negy2 - 1, posy2 + 2):
            if (x == negx2 - 1 or x == posx2 + 1 or 
                y == negy2 - 1 or y == posy2 + 1):
                obstacle_list.append((x * 5, y * 5))
    obstacle_list.remove(((random.randrange(negx2 + 1, posx2 - 1)) * 5, (negy2 - 1) * 5))
    obstacle_list.remove(((random.randrange(negx2 + 1, posx2 - 1)) * 5, (posy2 + 1) * 5))
    obstacle_list.remove(((negx2 - 1) * 5,(random.randrange(negy2 + 1, posy2 - 1)) * 5))
    obstacle_list.remove(((posx2 + 1) * 5,(random.randrange(negy2 + 1, posy2 - 1)) * 5))

    for x in range(negx3 - 1, posx3 + 2):
        for y in range(negy3 - 1, posy3 + 2):
            if (x == negx3 - 1 or x == posx3 + 1 or 
                y == negy3 - 1 or y == posy3 + 1):
                obstacle_list.append((x * 5, y * 5))
    obstacle_list.remove(((random.randrange(negx3 + 1, posx3 - 1)) * 5, (negy3 - 1) * 5))
    obstacle_list.remove(((random.randrange(negx3 + 1, posx3 - 1)) * 5, (posy3 + 1) * 5))
    obstacle_list.remove(((negx3 - 1) * 5,(random.randrange(negy3 + 1, posy3 - 1)) * 5))
    obstacle_list.remove(((posx3 + 1) * 5,(random.randrange(negy3 + 1, posy3 - 1)) * 5))
    
    return obstacle_list
    

def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some maze obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))

print(get_obstacles())