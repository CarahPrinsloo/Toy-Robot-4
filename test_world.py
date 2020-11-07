import unittest
import world.world
import world.turtle.world
import robot


class test_the_turtle_package_world(unittest.TestCase):

    def test_update_position_turtle_move_forward(self):
        world.turtle.world.current_direction_index = 0
        moved = world.turtle.world.update_position(10)
        self.assertTrue(moved)

    
    def test_update_position_turtle_move_back(self):
        world.turtle.world.current_direction_index = 2
        moved = world.turtle.world.update_position(10)
        self.assertTrue(moved)


    def test_update_position_turtle_move_left(self):
        world.turtle.world.current_direction_index = 3
        moved = world.turtle.world.update_position(0)
        self.assertTrue(moved)


    def test_update_position_turtle_move_right(self):
        world.turtle.world.current_direction_index = 1
        moved = world.turtle.world.update_position(0)
        self.assertTrue(moved)


class test_the_normal_package_world(unittest.TestCase):

    def test_update_position_move_forward(self):
        world.world.current_direction_index = 0
        moved, output = world.world.update_position(10)
        self.assertTrue(moved)

    
    def test_update_position_move_back(self):
        world.world.current_direction_index = 2
        moved, output = world.world.update_position(10)
        self.assertTrue(moved)


    def test_update_position_move_left(self):
        world.world.current_direction_index = 3
        moved, output = world.world.update_position(0)
        self.assertTrue(moved)


    def test_update_position_move_right(self):
        world.world.current_direction_index = 1
        moved, output = world.world.update_position(0)
        self.assertTrue(moved)

if __name__ == "__main__":
    unittest.main()