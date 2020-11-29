import random

x = 0
y = 0

def get_obstacles():
    '''
    Ensures new list of obstacles isn't 
    recalculated each time fn is called
    '''

    obstacles = [(random.randint(-100,100), random.randint(-200,200)) 
    for coord in range(200)]

    return obstacles


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
        if x in range(obstacle[0], obstacle[0] + 4) and y in range(obstacle[1], obstacle[1] + 4):
            obstacle_present = True
    
    # print("is position blocked, ", x, y, obstacles, obstacle_present)

    return obstacle_present


def is_path_blocked(x1,y1,x2,y2, obstacles):
    '''
    Looks ahead to see if destined position will come into contact
    with an obstacle.
    :param: x1,y1: original x and y pos
    :param: x2,y2: potentially destined x and y pos
    :return: True if there is an obstacle along the path
    '''

    path_is_blocked = False

    # print("In is path blocked obstacles: ", obstacles)
    # print("In is path blocked ", x1,y1,x2,y2)

    if x1 == x2:
        #only asseses obstacles moving vertically
        for obstacle in obstacles:
            if obstacle[1] >= min(y1,y2) and obstacle[1] <= max(y1,y2):
                for current_y_pos in range (min(y1,y2), max(y1,y2)):
                    if is_position_blocked(x2, current_y_pos, obstacles) == True:
                        path_is_blocked = True

    if y1 == y2:
        #only asseses obstacles moving horizontally
        for obstacle in obstacles:
            if obstacle[0] >= min(x1,x2) and obstacle[0] <= max(x1,x2):
                for current_x_pos in range (min(x1,x2), max(x1,x2)):
                    if is_position_blocked(current_x_pos, y1, obstacles) ==True:
                        path_is_blocked = True

    return path_is_blocked


def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some maze obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))