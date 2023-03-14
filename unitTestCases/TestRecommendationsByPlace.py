import unittest
from recommendations import getsamePlaceBooks

class TestRecommendationsByPlace(unittest.TestCase):
    def test_valid_input(self):
        place = "portland"
        result = getsamePlaceBooks(place)
        self.assertIn("Trending books at the same location", result.title)
        self.assertEqual(len(result.books), 5)

    def test_unknown_input(self):
        place = "unknown country"
        result = getsamePlaceBooks(place)
        self.assertIn("oops! No recommendations for place input", result.title)
        self.assertEqual(len(result.books), 0)
    
    def test_invalid_input(self):
        place = None
        result = getsamePlaceBooks(place)
        self.assertIn("oops! No recommendations for place input", result.title)
        self.assertEqual(len(result.books), 0)

    def test_empty_input(self):
        place = " "
        result = getsamePlaceBooks(place)
        self.assertIn("oops! No recommendations for place input", result.title)
        self.assertEqual(len(result.books), 0)
    
    def test_case_insensitive_input(self):
        place = "CaliFORNIA"
        result = getsamePlaceBooks(place)
        self.assertIn("Trending books at the same location", result.title)
        self.assertEqual(len(result.books), 5)


if __name__ == '__main__':
    unittest.main()