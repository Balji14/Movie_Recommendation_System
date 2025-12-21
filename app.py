import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# UI
st.title("🎬 Movie Recommendation System")
st.write("Content-based movie recommender using NLP")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    if recommendations:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.warning("Movie not found in database.")
