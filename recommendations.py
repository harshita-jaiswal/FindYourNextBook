# %% [markdown]
# ## Data Loading

# %%
#importing python libraries
import pandas as pd
import numpy as np
import pickle

# %%
#loading datasets
df_books = pd.read_csv('Dataset/Books.csv', low_memory=False)
df_ratings = pd.read_csv('Dataset/Ratings.csv')
df_users = pd.read_csv('Dataset/Users.csv')

# %%
#set seed for reproducibility
np.random.seed(0)

# %% [markdown]
# ## Preprocessing on Books dataset

# %%
#first five rows of books dataset
df_books.head()

# %%
#number of missing values in books dataset
missing_books_count = df_books.isnull().sum()
missing_books_count

# %%
#dropping unrequired columns in books dataset
df_books.drop(['Image-URL-S', 'Image-URL-L'], axis = 1, inplace = True)

# %%
#uppercasing ISBN
df_books['ISBN'].str.upper()

# %%
#replacing null author and publisher with other
null_Author = np.where(df_books['Book-Author'].isnull())
null_publisher = np.where(df_books['Publisher'].isnull())

df_books.at[null_Author[0][0],'Book-Author'] = 'Other'
df_books.at[null_publisher[0][0],'Publisher'] = 'Other'
df_books.at[null_publisher[0][1],'Publisher'] = 'Other'

# %%
#get all the unique values of year of publication
years = df_books['Year-Of-Publication'].unique().sort()


# %%
#checking data for 'DK Publishing Inc'
df_books.loc[df_books['Year-Of-Publication'] == 'DK Publishing Inc',:]

# %%
#editing data for DK Publishing Inc
df_books.at[209538,'Book-Author'] = 'Other'
df_books.at[209538,'Year-Of-Publication'] = 2000
df_books.at[209538,'Publisher'] = 'DK Publishing Inc'

df_books.at[221678,'Book-Author'] = 'Other'
df_books.at[221678,'Publisher'] = 'DK Publishing Inc'
df_books.at[221678,'Year-Of-Publication'] = 2000

# %%
#checking data for 'Gallimard'
df_books.loc[df_books['Year-Of-Publication'] == 'Gallimard',:]

# %%
#editing data for Gallimard
df_books.at[220731 ,'Book-Author'] = 'Other'
df_books.at[220731 ,'Publisher'] = 'Gallimard'
df_books.at[220731 ,'Year-Of-Publication'] = '2003'

# %%
#converting year of publication in int data type
df_books['Year-Of-Publication'] = df_books['Year-Of-Publication'].astype(int)

# %%
#selecting range which less than 2022
df_books.loc[df_books['Year-Of-Publication'] > 2022, 'Year-Of-Publication'] = 2002

#replacing Invalid years with max year
df_books.loc[df_books['Year-Of-Publication'] == 0, 'Year-Of-Publication'] = 2002

# %%
#duplicate rows in books dataset
duplicated_books = df_books.duplicated().sum()

# %% [markdown]
# ## Preprocessing on Users dataset

# %%
#first five rows of users dataset
df_users.head()

# %%
#number of missing values in users dataset
missing_users_count = df_users.isnull().sum()

# %%
#splitting location into city, state and country
locations_list = df_users.Location.str.split(', ')
location_count = len(locations_list)
cities_list = []
states_list = []
countries_list = []
for location in range(0, location_count):
    if locations_list[location][0] == '' or locations_list[location][0] == 'n/a' or locations_list[location][0] == ' ':
        cities_list.append('Other')
    else: 
        cities_list.append(locations_list[location][0])

    if (len(locations_list[location]) < 2):
        states_list.append('Other')
        countries_list.append('Other')
    
    else: 
        if locations_list[location][1] == '' or locations_list[location][1] == 'n/a' or locations_list[location][1] == ' ':
            states_list.append('Other')
        else: 
            states_list.append(locations_list[location][1])
        
        if (len(locations_list[location]) < 3):
            countries_list.append('Other')
        
        else: 
            if locations_list[location][2] == '' or locations_list[location][2] == 'n/a' or locations_list[location][2] == ' ':
                countries_list.append('Other')
            else: 
                countries_list.append(locations_list[location][2])



# %%
#creating location dataframes
df_city = pd.DataFrame(cities_list, columns=['City'])
df_state = pd.DataFrame(states_list, columns = ['State'])
df_country = pd.DataFrame(countries_list, columns =['Country'])

df_location = pd.concat([df_city, df_state, df_country], axis=1)
df_location

# %%
#converting location to lowercase
df_location['City'] = df_location['City'].str.lower()
df_location['State'] = df_location['State'].str.lower()
df_location['Country'] = df_location['Country'].str.lower()

# %%
#adding locations to df_users
df_users = pd.concat([df_users, df_location], axis = 1)
df_users

# %%
#dropping location from users dataset
df_users.drop(['Location'], axis = 1, inplace = True)

# %%
#age preprocessing
ages = df_users['Age'].unique().sort()
considerable_age = df_users[df_users['Age'] <= 98] 
considerable_age = considerable_age[considerable_age['Age'] >= 8]
average_age = round(considerable_age['Age'].mean())


# %%
#replacing ages that don't fall in range with average
df_users.loc[df_users['Age'] > 98, 'Age'] = average_age
df_users.loc[df_users['Age'] < 8, 'Age'] = average_age

# %%
#filling missing age with average age 
#changing age data type to int
df_users['Age'] = df_users['Age'].fillna(average_age)

df_users['Age'] = df_users['Age'].astype(int)

# %%
#duplicate users in books dataset
duplicated_users = df_users.duplicated().sum()
duplicated_users

# %% [markdown]
# ## Preprocessing on Ratings dataset

# %%
#first five rows of ratings dataset
df_ratings.head()

# %%
#number of missing values in ratings dataset
missing_ratings_count = df_ratings.isnull().sum()
missing_ratings_count

# %%
#checking data type of 'Book-Rating'
df_ratings.dtypes

# %%
#uppercasing ISBN
df_books['ISBN'].str.upper()

# %%
#duplicate ratings in books dataset
duplicated_ratings = df_ratings.duplicated().sum()
duplicated_ratings

# %% [markdown]
# ## Dataset Merging

# %%
df_recommendation_dataset = pd.merge(df_books, df_ratings, on="ISBN")
df_recommendation_dataset = pd.merge(df_recommendation_dataset, df_users, on="User-ID")

# %%
df_recommendation_dataset.head()

# %%
#books with ratings
df_books_with_ratings = df_recommendation_dataset[df_recommendation_dataset['Book-Rating'] != 0]
df_books_with_ratings = df_books_with_ratings.reset_index(drop = True)

# %%
#books without ratings
df_books_without_ratings = df_recommendation_dataset[df_recommendation_dataset['Book-Rating'] == 0]
df_books_without_ratings = df_books_without_ratings.reset_index(drop = True)

# %% [markdown]
# ## TOP 50 Books

# %%
#calculating total number of ratings for each book
df_ratings_count = df_books_with_ratings.groupby('Book-Title').count()['Book-Rating'].reset_index()
df_ratings_count = df_ratings_count.sort_values('Book-Rating', ascending=False)

# %%
#calculating average ratings 
df_average_rating = df_books_with_ratings.groupby('Book-Title').mean(numeric_only = True)['Book-Rating'].reset_index()
df_average_rating.rename(columns={'Book-Rating':'Average-Rating'},inplace=True)
df_average_rating = df_average_rating.sort_values('Average-Rating', ascending=False)


# %%
#merging total-ratings and average-ratings dataset
df_popular_books = pd.merge(df_ratings_count, df_average_rating, on="Book-Title")

# %%
#filter to consider total-ratings atleast more than 200
df_top_books = df_popular_books[df_popular_books['Book-Rating']>=200].sort_values('Average-Rating',ascending=False)

# %%
#merge with books for display
df_top_books = df_top_books.merge(df_books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M', 'Book-Rating', 'Average-Rating']]
df_top_books.reset_index(inplace=True)

# %%
def get_top_books():
    top_books = pickle.dump(df_top_books, open('top_books.pkl', 'wb'))
    return top_books
get_top_books()

# %% [markdown]
# ## Books by same author and publisher

# %%
#calculating ratings count on all books
df_total_ratings_count = df_recommendation_dataset.groupby('Book-Title').count()['Book-Rating'].reset_index()
df_total_ratings_count = df_total_ratings_count.sort_values('Book-Rating', ascending=False)

# %%
#calculating average ratings on all books
df_average_books_rating = df_recommendation_dataset.groupby('Book-Title').mean(numeric_only = True)['Book-Rating'].reset_index()
df_average_books_rating.rename(columns={'Book-Rating':'Average-Rating'},inplace=True)

# %%
# merging all the books
df_all_books = df_total_ratings_count.merge(df_average_books_rating,on='Book-Title')

# %%
#calculating aggregared rating
df_author_recommendations = df_all_books.sort_values('Average-Rating', ascending=False)
df_author_recommendations["Aggregated-Rating"] = df_author_recommendations['Book-Rating']*df_author_recommendations['Average-Rating']

# %%
#merging with books
df_author_recommendations = df_author_recommendations.merge(df_books,on='Book-Title').drop_duplicates('Book-Title')
df_author_recommendations=df_author_recommendations.sort_values('Aggregated-Rating',ascending=False)

# %%
#Helper method to create books in custom list from dataframe
def create_book_lists_helper(books):
    recommended_books = []
    for book in books.values.tolist():
        suggested = []
        suggested.append(book[0])
        suggested.append(book[5])
        suggested.append(book[8])
        recommended_books.append(suggested)
    return recommended_books

# %%
#Recommend books by same author of the book with bookname as an input  
def recommendation_by_same_author(bookname):
    book_entry = df_author_recommendations[df_author_recommendations['Book-Title'] == bookname]
    if book_entry.empty:
        return "No books found with the input title!"
    book_author = book_entry['Book-Author']
    author_name = book_author.to_string(index=False)
    author_recommendations = df_author_recommendations.loc[df_author_recommendations['Book-Author'] == author_name,:][:6]
    author_recommendations.drop(author_recommendations.index[author_recommendations['Book-Title'] == bookname], inplace = True)
    if author_recommendations.empty:
        return "No books found with the author of the input title!"
    return create_book_lists_helper(author_recommendations)

# %%
print(recommendation_by_same_author("Harry Potter and the Chamber of Secrets"))
# %%
def recommendation_by_same_publisher(bookname):
    book_entry = df_author_recommendations[df_author_recommendations['Book-Title'] == bookname]
    if book_entry.empty:
        return "No books found with the input title!"
    book_publisher = book_entry['Publisher']
    publisher_name = book_publisher.to_string(index=False)
    publisher_recommendations = df_author_recommendations.loc[df_author_recommendations['Publisher'] == publisher_name,:][:6]
    publisher_recommendations.drop(publisher_recommendations.index[publisher_recommendations['Book-Title'] == bookname], inplace = True)
    if publisher_recommendations.empty:
        return "No books found with the publisher of the input title!"
    return create_book_lists_helper(publisher_recommendations) 

#%%
print(recommendation_by_same_publisher("Harry Potter and the Chamber of Secrets"))

# %% [markdown]
# ## collaborative filtering

# %%
#fetching experienced users who have rated at least 200 books
collaborative_user_data = df_recommendation_dataset.groupby('User-ID').count()['Book-Rating'] > 200
experienced_users = collaborative_user_data[collaborative_user_data].index

df_filtered_collaborative_data = df_recommendation_dataset[df_recommendation_dataset['User-ID'].isin(experienced_users)]

# %%
#fetching books with minimum 50 ratings by users
collaborative_rating_data = df_filtered_collaborative_data.groupby('Book-Title').count()['Book-Rating'] > 50
books_with_experienced_ratings = collaborative_rating_data[collaborative_rating_data].index 

df_final_collaborative_data = df_filtered_collaborative_data[df_filtered_collaborative_data['Book-Title'].isin(books_with_experienced_ratings)]

# %%
#creating pivot table
df_pivot_table = df_final_collaborative_data.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
df_pivot_table.fillna(0, inplace=True)

# %%
df_pivot_table

# %%
#similarity-scores
from sklearn.metrics.pairwise import cosine_similarity
df_similarity_scores = cosine_similarity(df_pivot_table)

# %%
def collaborative_recommendation(book_name):
    book_index = np.where(df_pivot_table.index==book_name)[0][0]
    similar_books = sorted(list(enumerate(df_similarity_scores[book_index])),key=lambda x:x[1],reverse=True)[1:5]
    
    recommended_books = []
    for book in similar_books:
        books = []
        temp_df = df_books[df_books['Book-Title'] == df_pivot_table.index[book[0]]]
        books.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        books.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        books.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        recommended_books.append(books)
    
    return recommended_books

# %%
collaborative_recommendation('1st to Die: A Novel')

# %%
pickle.dump(df_pivot_table, open('pivot_table.pkl', 'wb'))
pickle.dump(df_similarity_scores, open('similarity_scores.pkl', 'wb'))
pickle.dump(df_books,open('books.pkl', 'wb'))

# %% [markdown]
# ## Books Published Yearly

# %%
#year as input
def getBooksYearly(year):
    year = int(year)
    user_year = ((df_recommendation_dataset['Year-Of-Publication'] == year))
    if user_year.any(): 
        same_year_books = df_recommendation_dataset[df_recommendation_dataset['Year-Of-Publication'] == year]
        #top 5 rated books
        same_year_books = same_year_books.sort_values(by = "Book-Rating", ascending=False)[:5]
        if (len(same_year_books) == 0):
            return "No books found in this year!"
        same_year_books = list(zip(same_year_books['Book-Title'], same_year_books['Book-Author'], same_year_books['Image-URL-M']))
        message = "Trending books in the same year"
        result = {"title": message,"books":same_year_books}
        return result
    else:
        return "Invalid year!"

# %%
#book name as input
def getBooksYearlyByName(book_name):
    same_year_books_bookname = df_recommendation_dataset[df_recommendation_dataset['Book-Title'].str.lower().str.contains(book_name.lower())]
    if same_year_books_bookname.empty:
        return "No books found with that title!"
    else:
        year = same_year_books_bookname.iloc[0]['Year-Of-Publication']
        same_year_books_bookname = df_recommendation_dataset[df_recommendation_dataset['Year-Of-Publication'] == year]
         #top 5 rated books
        same_year_books_bookname = same_year_books_bookname.sort_values(by = "Book-Rating", ascending=False)[:5]
        if (len(same_year_books_bookname)==0):
            return "No books found in the same year!"
        same_year_books_bookname = same_year_books_bookname.drop_duplicates(subset=["Book-Title"])
        same_year_books_bookname = list(zip(same_year_books_bookname['Book-Title'], same_year_books_bookname['Book-Author'], same_year_books_bookname['Image-URL-M']))
        message = "Trending books in the same year"
        result = {"title": message,"books":same_year_books_bookname}
        return result


