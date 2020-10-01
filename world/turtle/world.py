import turtle
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
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def draw_vertical_obstacle(start_x, start_y, end_y):
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(int(end_y) - int(start_y))
    turtle.end_fill()


def draw_horizontal_obstacle(start_x, end_x, start_y):
    turtle.goto(start_x, start_y)
    turtle.pendown()
    change_turtle_direction('right')
    turtle.begin_fill()
    turtle.forward(int(end_x) - int(start_x))
    turtle.end_fill()
    change_turtle_direction('left')


def draw_square_obstacle(start_x, end_x, start_y, end_y):
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        change_turtle_direction('right')
        turtle.forward(int(end_x) - int(start_x))
        change_turtle_direction('right')
        turtle.forward(int(end_y) - int(start_y))
    turtle.end_fill()


def draw_obstacles_on_map(obstacles):
    turtle.color('red', 'red')
    for obstacle in obstacles:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3]
        turtle.penup()
        if start_x == end_x:
            draw_vertical_obstacle(start_x, start_y, end_y)
        elif start_y == end_y:
            draw_horizontal_obstacle(start_x, end_x, start_y)
        else:
            draw_square_obstacle(start_x, end_x, start_y, end_y)
    turtle.penup()
    reset_turtle_to_start()


def reset_turtle_to_start():
    turtle.goto(0,0)
    turtle.color('black', 'black')
    turtle.pendown()


def change_turtle_direction(move):
    turtle.degrees()
    if move == 'right':
        turtle.right(90)
    elif move == 'left':
        turtle.left(90)


def move_turtle():
    turtle.mode()
    try:
        turtle.goto(position_x, position_y)
    except:
        return False
    return True

def is_position_allowed(new_x, new_y, obstacle):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    if not (min_x <= new_x <= max_x and min_y <= new_y <= max_y):
        return False, ': Sorry, I cannot go outside my safe zone.'
    if world.obstacles.is_path_blocked(position_x, position_y, new_x, new_y, obstacle):
        return False, ': Sorry, there is an obstacle in the way.'
    return True, ''


def update_position(steps, obstacle_list):
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

    allowed, output = is_position_allowed(new_x, new_y, obstacle_list)
    if allowed:
        position_x = new_x
        position_y = new_y
        if move_turtle():
            return True, output
    return False, output