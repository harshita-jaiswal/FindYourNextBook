import unittest
from recommendations import getAllRecommendationsByBookName

class TestRecommendationsByCollaborativeFiltering(unittest.TestCase):

    def test_Collaborative_By_BookName_Results_Success(self):
        input = 'Harry Potter and the Chamber of Secrets (Book 2)'
        results = getAllRecommendationsByBookName(input)
        self.assertIn('Top trending', results)

    def test_Collaborative_By_BookName_NoResults_Success(self):
        input = 'askdjbfjhdasbc'
        results = getAllRecommendationsByBookName(input)
        self.assertIn('No Books found!', results)

if __name__ == '__main__':
    unittest.main()


