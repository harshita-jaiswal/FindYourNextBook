from flask import Flask,render_template, request
import pickle
import numpy as np

top_100_books = pickle.load(open('top_100.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
    book_name = list(top_100_books['Book-Title'].values),
    book_author = list(top_100_books['Book-Author'].values),
    book_image = list(top_100_books['Image-URL-M'].values)
    )

# if __name__== '__main__':
app.run(debug=True)
