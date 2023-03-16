import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        html = response.data.decode()
        assert "<a class=\"btnText\" href=\"/recommend\">Find Your Next Book</a>" in html
        self.assertEqual(response.status_code, 200)

    def test_recommend_ui(self):
        response = self.app.get('/recommend')
        html = response.data.decode()
        assert "<input type=\"submit\" class=\"searchBtn\" value=\"Search\" />" in html
        self.assertEqual(response.status_code, 200)

    def test_recommend(self):
        payload = {
            "searchBy": "author",
            "userInput": "J. K. Rowling"
        }
        response = self.app.post('/recommend_books', data=payload)
        html = response.data.decode()
        assert "<div class=\"bookCard\">" in html
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()