import os.path
from maze import obstacles
from import_helper import dynamic_import

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def initialise(selected_maze):
    """
    Initiate text module.
    """
    global position_x, position_y, current_direction_index

    mazeModule = obstacles

    if selected_maze == 'obstacles':
        _obstacles = obstacles.get_obstacles()
    elif os.path.isfile('maze/' + selected_maze + '.py'):
        mazeModule = dynamic_import(f'maze.{selected_maze.lower()}')
        _obstacles = mazeModule.get_obstacles()
    else:
        _obstacles = []

    print_obstacles(_obstacles)

    position_x = 0
    position_y = 0
    current_direction_index = 0

    return _obstacles


def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))


def teardown():
    """
    Terminate text module.
    """
    pass


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','
    +str(position_y)+').')


def is_position_allowed(position_x, position_y, new_x, new_y, obstacles1):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    # print("in pos allowed, ", position_x, position_y, new_x, new_y, obstacles1)

    # check to see if obstacles don't block robot moving 
    if obstacles.is_path_blocked(position_x, position_y, new_x, new_y, obstacles1):
        return False, 'obstacles'
    else:
        can_move = min_x <= new_x <= max_x and min_y <= new_y <= max_y
        if can_move:
           return can_move, 'none'
        else:
            return can_move, 'edge'
        

def update_position(steps, obstacles):
    """
    Update the current x and y positions given the current direction, and 
    specific no. of steps
    :param steps:
    :return: True if the position was updated, else False
    """


    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    can_move, reason = is_position_allowed(position_x, position_y, new_x, new_y, obstacles)

    if can_move:
        position_x = new_x
        position_y = new_y
        return True, reason
    return False, reason


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def go_the_correct_way(next_position, robot_name):
    '''
    Turns robot left till it is facing the correct direction
    :param: next_position - tuple of position robot must move to
    :param: robot_name
    '''

    if next_position[1] > position_y:
        required_direction = 0
    elif next_position[1] < position_y:
        required_direction = 2
    elif next_position[0] > position_x:
        required_direction = 1
    else:
        required_direction = 3

    while current_direction_index != required_direction:
        do_left_turn(robot_name)


def do_mazerun_path(path, obstacles, robot_name, edge):
    '''
    Moves the robot along the given path
    :param: path - list of tuples
    :param: obstacles
    :param: robot_name
    :param: edge - top/bottom/left/right
    return: True when at the edge
    '''
    for coord in path:
        go_the_correct_way(coord, robot_name)
        update_position(1, obstacles)

    return True, ''+robot_name+': I am at the {} edge'.format(edge)  
