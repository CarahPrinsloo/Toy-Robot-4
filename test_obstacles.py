import unittest
from world import obstacles
import robot

class TestFunctions(unittest.TestCase):


    def test_get_obstacles_is_square_obstacle(self):
        for obstacle in robot.obstacles:
            x1, x2, y1, y2 = obstacle[0], obstacle[1], obstacle[3], obstacle[4]
            self.assertEqual(x2, x1+4)
            self.assertEqual(y2, y1+4)


    def test_get_obstacles_in_limit(self):
        for obstacle in robot.obstacles:
            x1, x2, y1, y2 = obstacle[0], obstacle[1], obstacle[3], obstacle[4]
            self.assertTrue(x1 >= -100 and x1 <= 96)
            self.assertTrue(y1 >= -200 and y1 <= 196)
            self.assertEqual(x2, x1+4)
            self.assertEqual(y2, y1+4)


    def test_check_if_in_path_of_obstacle_blocked_1(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 0, 1, 1, 1
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertTrue(blocked)


    def test_check_if_in_path_of_obstacle_blocked_2(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 1, 1, 0, 1
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertTrue(blocked)


    def test_check_if_in_path_of_obstacle_blocked_3(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 5, 5, 6, 5
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertTrue(blocked)


    def test_check_if_in_path_of_obstacle_blocked_4(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 6, 5, 5, 5
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertTrue(blocked)


    def test_check_if_in_path_of_obstacle_not_blocked_1(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 0, 0, 0, 1
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertFalse(blocked)


    def test_check_if_in_path_of_obstacle_not_blocked_2(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 0, 1, 0, 0
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertFalse(blocked)


    def test_check_if_in_path_of_obstacle_not_blocked_3(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 6, 6, 5, 4
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertFalse(blocked)


    def test_check_if_in_path_of_obstacle_not_blocked_4(self):
        obstacle = (1, 5, 1, 5)
        x1, x2, y1, y2 = 6, 5, 6, 6
        blocked = obstacles.check_if_in_path_of_obstacle(x1, y1, x2, y2, obstacle)
        self.assertFalse(blocked)


if __name__ == "__main__":
    unittest.main()