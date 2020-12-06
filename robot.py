import sys
import os.path
import world.text.world as blueworld
import world.turtle.world as turtleworld
from maze import mazerunner



#list of mazes
# valid_mazes = [hiranya_maze, test_maze]

# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 
'sprint', 'mazerun']
move_commands = valid_commands[3:]

# variables tracking position and direction
directions = ['forward', 'right', 'back', 'left']

environment = None

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#commands history
history = []


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    print("The command you just gave is {}".format(command))
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, 
    as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 2)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    edge_list = ['top', 'bottom', 'left', 'right']
    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed','')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or arg1.lower() in edge_list)


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, 
SPRINT]
"""


def do_forward(robot_name, steps, obstacles):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :param obstacles:
    :return: (True, forward output text)
    """
    global environment

    can_update_position, reason = environment.update_position(steps, obstacles)

    if can_update_position:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        if reason == "obstacles":
            return True, ''+robot_name+': Sorry, there is an obstacle in the way'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps, obstacles):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    :param obstacles:
    """
    global environment

    if environment.update_position(-steps, obstacles):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_sprint(robot_name, steps, obstacles):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + 
    .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :param obstacles:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1, obstacles)
    else:
        (do_next, command_output) = do_forward(robot_name, steps, obstacles)
        print(command_output)
        return do_sprint(robot_name, steps - 1, obstacles)


def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into 
    (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of 
    command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command,
    e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments, obstacles):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :param obstacles:
    :return: True, output string
    """
    global environment

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name, obstacles)
        if not silent:
            print(command_output)
            environment.show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def do_mazerun(robot_name, edge, obstacles):
    print("The path that was found is to this: {} ".format(edge))
    path = mazerunner.astar_search(obstacles, edge)
    return environment.do_mazerun_path(path, obstacles, robot_name, edge)


def call_command(command_name, command_arg, robot_name, obstacles):
    global environment

    if command_name == 'help':
        return do_help()
    elif command_name == 'mazerun':
        return do_mazerun(robot_name, command_arg, obstacles)
    elif command_name == 'forward':
        return do_forward(robot_name, int(command_arg), obstacles)
    elif command_name == 'back':
        return do_back(robot_name, int(command_arg), obstacles)
    elif command_name == 'right':
        return environment.do_right_turn(robot_name)
    elif command_name == 'left':
        return environment.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return do_sprint(robot_name, int(command_arg), obstacles)
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg, obstacles)
    return False, None


def handle_command(robot_name, command, obstacles):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :param obstacles:
    :return: `True` if the robot must continue after the command, or else 
    `False` if robot must shutdown
    """
    global environment
    
    (command_name, arg) = split_command_input(command)

    print("command name is {}".format(command_name))
    print("arg name is {}".format(arg))

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name, obstacles)

    print(command_output)
    environment.show_position(robot_name)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)



# def robot_start(world_arg='text'):
def robot_start(world_arg, selected_maze):
    """This is the entry point for starting my robot"""

    global history, environment
    # global position_x, position_y, current_direction_index, history, environment

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    environment = blueworld
    if world_arg == 'turtle':
        environment = turtleworld

    obstacles = environment.initialise(selected_maze)

    history = []
    
    command = get_command(robot_name)
    while handle_command(robot_name, command, obstacles):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")
    environment.teardown()
    environment = None


if __name__ == "__main__":

    worldVariable = 'text'
    mazevariable = 'obstacles'

    for arg in sys.argv:
        if 'turtle' in arg:
            worldVariable = 'turtle'
        if os.path.isfile('maze/' + arg + '.py'):
            mazevariable = arg

    robot_start(worldVariable, mazevariable)

