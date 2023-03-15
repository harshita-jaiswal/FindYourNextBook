import unittest
from flask import Flask
import json
from app import app

class TestApp(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        self.app = app
    
    def test_home(self):
        self.app.get('/')
        self.assert_template_used('home.html')
        self.assert_context("book_name", list)
        self.assert_context("book_author", list)
        self.assert_context("book_image", list)

    def test_recommend(self):
        self.app.get('/recommend')
        self.assert_template_used('searchBooks.html')

    def test_recommend_books(self):
        self.app.get('/recommend_books')
        payload = json.dumps({
            "searchBy": "author",
            "userInput": "J. K. Rowling"
        })
        response = self.app.post('/recommend_books', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        self.assert_template_used('searchBooks.html')
        self.assert_context("bookList", list)

if __name__ == '__main__':
    unittest.main()