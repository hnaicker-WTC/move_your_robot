import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import maze.obstacles as obstacles
import robot


class Testrobot(unittest.TestCase):
    #reset histoy list
    del robot.history[:]
    
    def test_test_add_to_history(self):
        """
        Test append to history list
        """
        robot.add_to_history("back 10")
        self.assertEqual(robot.history, ["back 10"])
        del robot.history[:]

    def test_replay_silent(self):
        """
        Test for silent
        """
        self.assertEqual(robot.do_replay("HAL","silent", [()]), (True, " > HAL replayed 0 commands silently."))


    def test_replay_reversed(self):
        """
        Test correct for reveresed
        """
        self.assertEqual(robot.do_replay("HAL","reversed", [()]), (True, " > HAL replayed 0 commands in reverse."))


    def test_replay_silent_reversed(self):
        """
        Test for silent and reverse
        """
        self.assertEqual(robot.do_replay("HAL","silent reversed", [()]), (True, " > HAL replayed 0 commands in reverse silently."))

