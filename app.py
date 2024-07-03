import streamlit as st
import pandas as pd
import pickle
import gdown
import os

# Function to download file from Google Drive


def download_file_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, destination, quiet=False)


# Download the similarty.pkl file if it doesn't exist
if not os.path.exists('similarty.pkl'):
    file_id = '1VgyGHGxbcEvaTYwYeQyFHYdam-w6KJy_'  # Google Drive file ID
    download_file_from_google_drive(file_id, 'similarty.pkl')


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

# Load the similarity matrix
with open('similarty.pkl', 'rb') as file:
    similarty = pickle.load(file)

# Streamlit application title
st.title('MOVIE RECOMMENDER SYSTEM')

# Selectbox for movie titles
selected_movie_name = st.selectbox(
    'How would you like to be connected?', movies['title'].values)

if st.button('RECOMMEND'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


# import streamlit as st
# import pandas as pd
# import pickle
# import gdown
# import os

# # Download the similarty.pkl file if it doesn't exist


# def download_file_from_google_drive(file_id, destination):
#     url = f"https://drive.google.com/uc?id={file_id}"
#     gdown.download(url, destination, quiet=False)


# if not os.path.exists('similarty.pkl'):
#     file_id = 'YOUR_FILE_ID'  # Replace YOUR_FILE_ID with the actual file ID
#     download_file_from_google_drive(file_id, 'similarty.pkl')


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarty[movie_index]
#     movies_list = sorted(list(enumerate(distances)),
#                          reverse=True, key=lambda x: x[1])[1:6]

#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies


# # Load the movies dictionary from the pickle file
# with open('movies_dict.pkl', 'rb') as file:
#     movies_dict = pickle.load(file)

# # Convert the dictionary to a pandas DataFrame
# movies = pd.DataFrame(movies_dict)

# # Load the similarity matrix
# with open('similarty.pkl', 'rb') as file:
#     similarty = pickle.load(file)

# # Streamlit application title
# st.title('MOVIE RECOMMENDER SYSTEM')

# # Selectbox for movie titles
# selected_movie_name = st.selectbox(
#     'How would you like to be connected?', movies['title'].values)

# if st.button('RECOMMEND'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)


# # https: // drive.google.com/file/d/1VgyGHGxbcEvaTYwYeQyFHYdam-w6KJy_/view?usp = drive_link
