import unittest
from flask import Flask
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        # self.app = app
        self.app = app.test_client()
    
    def test_home(self):
        self.app.get('/')
        self.assertTemplateUsed('home.html')
        self.assertContext("book_name", list)
        self.assertContext("book_author", list)
        self.assertContext("book_image", list)

    def test_recommend_ui(self):
        self.app.get('/recommend')
        self.assertTemplateUsed('searchBooks.html')

    def test_recommend_books(self):
        self.app.get('/recommend_books')
        payload = json.dumps({
            "searchBy": "author",
            "userInput": "J. K. Rowling"
        })
        response = app.post('/recommend_books', data=payload)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'searchBooks.html')
        self.assertContext("bookList", list)

if __name__ == '__main__':
    unittest.main()