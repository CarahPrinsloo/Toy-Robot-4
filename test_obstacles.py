import unittest
import world.obstacles

class TestFunctions(unittest.TestCase):

    def test_create_random_position_for_obstacle(self):
        x, y = world.obstacles.create_random_position_for_obstacle()
        x_between_minus_100_and_96 = (x>=-100 and x<=96)
        y_between_minus_200_and_196 = (y>=-200 and y<=196)
        self.assertTrue(x_between_minus_100_and_96)
        self.assertTrue(y_between_minus_200_and_196)

    
    def test_randomly_assign_sizes_of_obstacles(self):
        x2, y2 = world.obstacles.randomly_assign_sizes_of_obstacles(2,3)
        completed = (x2 == 6) or (y2 == 7)
        self.assertTrue(completed)


    def test_get_obstacles(self):
        obstacles = world.obstacles.get_obstacles()
        obstacles_list_created = len(obstacles) >= 0
        self.assertTrue(obstacles_list_created)


    def test_is_position_blocked_vertical_obstacle_blocked_position(self):
        obstacles = [(4, 4, 0, 4)]
        x2, y2 = 4, 2
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertTrue(position_is_blocked)


    def test_is_position_blocked_horizontal_obstacle_blocked_position(self):
        obstacles = [(0, 4, 4, 4)]
        x2, y2 = 2, 4
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertTrue(position_is_blocked)


    def test_is_position_blocked_square_obstacle_blocked_position(self):
        obstacles = [(0, 4, 0, 4)]
        x2, y2 = 2, 2
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertTrue(position_is_blocked)


    def test_is_position_blocked_vertical_obstacle_not_blocked_position(self):
        obstacles = [(4, 4, 0, 4)]
        x2, y2 = 5, 2
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertFalse(position_is_blocked)


    def test_is_position_blocked_horizontal_obstacle_not_blocked_position(self):
        obstacles = [(0, 4, 4, 4)]
        x2, y2 = 2, 5
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertFalse(position_is_blocked)


    def test_is_position_blocked_square_obstacle_not_blocked_position(self):
        obstacles = [(0, 4, 0, 4)]
        x2, y2 = 5, 5
        position_is_blocked = world.obstacles.is_position_blocked(x2, y2, obstacles)
        self.assertFalse(position_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_blocks_path_1(self):
        obstacles = [(4, 4, 0, 4)]
        x1, x2 = 4, 4
        y1, y2 = -1, 5
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_blocks_path_2(self):
        obstacles = [(3, 3, 3, 7)]
        x1, x2 = 3, 3
        y1, y2 = 1, 4
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_blocks_path_3(self):
        obstacles = [(3, 3, 3, 7)]
        x1, x2 = 3, 3
        y1, y2 = 4, 1
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_blocks_path_4(self):
        obstacles = [(4, 4, 0, 4)]
        x1, x2 = 0, 5
        y1, y2 = 2, 2
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_does_not_block_path_1(self):
        obstacles = [(4, 4, 0, 4)]
        x1, x2 = 0, 3
        y1, y2 = 0, 0
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)


    def test_is_path_blocked_vertical_obstacle_that_does_not_block_path_2(self):
        obstacles = [(3, 3, 3, 7)]
        x1, x2 = 3, 3
        y1, y2 = 0, 2
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_blocks_path_1(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 1, 6
        y1, y2 = 3, 3
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_blocks_path_2(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 1, 4
        y1, y2 = 3, 3
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_blocks_path_3(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 4, 4
        y1, y2 = 1, 4
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_blocks_path_4(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 4, 4
        y1, y2 = 4, 1
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_does_not_block_path_1(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 0, 2
        y1, y2 = 3, 3
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)


    def test_is_path_blocked_horizontal_obstacle_that_does_not_block_path_2(self):
        obstacles = [(3, 7, 3, 3)]
        x1, x2 = 4, 4
        y1, y2 = 0, 2
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_blocks_path_1(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 6, 6
        y1, y2 = 0, 4
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_blocks_path_2(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 6, 6
        y1, y2 = 0, 6
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_blocks_path_3(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 6, 6
        y1, y2 = 4, 0
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_blocks_path_4(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 1, 6
        y1, y2 = 2, 2
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertTrue(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_does_not_block_path_1(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 1, 6
        y1, y2 = 6, 6
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)


    def test_is_path_blocked_square_obstacle_that_does_not_block_path_2(self):
        obstacles = [(3, 7, 1, 5)]
        x1, x2 = 2, 2
        y1, y2 = 0, 3
        path_is_blocked = world.obstacles.is_path_blocked(x1, y1, x2, y2, obstacles)
        self.assertFalse(path_is_blocked)

if __name__ == "__main__":
    unittest.main()