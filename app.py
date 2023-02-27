from flask import Flask,render_template, request
import pickle
import numpy as np
from recommendations import getBooksYearly

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
    user_input = request.form.get('user_input')
    year = request.form.get('user_input')
    same_year_books = getBooksYearly(year)
    print(year)
    print(same_year_books)
    
    
    return render_template('searchBooks.html')

# if __name__== '__main__':
app.run(debug=True)
