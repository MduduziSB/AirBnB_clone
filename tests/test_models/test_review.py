#!/usr/bin/python3
"""Tests for review"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the review class"""
    def test_attributes(self):
        review1 = Review()
        self.assertEqual(review1.place_id, "")
        self.assertEqual(review1.user_id, "")
        self.assertEqual(review1.text, "")


if __name__ == "__main__":
    unittest.main()
