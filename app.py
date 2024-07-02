import streamlit as st
import pandas as pd
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarty[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


    # Load the movies dictionary from the pickle file
with open('movies_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)

# Convert the dictionary to a pandas DataFrame
movies = pd.DataFrame(movies_dict)

similarty = pickle.load((open('similarty.pkl', 'rb')))

# Streamlit application title
st.title('MOVIE RECOMMENDER SYSTEM')

# Selectbox for movie titles
selected_movie_name = st.selectbox(
    'How would you like to be connected?', movies['title'].values)


if st.button('RECOMMEND'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
