from flask import Flask,render_template, request
import pickle
import numpy as np

from recommendations import getBooksYearly
from recommendations import samePlaceBooks

top_books = pickle.load(open('top_books.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
    book_name = list(top_books['Book-Title'].values),
    book_author = list(top_books['Book-Author'].values),
    book_image = list(top_books['Image-URL-M'].values)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('searchBooks.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    #TAKE INPUT: bookname
    #display: similar trending books, books by same author, books by same publisher, books published in the same year, books published at same places

    #year data
    year_or_book = request.form.get("user_input")
    same_year_books = getBooksYearly(year_or_book)

    #places data
    place = request.form.get("user-input")
    same_place_books = samePlaceBooks(place)

    #result
    all_books = []
    all_books.append(same_year_books)
    all_books.append(same_place_books)
    print(all_books)
    return render_template('searchBooks.html')

# if __name__== '__main__':
app.run(debug=True)
