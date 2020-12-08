import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from maze import mazerunner
import maze.obstacles as obstacles
import robot


class TestMazerun(unittest.TestCase):

    def test_at_the_top_edge(self):
        self.assertTrue(mazerunner.at_the_edge('top', (0,200)))
        self.assertFalse(mazerunner.at_the_edge('top', (0,99)))

    def test_at_the_bottom_edge(self):
        self.assertTrue(mazerunner.at_the_edge('bottom', (0,-200)))
        self.assertFalse(mazerunner.at_the_edge('bottom', (0,-99)))

    def test_at_the_right_edge(self):
        self.assertTrue(mazerunner.at_the_edge('right', (100,50)))
        self.assertFalse(mazerunner.at_the_edge('right', (10,-99)))

    def test_at_the_left_edge(self):
        self.assertTrue(mazerunner.at_the_edge('left', (-100,50)))
        self.assertFalse(mazerunner.at_the_edge('left', (10,-99)))


   
