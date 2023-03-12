import unittest
from recommendations import getAllRecommendationsByAuthorName


class TestRecommendationsByAuthor(unittest.TestCase):

    def test_Author_By_AuthorName_Results_Success(self):
        input = 'J. K. Rowling'
        results = getAllRecommendationsByAuthorName(input)
        self.assertIn('Similar top Books', results)

    def test_Author_By_AuthorName_NoResults_Success(self):
        input = 'askdjbfjhdasbc'
        results = getAllRecommendationsByAuthorName(input)
        self.assertIn('oops!', results)

if __name__ == '__main__':
    unittest.main()


