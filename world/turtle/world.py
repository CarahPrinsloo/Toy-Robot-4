import turtle
import world.obstacles
import robot

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def draw_filled_square_obstacle(start_x, end_x, start_y, end_y):
    '''Draws square obstacle on turtle map at indicated position'''

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        change_turtle_direction('right')
        turtle.forward(int(end_x) - int(start_x))
        change_turtle_direction('right')
        turtle.forward(int(end_y) - int(start_y))
    turtle.end_fill()
    turtle.penup()


def draw_obstacles_on_map():
    '''Draws all obstacles on turtle map'''

    turtle.color('red', 'red')
    for obstacle in robot.obstacles:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3]
        draw_filled_square_obstacle(start_x, end_x, start_y, end_y)
    reset_turtle_to_start()


def reset_turtle_to_start():
    '''Return turtle to position on turtle map where player starts game'''

    turtle.goto(0,0)
    turtle.color('black', 'black')
    change_turtle_direction('left')
    turtle.pendown()


def change_turtle_direction(direction):
    '''Moves turtle in direction indicated'''

    turtle.degrees()
    if direction == 'right':
        turtle.right(90)
    elif direction == 'left':
        turtle.left(90)


def draw_restricted_area(start_x, start_y, end_x, end_y):
    '''Draws restricted area on turtle map'''

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.color('red')
    change_turtle_direction('left')
    for i in range(2):
        turtle.forward(int(end_y) - int(start_y))
        change_turtle_direction('right')
        turtle.forward(int(end_x) - int(start_x))
        change_turtle_direction('right')
    turtle.penup()


def create_turtle_world():
    '''Create turtle map'''

    s = turtle.getscreen()
    turtle.title('My Turtle Robot World')
    turtle.setworldcoordinates(-100,-200,100,200)
    draw_restricted_area(-100,-200,100,200)
    draw_obstacles_on_map()


def show_position(robot_name):
    '''Prints position of turtle robot'''

    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def move_turtle():
    '''Move turtle on turtle map'''

    turtle.mode()
    try:
        turtle.goto(position_x, position_y)
    except:
        return False
    return True

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
        if move_turtle():
            return True, output
    return False, output