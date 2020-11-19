import turtle
from maze import obstacles
# from ..obstacles import obstacles

michaelangelo = None 

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def initialise():
    """
    Initiate turtle module.
    """
    global michaelangelo
    michaelangelo = turtle.Turtle()

    draw_outline()
    _obstacles = obstacles.get_obstacles()
    draw_obstacles(_obstacles)
    set_michaelangelo()

    return _obstacles
    

def draw_outline():

    michaelangelo.hideturtle()
    michaelangelo.color('red', 'white')
    michaelangelo.up()
    michaelangelo.goto(-100, -200)
    michaelangelo.down()
    michaelangelo.pensize(5)
    michaelangelo.begin_fill()
    for i in range(4):
        if(i%2 == 0):
            michaelangelo.forward(200)
        else:
            michaelangelo.forward(400)
        michaelangelo.left(90)
    michaelangelo.end_fill()
    michaelangelo.up()
   

def draw_obstacles(obstacles):

    michaelangelo.hideturtle()
    michaelangelo.color('red', 'red')

    for obstacle in obstacles:
        michaelangelo.up()
        michaelangelo.goto(obstacle[0],obstacle[1])
        michaelangelo.down()
        michaelangelo.pensize(1)
        michaelangelo.begin_fill()
        for i in range(4):
            michaelangelo.forward(4)
            michaelangelo.left(90)
        michaelangelo.end_fill()
    
    michaelangelo.up()


def set_michaelangelo():
    michaelangelo.goto(0, 0)
    michaelangelo.down()
    michaelangelo.color('black', 'black')
    michaelangelo.left(90)
    michaelangelo.showturtle()


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(position_x, position_y, new_x, new_y, obstacles1):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    print("in pos allowed, ", position_x, position_y, new_x, new_y, obstacles1)

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
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, michaelangelo
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
        michaelangelo.forward(steps)

        return True, reason
    return False, reason



def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index, michaelangelo

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    michaelangelo.right(90)

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index, michaelangelo

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    michaelangelo.left(90)

    return True, ' > '+robot_name+' turned left.'


def teardown():
    """
    Terminate turtle module.
    """
    turtle.bye()

# initialise()
# update_position(50)
# do_right_turn("poop")
# update_position(150)

# Step 4: We're done!
# initialise()
# draw_outline()

