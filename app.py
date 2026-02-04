import streamlit as st
import pickle
import pandas as pd

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# ------------------ LOAD DATA ------------------
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# ------------------ HELPERS ------------------
def find_movie_by_keyword(keyword):
    """Return the first movie title containing the keyword (case-insensitive)."""
    keyword = keyword.lower().strip()
    matches = movies[movies['title'].str.lower().str.contains(keyword)]
    if not matches.empty:
        return matches.iloc[0]['title']
    return None

def recommend(movie_name):
    """Return top 5 recommended movie names based on similarity."""
    closest_movie = find_movie_by_keyword(movie_name)
    if closest_movie is None:
        return None, []

    movie_index = movies[movies["title"] == closest_movie].index[0]
    distances = similarity[movie_index]

    # Get top 5 recommendations excluding the input movie itself
    similar_indices = sorted(range(len(distances)), key=lambda i: distances[i], reverse=True)
    similar_indices = [i for i in similar_indices if i != movie_index][:5]

    recommended_titles = [movies.iloc[i]["title"] for i in similar_indices]
    return closest_movie, recommended_titles

# ------------------ UI ------------------
st.title("🎬 Movie Recommendation System")
st.write("Content-based movie recommender (just names, keyword search)")

user_movie = st.text_input("Enter a movie name or keyword:")

if st.button("Recommend"):
    if not user_movie.strip():
        st.warning("Please enter a movie name.")
    else:
        matched_movie, recommendations = recommend(user_movie)
        if not matched_movie:
            st.error("No movies found with that keyword. Try another keyword.")
        else:
            st.success(f"Showing recommendations for: **{matched_movie}**")
            st.subheader("Recommended Movies:")
            for idx, title in enumerate(recommendations, start=1):
                st.write(f"{idx}. {title}")