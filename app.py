from flask import Flask,render_template, request
import pickle
import numpy as np

from recommendations import getBooksYearlyByName


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

    user_input = request.form.get('user_input')
    book_name = request.form.get('user_input')
    year = request.form.get('user_input')
    same_year_books_by_name = getBooksYearlyByName(book_name)
    

    print(book_name)
    print(same_year_books_by_name)

    return render_template('searchBooks.html', same_year_books_by_name=same_year_books_by_name)

# if __name__== '__main__':
app.run(debug=True)
