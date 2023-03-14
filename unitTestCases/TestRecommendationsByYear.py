import unittest
from recommendations import getBooksYearly

class TestRecommendationsByYear(unittest.TestCase):
    def test_valid_year(self):
        year = 2000
        result = getBooksYearly(year)
        self.assertIn("Trending books in the same year", result.title)
        self.assertEqual(len(result.books), 5)

    def test_year_as_string(self):
        year = "2000"
        result = getBooksYearly(year)
        self.assertIn("Trending books in the same year", result.title)
        self.assertEqual(len(result.books), 5)

    def test_invalid_year(self):
        year = 1200
        result = getBooksYearly(year)
        self.assertIn("oops! Please input the valid year between 1900 - 2022", result.title)
        self.assertEqual(len(result.books), 0)

    def test_book_title(self):
        result = getBooksYearly("harry potter")
        self.assertIn("Trending books in the same year", result.title)
        self.assertEqual(len(result.books), 5)

    def test_book_title_no_result(self):
        result = getBooksYearly("not a valid book title")
        self.assertIn("oops! No yearly recommendations for the input", result.title)
        self.assertEqual(len(result.books), 0)

if __name__ == '__main__':
    unittest.main()