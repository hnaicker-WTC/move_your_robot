# from ..obstacles import obstacles
from maze import obstacles
from maze import hiranya_maze
from import_helper import dynamic_import

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

valid_mazes = [hiranya_maze, test_maze]

def initialise(selected_maze):
    """
    Initiate text module.
    """
    global position_x, position_y, current_direction_index

    if selected_maze == 'obstacles':
        _obstacles = obstacles.get_obstacles()
    elif selected_maze in valid_mazes:
        _obstacles = dynamic_import(f'maze.{argument.lower()}')

    obstacles.print_obstacles(_obstacles)

    position_x = 0
    position_y = 0
    current_direction_index = 0

    return _obstacles



def teardown():
    """
    Terminate text module.
    """
    pass


# def display_obstacles():
#     '''
#     Prints out positions of obstacles
#     :return: list of tuples of obstacle positions
#     '''
#     _obstacles = obstacles.get_obstacles()

#     for _obstacle in _obstacles:
#         print("- At position {} (to {},{})",_obstacle, _obstacle[0]+4 ,
#          _obstacle[1]+4 )
#     return _obstacles


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



