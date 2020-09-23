import turtle

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def execute_valid_move(move, steps):
    """Commands turtle to execute move
    ::returns true if move is executed"""

    moved = False
    if move == 'forward':
        turtle.forward(steps)
        moved = True
    elif move == 'back':
        turtle.back(steps)
        moved = True
    elif move == 'right':
        turtle.right(steps)
        moved = True
    elif move == 'left':
        turtle.left(steps)
        moved = True
    return moved   


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


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

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        if execute_valid_move(directions[current_direction_index], steps):
            return True
    return False