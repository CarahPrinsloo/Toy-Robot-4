import world.world
import world.turtle.world
import world.obstacles
import sys

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent']

#mode: turtle/text
mode_is_turtle = False

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name, history):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    update_history(command.lower(), history)
    return command.lower()


def list_contains_only_numbers(num_list):
    for i in range(2):
        if not num_list[i].isdigit():
            return False
    return True


def set_replay_limits(args, index):

    limits = args[index].split('-')
    args[1] = limits[0]
    if len(args) > 2:
        args[2] = limits[1]
    else:
        args.append(limits[1])
    if not list_contains_only_numbers(limits):
        (args[0], args[1], args[2]) = '', '', ''


def is_move_with_steps(args):
    command_name = args[0].lower()
    if len(args) > 1 and (command_name == 'forward' or command_name == 'back' or command_name == 'sprint' or command_name == 'replay'):
        return True
    return False


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument1, argument2)
    """

    args = command.split(' ')
    if len(args) >= 2 and not args[len(args)-1].isdigit():
        for i in range(1, len(args)):
            if not '-' in args[i] and not args[i].isdigit():
                args[0] = str(args[0]) + ' ' + str(args[i])
                args[i] = ''
            elif '-' in args[i]:
                set_replay_limits(args, i)
            elif args[i].isdigit():
                args[1] = args[i]
            else:
                args[1] = ''
    elif not is_move_with_steps(args) and args[len(args)-1].isdigit():
        return '','',''
    args = list(filter(None, args))
    if len(args) < 1 or len(args) > 3:
        return '','',''
    if len(args) > 1:
        if len(args) == 2:
            return args[0], args[1], ''
        else:
            return args[0], args[1], args[2]
    return args[0], '', ''


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

    (command_name, arg1, arg2) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)) and (len(arg2) == 0 or is_int(arg2))


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
"""


def do_forward(robot_name, steps, silent, obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if mode_is_turtle:
        position_was_updated, output = world.turtle.world.update_position(steps, obstacle_list)
    else:
        position_was_updated, output = world.world.update_position(steps, obstacle_list)

    if position_was_updated and not silent:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif silent:
        return True, ''
    else:
        return True, ''+ robot_name + str(output)


def do_back(robot_name, steps, silent, obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if mode_is_turtle:
        position_was_updated = world.turtle.world.update_position(-steps, obstacle_list)
    else:
        position_was_updated = world.world.update_position(-steps, obstacle_list)

    if position_was_updated and not silent:
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif not silent:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    else:
        return True, ''


def do_right_turn(robot_name, silent):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """

    if mode_is_turtle:
        world.turtle.world.current_direction_index += 1
        if world.turtle.world.current_direction_index > 3:
            world.turtle.world.current_direction_index = 0
        world.turtle.world.change_turtle_direction('right')
        world.turtle.world.move_turtle()
    else:
        world.world.current_direction_index += 1
        if world.world.current_direction_index > 3:
            world.world.current_direction_index = 0

    if not silent:
        text = ' > '+robot_name+' turned right.'
    else:
        text = ''
    return True, text


def do_left_turn(robot_name, silent):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """

    if mode_is_turtle:
        world.turtle.world.current_direction_index -= 1
        if world.turtle.world.current_direction_index < 0:
            world.turtle.world.current_direction_index = 3
        world.turtle.world.change_turtle_direction('left')
        world.turtle.world.move_turtle()
    else:
        world.world.current_direction_index -= 1
        if world.world.current_direction_index < 0:
            world.world.current_direction_index = 3

    if not silent:
        return True, ' > '+robot_name+' turned left.'
    else:
        return True, ''


def do_sprint(robot_name, steps, silent):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1, silent)
    else:
        (do_next, command_output) = do_forward(robot_name, steps, silent)
        if not silent:
            print(command_output)
        return do_sprint(robot_name, int(steps) - 1, silent)


def output_replay(robot_name, reversed, silent, commands_performed):
    '''Returns output that will be printed after replay performed'''

    if reversed and silent: #reversed, silent replay
        output = ' > '+robot_name+' replayed '+str(commands_performed)+ ' commands in reverse silently.'
    elif reversed: #reversed replay
        output = ' > '+robot_name+' replayed '+str(commands_performed)+ ' commands in reverse.'
    elif silent: #normal, silent replay
        output = ' > '+robot_name+' replayed '+str(commands_performed)+ ' commands silently.'
    else: #normal replay
        output = ' > '+robot_name+' replayed '+str(commands_performed)+ ' commands.'
    return output
    

def calculate_start_and_end_of_replay_execution(start, end, reversed, history):
    """Calculates start and end index of moves (incl.) that need to be replayed from history"""
    
    #either/both start and end is given
    if start.isdigit():
        if end.isdigit():
            if (int(start) - int(end)) < 1:
                end = 0
                start = 0
            elif reversed:
                temp_start = start
                start = (len(history)-1) - int(end)
                end = len(history) - int(temp_start)
            else:
                start = len(history) - int(start)
                end = (len(history)-1) - int(end)
        elif end == '':
            if reversed:
                start = len(history) - int(start)
                end = 0
            else:
                start = len(history) - int(start)
                end = len(history) - 1
    #neither start or end is given
    elif not end.isdigit():
        start = 0 
        end = len(history) - 1
        if reversed:
            start = len(history) - 1
            end = 0

    return start, end


def reversed_replay(robot_name, arg1, arg2, silent, history):
    '''Executes reversed replay mode'''

    commands_performed = 0
    (start_index, end_index) = calculate_start_and_end_of_replay_execution(arg1, arg2, True, history)
    
    if len(history) == 0:
        return True, output_replay(robot_name, reversed, silent, commands_performed)       
    
    for i in range(start_index, end_index-1, -1):
        command = history[i]
        handle_command(robot_name, command, silent, history)
        commands_performed += 1

    output = output_replay(robot_name, reversed, silent, commands_performed)       
    return True, output


def normal_replay(robot_name, arg1, arg2, silent, history):
    '''Executes normal replay mode'''
    
    commands_performed = 0
    (start_index, end_index) = calculate_start_and_end_of_replay_execution(arg1, arg2, False, history)
    
    if len(history) == 0:
        return True, output_replay(robot_name, False, silent, 0)
    for i in range(start_index, end_index+1):
        command = history[i]
        handle_command(robot_name, command, silent, history)
        commands_performed += 1

    output = output_replay(robot_name, False, silent, commands_performed)       
    return True, output   


def do_replay(robot_name, arg1, arg2, silent, reversed, history):
    """Choose correct replay mode and executes it"""
    
    if reversed: #reversed replay; silent/non-silent
        return reversed_replay(robot_name, arg1, arg2, silent, history)
    else: #normal replay; silent/non-silent
        return normal_replay(robot_name, arg1, arg2, silent, history)


def handle_command(robot_name, command, silent, history, obstacle_list):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg1, arg2) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg1), silent, obstacle_list)
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg1), silent, obstacle_list)
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name, silent)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name, silent)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, arg1, silent)
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(robot_name, arg1, arg2, False, False, history)
    elif command_name == 'replay silent':
        (do_next, command_output) = do_replay(robot_name, arg1, arg2, True, False, history)
    elif command_name == 'replay reversed':
        (do_next, command_output) = do_replay(robot_name, arg1, arg2, False, True, history)
    elif command_name == 'replay reversed silent':
        (do_next, command_output) = do_replay(robot_name, arg1, arg2, True, True, history)

    if not silent:
        print(command_output)
        if mode_is_turtle:
            world.turtle.world.show_position(robot_name)
        else:
            world.world.show_position(robot_name)
    return do_next


def update_history(command, history):
    
    args = command.split()
    if (args[0] == 'forward' or args[0] == 'back' or args[0] == 'right' or args[0] == 'left' or args[0] == 'sprint'):
        history.append(command)


def delete_content_of_text_file(filename):
    return open(filename,'w')


def get_mode_from_argv():
    if len(sys.argv) < 2:
        return 'text'
    return sys.argv[1]


def get_world_module_path():
    global mode_is_turtle
    mode = get_mode_from_argv()
    if mode == 'turtle':
        mode_is_turtle = True


def robot_start():
    """This is the entry point for starting my robot"""

    get_world_module_path()
    history = []
    obstacle_list = world.obstacles.get_obstacles()  

    if mode_is_turtle:
        world.turtle.world.position_x = 0
        world.turtle.world.position_y = 0
        world.turtle.world.current_direction_index = 0
        world.turtle.world.change_turtle_direction('left')
        world.turtle.world.draw_obstacles_on_map(obstacle_list)
    else:
        world.world.position_x = 0
        world.world.position_y = 0
        world.world.current_direction_index = 0
        
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    world.obstacles.print_obstacle_list(obstacle_list)
    

    command = get_command(robot_name, history)
    while handle_command(robot_name, command, False, history, obstacle_list):
        command = get_command(robot_name, history)
    
    delete_content_of_text_file('world/text/world.txt')   
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()