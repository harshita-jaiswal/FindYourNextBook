import unittest

from recommendations import getAllRecommendationsByPublisherName
from recommendations import getAllRecommendationsByPublisherName
 
class TestRecommendationsByPublisher(unittest.TestCase):

    def test_Publisher_By_PublisherName_Results_Success(self):
        input = 'Bloomsbury'
        results = getAllRecommendationsByPublisherName(input)
        self.assertIn('Similar top Books', results)

    def test_Publisher_By_PublisherName_NoResults_Success(self):
        input = 'askdjbfjhdasbc'
        results = getAllRecommendationsByPublisherName(input)
        self.assertIn('oops!', results)

if __name__ == '__main__':
    unittest.main()


