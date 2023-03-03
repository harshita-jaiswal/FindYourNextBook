from flask import Flask,render_template, request
import pickle
import numpy as np

from recommendations import getBooksYearly
from recommendations import samePlaceBooks
from recommendations import getAllRecommendations

top_books = pickle.load(open('top_books.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    print('top book----', top_books)
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
    # year_or_book = request.form.get("user_input")
    # same_year_books = getBooksYearly(year_or_book)

    # #places data
    # place = request.form.get("user-input")
    # same_place_books = samePlaceBooks(place)

    # #result
    # all_books = []
    # all_books.append(same_year_books)
    # all_books.append(same_place_books)
    # print(all_books)
    # return render_template('searchBooks.html')
    # user_input = request.form.get('user_input')
    book_name = request.form.get('user_input')
    # year = request.form.get('user_input')
    # same_year_books_by_name = getBooksYearlyByName(book_name)
    bookList = [
    {
        "title": "recommendation_by_same_author",
        "books": [
            {
                "name": "Daddy's Little Girl",
                "cover": "http://images.amazon.com/images/P/0743206045.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "On the Street Where You Live",
                "cover": "http://images.amazon.com/images/P/0671004530.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "Pretend You Don't See Her",
                "cover": "http://images.amazon.com/images/P/0671867156.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "All Around the Town",
                "cover": "http://images.amazon.com/images/P/0671793489.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "We'll Meet Again",
                "cover": "http://images.amazon.com/images/P/0671004565.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "Loves Music, Loves to Dance",
                "cover": "http://images.amazon.com/images/P/0671758896.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            }
        ]
    },
    {
        "title": "recommendation_by_same_publisher",
        "books": [
            {
                "name": "The Color Purple",
                "cover": "http://images.amazon.com/images/P/0671617028.01.MZZZZZZZ.jpg",
                "author": "Alice Walker"
            },
            {
                "name": "Deadly Decisions",
                "cover": "http://images.amazon.com/images/P/0671028367.01.MZZZZZZZ.jpg",
                "author": "Kathy Reichs"
            },
            {
                "name": "And Then There Were None",
                "cover": "http://images.amazon.com/images/P/0671704664.01.MZZZZZZZ.jpg",
                "author": "Agatha Christie"
            },
            {
                "name": "From a Buick 8",
                "cover": "http://images.amazon.com/images/P/0743417682.01.MZZZZZZZ.jpg",
                "author": "Stephen King"
            },
            {
                "name": "Coast Road: A Novel",
                "cover": "http://images.amazon.com/images/P/0671027662.01.MZZZZZZZ.jpg",
                "author": "Barbara Delinsky"
            }
        ]
    },
    {
        "title": "Top trending similar books",
        "books": [
            {
                "name": "Loves Music, Loves to Dance",
                "cover": "http://images.amazon.com/images/P/0671758896.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "I'll Be Seeing You",
                "cover": "http://images.amazon.com/images/P/0671888587.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "Before I Say Good-Bye",
                "cover": "http://images.amazon.com/images/P/0671004573.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            },
            {
                "name": "Daddy's Little Girl",
                "cover": "http://images.amazon.com/images/P/0743206045.01.MZZZZZZZ.jpg",
                "author": "Mary Higgins Clark"
            }
        ]
    },
    {
        "title": "Trending books in the same year",
        "books": [
            {
                "name": "Birdman",
                "cover": "http://images.amazon.com/images/P/038549694X.01.MZZZZZZZ.jpg",
                "author": "Mo Hayder"
            },
            {
                "name": "The Bad Beginning (A Series of Unfortunate Events, Book 1)",
                "cover": "http://images.amazon.com/images/P/0064407667.01.MZZZZZZZ.jpg",
                "author": "Lemony Snicket"
            },
            {
                "name": "Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))",
                "cover": "http://images.amazon.com/images/P/059035342X.01.MZZZZZZZ.jpg",
                "author": "J. K. Rowling"
            },
            {
                "name": "The Accidental Bride",
                "cover": "http://images.amazon.com/images/P/0553578960.01.MZZZZZZZ.jpg",
                "author": "Jane Feather"
            },
            {
                "name": "I Lost My Tooth! (Hello Reader. Level 1)",
                "cover": "http://images.amazon.com/images/P/0590642308.01.MZZZZZZZ.jpg",
                "author": "Hans Wilhelm"
            }
        ]
    }
]
    

    print('test----',book_name)
    # print(user_input)
    allResult = getAllRecommendations(book_name)
    print('value-------', allResult)
    # return render_template('searchBooks.html')

    return render_template('searchBooks.html', bookList=bookList)
    #year_or_book = request.form.get("user_input")
    #same_year_books = getBooksYearly(year_or_book)

    #places data
    #place = request.form.get("user-input")
    #same_place_books = samePlaceBooks(place)

    #result
    #all_books = []
    #all_books.append(same_year_books)
    #all_books.append(same_place_books)
    #print(all_books)

    
    # allResults = getAllRecommendations('1984')
    # print('allResults-------',allResults)
    # return render_template('searchBooks.html')

# if __name__== '__main__':
app.run(debug=True)
