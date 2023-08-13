#!/usr/bin/python3
"""Tests for user"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the state class"""
    def test_attributes(self):
        User1 = User()
        self.assertEqual(User1.email, "")
        self.assertEqual(User1.password, "")
        self.assertEqual(User1.first_name, "")
        self.assertEqual(User1.last_name, "")


if __name__ == "__main__":
    unittest.main()
