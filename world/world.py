import world.obstacles

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

def show_position(robot_name):
    output = ' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').'
    print(output)
    update_text_file_with_robot_position(output)


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    if not (min_x <= new_x <= max_x and min_y <= new_y <= max_y):
        return False, ': Sorry, I cannot go outside my safe zone.'
    if world.obstacles.is_path_blocked(position_x, position_y, new_x, new_y):
        return False, ': Sorry, there is an obstacle in the way.'
    return True, ''


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + int(steps)
    elif directions[current_direction_index] == 'right':
        new_x = new_x + int(steps)
    elif directions[current_direction_index] == 'back':
        new_y = new_y - int(steps)
    elif directions[current_direction_index] == 'left':
        new_x = new_x - int(steps)

    allowed, output = is_position_allowed(new_x, new_y)
    if allowed:
        position_x = new_x
        position_y = new_y
        return True, output
    return False, output

def update_text_file_with_robot_position(output):
    file_object = open('world/text/world.txt', 'a')
    file_object.write(str(output))
    file_object.close()
    