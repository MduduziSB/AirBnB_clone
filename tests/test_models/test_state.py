#!/usr/bin/python3
"""Tests for state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests the state class"""
    def test_attributes(self):
        state1 = State()
        self.assertEqual(state1.name, "")


if __name__ == "__main__":
    unittest.main()
