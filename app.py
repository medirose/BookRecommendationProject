import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import streamlit as st

# Data Preparation
df = pd.read_csv('/Users/medirose/Documents/GitHub/BookRecommendationProject/cleaned.csv')

# Ensure correct data types
df['user_id'] = df['user_id'].astype(int)
df['book_id'] = df['book_id'].astype(int)
df['gr_book_id'] = df['gr_book_id'].astype(int)
df['books_count'] = df['books_count'].astype(int)
df['year'] = df['year'].astype(int)
df['rating'] = df['rating'].astype(int)
df['ratings_count'] = df['ratings_count'].astype(int)

# Check for missing values in 'title', 'authors', 'isbn', and 'genre' columns
df = df.dropna(subset=['title', 'authors', 'isbn', 'genre'])

# Recommendation Engine
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'book_id', 'rating']], reader)

trainset, testset = train_test_split(data, test_size=0.2)
algo = SVD()
algo.fit(trainset)

# Define the function to get recommendations
def get_recommendations(user_id, num_recommendations=5):
    user_books = df[df['user_id'] == user_id]['book_id']
    recommendations = []
    for book_id in df['book_id'].unique():
        if book_id not in user_books.values:
            pred = algo.predict(user_id, book_id)
            recommendations.append((book_id, pred.est))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:num_recommendations]

# Streamlit Interface
st.title('RSMC Book Recommendation System')

user_id = st.number_input('Enter User ID', min_value=1, value=1)
num_recommendations = st.slider('Number of Recommendations', min_value=1, max_value=20, value=5)

if st.button('Get Recommendations'):
    recommendations = get_recommendations(user_id, num_recommendations)
    for book_id, rating in recommendations:
        book_info = df[df['book_id'] == book_id].iloc[0]
        st.write(f"Title: {book_info['title']}, Author: {book_info['authors']}, Rating: {rating:.2f}")

# Optionally, you can add some summary statistics or visualizations to the Streamlit app
# For example, you can display the distribution of ratings:
if st.checkbox('Show Rating Distribution'):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, ax = plt.subplots()
    sns.histplot(df['rating'], bins=5, kde=True, ax=ax)
    ax.set_title('Distribution of Ratings')
    st.pyplot(fig)
