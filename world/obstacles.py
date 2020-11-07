import random
import world
import robot


def get_obstacles():
    '''generates list of obstacles'''

    amount_obstacles = random.randint(0,10)
    for i in range(amount_obstacles):
        x1, y1 = random.randint(-100, 96), random.randint(-200,196)
        x2, y2 = x1 + 4, y1 + 4
        robot.obstacles.append((x1, x2, y1, y2))


def is_position_blocked(x, y):
    '''checks if (x,y) coordinates are occupied by obstacle
    ::returns True if (x,y) blocked'''

    for obstacle in robot.obstacles:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3]
        if (x >= start_x and x <= end_x) and (y >= start_y and y <= end_y):
            return True
    return False


def check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle):
    '''checks if (x,y) coordinates are in path of obstacle
    ::returns True if (x,y) is in path of obstacle'''

    start_x, end_x, start_y, end_y  = obstacle[0], obstacle[1], obstacle[2], obstacle[3]

    if (x1 == x2):
        if (x2 >= start_x and x2 <= end_x):
            #forwards movement into obstacle
            if (y1 <= start_y) and (y2 >= start_y and y2 <= end_y):
                return True
            #backwards movement into obstacle
            if (y1 >= start_y) and (y2 >= start_y and y2 <= end_y):
                return True
            #forwards obstacle in path
            if (y1 <= start_y) and (y2 >= start_y):
                return True
            #backwards obstacle in path
            if (y1 >= start_y) and (y2 <= start_y):
                return True
    if (y1 == y2):
        if (y2 >= start_y and y2 <= end_y):
            #forwards movement into obstacle
            if (x1 <= start_x) and (x2 >= start_x and x2 <= end_x):
                return True
            #backwards movement into obstacle
            if (x1 >= start_x) and (x2 >= start_x and x2 <= end_x):
                return True
            #forwards obstacle in path
            if (x1 <= start_x) and (x2 >= start_x):
                return True
            #backwards obstacle in path
            if (x1 >= start_x) and (x2 <= start_x):
                return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    '''checks if (x,y) coordinates are in path or blocked by obstacle
    ::returns True if (x,y) blocked/in path'''

    if len(robot.obstacles) == 0:
        return False
    for obstacle in robot.obstacles:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3],
        if (end_x - start_x == 4) and (end_y - start_y == 4):
            blocked = check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        if blocked:
            return True
    return False


def print_obstacle_list():
    '''prints list of obstacles in given format'''

    for i in range(0, len(robot.obstacles)):
        if i == 0:
            print('There are some obstacles:')
        obstacle = robot.obstacles[i]
        print('- At position ' + str(obstacle[0]) + ',' + str(obstacle[2]) + ' (to ' + str(obstacle[1]) + ',' + str(obstacle[3]) + ')')