import unittest
import robot
#import world.world

class TestFunctions(unittest.TestCase):


    def test_update_history_add_non_replay_command_1(self):
        history = ['forward 10']
        robot.update_history('forward 5', history)
        self.assertEqual(history, ['forward 10', 'forward 5'])


    def test_update_history_add_non_replay_command_2(self):
        history = ['forward 10']
        robot.update_history('back 5', history)
        self.assertEqual(history, ['forward 10', 'back 5'])


    def test_update_history_add_non_replay_command_3(self):
        history = ['forward 10']
        robot.update_history('right', history)
        self.assertEqual(history, ['forward 10', 'right'])


    def test_update_history_add_non_replay_command_4(self):
        history = ['forward 10']
        robot.update_history('left', history)
        self.assertEqual(history, ['forward 10', 'left'])


    def test_update_history_not_add_replay_command(self):
        history = ['forward 10']
        robot.update_history('replay 10', history)
        self.assertEqual(history, ['forward 10'])


    def test_valid_command_with_valid_forward_movement(self):
        command = 'forward 3'
        valid = robot.valid_command(command)
        self.assertTrue(valid)

    
    def test_valid_command_with_invalid_forward_movement(self):
        command = 'forward n'
        valid = robot.valid_command(command)
        self.assertFalse(valid)


    def test_valid_command_with_valid_back_movement(self):
        command = 'back 15'
        valid = robot.valid_command(command)
        self.assertTrue(valid)

    
    def test_valid_command_with_invalid_back_movement(self):
        command = 'back na'
        valid = robot.valid_command(command)
        self.assertFalse(valid)


    def test_valid_command_with_valid_right_movement(self):
        command = 'right'
        valid = robot.valid_command(command)
        self.assertTrue(valid)


    def test_valid_command_with_invalid_right_movement(self):
        command = 'right abc'
        valid = robot.valid_command(command)
        self.assertFalse(valid)


    def test_valid_command_with_valid_left_movement(self):
        command = 'left'
        valid = robot.valid_command(command)
        self.assertTrue(valid)


    def test_valid_command_with_invalid_left_movement(self):
        command = 'left abc'
        valid = robot.valid_command(command)
        self.assertFalse(valid)


    def test_split_command_input_valid_forward_command(self):
        command = 'forward 3'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'forward')
        self.assertEqual(args1, '3')
        self.assertEqual(args2, '')


    def test_split_command_input_invalid_forward_command_1(self):
        command = 'forward abc'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'forward abc')
        self.assertEqual(args1, '')
        self.assertEqual(args2, '')


    def test_split_command_input_invalid_forward_command_2(self):
        command = 'forward 15c'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'forward 15c')
        self.assertEqual(args1, '')
        self.assertEqual(args2, '')


    def test_split_command_input_valid_back_command(self):
        command = 'back 8'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'back')
        self.assertEqual(args1, '8')
        self.assertEqual(args2, '')


    def test_split_command_input_invalid_back_command_1(self):
        command = 'back abc'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'back abc')
        self.assertEqual(args1, '')
        self.assertEqual(args2, '')


    def test_split_command_input_invalid_back_command_2(self):
        command = 'back 15c'
        (command_name, args1, args2) = robot.split_command_input(command)
        self.assertEqual(command_name, 'back 15c')
        self.assertEqual(args1, '')
        self.assertEqual(args2, '')


    def test_do_replay_with_valid_normal_replay_command(self):
        history = ['forward 10']
        (do_next, command_output) = robot.do_replay('HAL', '', '', False, False, history)
        self.assertTrue(do_next)
        self.assertEqual(command_output, ' > HAL replayed 1 commands.')


    def test_do_replay_with_valid_normal_silent_replay_command(self):
        history = ['forward 10']
        (do_next, command_output) = robot.do_replay('HAL', '', '', True, False, history)
        self.assertTrue(do_next)
        self.assertEqual(command_output, ' > HAL replayed 1 commands silently.')


    def test_do_replay_with_valid_reversed_replay_command(self):
        history = ['forward 10', 'back 2']
        (do_next, command_output) = robot.do_replay('HAL', '', '', False, True, history)
        self.assertTrue(do_next)
        self.assertEqual(command_output, ' > HAL replayed 2 commands in reverse.')


    def test_do_replay_with_valid_reversed_silent_replay_command(self):
        history = ['forward 10', 'right']
        (do_next, command_output) = robot.do_replay('HAL', '', '', True, True, history)
        self.assertTrue(do_next)
        self.assertEqual(command_output, ' > HAL replayed 2 commands in reverse silently.')

if __name__ == "__main__":
    unittest.main()