import unittest
import world.world
import world.turtle.world
import robot


class test_the_text_package_world(unittest.TestCase):

    def test_update_text_file_with_robot_position(self):
        content = ''
        world.world.update_text_file_with_robot_position(' > joe now at position (0,10).')
        file = open('world/text/world.txt', 'r')
        if file.mode == "r":
            content = file.read()
        self.assertEqual(' > joe now at position (0,10).', content)
        file.close()
        robot.delete_content_of_text_file('world/text/world.txt')


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

if __name__ == "__main__":
    unittest.main()