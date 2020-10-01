import world
import random

def create_random_position_for_obstacle():
    obstacle_y = random.randint(-200,196)
    obstacle_x = random.randint(-100, 96)
    return (obstacle_x, obstacle_y)


def randomly_assign_sizes_of_obstacles(x1, y1):
    num = random.randint(0,10)
    x2, y2 = x1, y1
    if num % 2 == 0 and num < 5:
        x2 += 4
    elif num % 2:
        y2 += 4
    else:
        x2 += 4
        y2 += 4
    return (x2, y2)


def get_obstacles():
    obstacles = []
    amount_obstacles = random.randint(0,10)
    for i in range(amount_obstacles):
        x1, y1 = create_random_position_for_obstacle()
        x2, y2 = randomly_assign_sizes_of_obstacles(x1, y1)
        obstacles.append((x1, x2, y1, y2))
    return list(obstacles)


def is_position_blocked(x, y, obstacles):
    for obstacle in obstacles:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3]
        if (x >= start_x and x <= end_x) and (y >= start_y and y <= end_y):
            return True
    return False


def check_if_in_path_of_vertical_obstacle(x1, y1, x2, y2, obstacle):
    start_x, end_x, start_y, end_y  = obstacle[0], obstacle[1], obstacle[2], obstacle[3]

    #same x-axis
    if x1 == x2 and x2 == start_x:
        #movement into obstacle
        if y2 >= start_y and y2 <= end_y:
            return True
        #forwards movement
        if y1 <= start_y and y2 >= end_y:
            return True
        #backwards movement
        if y1 >= start_y and y2 <= end_y:
            return True
    #same y_axis
    elif y1 == y2 and (y2 >= start_y and y2 <= end_y):
        #movement into obstacle
        if x2 == start_x and x2 == end_x:
            return True
        #forwards movement
        if x1 <= start_x and x2 >= end_x:
            return True
        #backwards movement
        if x1 >= start_x and x2 <= end_x:
            return True
    return False


def check_if_in_path_of_horizontal_obstacle(x1, y1, x2, y2, obstacle):
    start_x, end_x, start_y, end_y  = obstacle[0], obstacle[1], obstacle[2], obstacle[3]

    #same y-axis
    if y1 == y2 and y2 == start_y:
        #movement into obstacle
        if x2 >= start_x and x2 <= end_x:
            return True
        #forwards movement
        if x1 <= start_x and x2 >= end_x:
            return True
        #backwards movement
        if x1 >= start_x and x2 <= end_x:
            return True
    #same x_axis
    elif x1 == x2 and (x2 >= start_x and x2 <= end_x):
        #movement into obstacle
        if y2 == start_y and y2 == end_y:
            return True
        #forwards movement
        if y1 <= start_y and y2 >= end_y:
            return True
        #backwards movement
        if y1 >= start_y and y2 <= end_y:
            return True
    return False


def check_if_in_path_of_square_obstacle(x1, y1, x2, y2, obstacle):
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



def is_path_blocked(x1,y1, x2, y2, obstacle_list):

    blocked = False

    if len(obstacle_list) == 0:
        return False

    for obstacle in obstacle_list:
        start_x, end_x, start_y, end_y = obstacle[0], obstacle[1], obstacle[2], obstacle[3],
        #vertical obstacle
        if (start_x == end_x) and not (start_y == end_y):
            blocked = check_if_in_path_of_vertical_obstacle(x1, y1, x2, y2, obstacle)
        #horizontal obstacle
        elif (start_y == end_y) and not (start_x == end_x):
            blocked = check_if_in_path_of_horizontal_obstacle(x1, y1, x2, y2, obstacle)
        #square obstacle
        elif (end_x - start_x == 4) and (end_y - start_y == 4):
            blocked = check_if_in_path_of_square_obstacle(x1, y1, x2, y2, obstacle)
        if blocked:
            return True

    return blocked


def print_obstacle_list(obstacles):
    print('There are some obstacles:')
    for obstacle in obstacles:
        print('- At position ' + str(obstacle[0]) + ',' + str(obstacle[2]) + ' (to ' + str(obstacle[1]) + ',' + str(obstacle[3]) + ')')