import unittest
from io import StringIO
import world.obstacles as _obstacles



class Testobstacles(unittest.TestCase):
    def test_no_obstacles(self):
        '''
        Test that there can be zero obstacles
        '''
        _obstacles.random.randint = lambda a, b: 0
        self.assertEqual(_obstacles.get_obstacles(), [])


    def test_is_position_blocked(self):
        '''
        Basic check to see if positions given intersect with obstacle (2,2)
        '''
        self.assertEqual(_obstacles.is_position_blocked(2,2, [(2,2)]), True)
        self.assertEqual(_obstacles.is_position_blocked(3,2, [(2,2)]), True)
        self.assertEqual(_obstacles.is_position_blocked(2,5, [(2,2)]), True)
        self.assertEqual(_obstacles.is_position_blocked(-2,2, [(2,2)]), False)
        self.assertEqual(_obstacles.is_position_blocked(0,10, [(2,2)]), False)


    def test_is_path_blocked_equal_x_true (self):
        '''
        Checks for vertical movement if there is an obstacle -True 
        '''
        self.assertEqual(_obstacles.is_path_blocked(2,1,2,5, [(2,2)]), True)
        self.assertEqual(_obstacles.is_path_blocked(2,0,2,3, [(2,2)]), True)


    def test_is_path_blocked_equal_x_false (self):
        '''
        Checks for vertical movement if there is an obstacle -False 
        '''
        self.assertEqual(_obstacles.is_path_blocked(1,1,1,5, [(2,2)]), False)
        self.assertEqual(_obstacles.is_path_blocked(-2,0,-2,3, [(2,2)]), False)


    def test_is_path_blocked_equal_y_true (self):
        '''
        Checks for horizontal movement if there is an obstacle -True 
        '''
        self.assertEqual(_obstacles.is_path_blocked(1,2,5,2, [(2,2)]), True)
        self.assertEqual(_obstacles.is_path_blocked(0,2,3,2, [(2,2)]), True)


    def test_is_path_blocked_equal_y_false (self):
        '''
        Checks for horizontal movement if there is an obstacle -False 
        '''
        self.assertEqual(_obstacles.is_path_blocked(10,2,20,2, [(2,2)]), False)
        self.assertEqual(_obstacles.is_path_blocked(6,2,30,2, [(2,2)]), False)
