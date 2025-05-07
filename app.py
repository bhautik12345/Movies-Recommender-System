import streamlit as st
import pickle
import pandas as pd


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_scores = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_titles = [movies.iloc[i[0]].title for i in movie_scores]
    return recommended_titles


st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.title("🎬 Movie Recommender System")
st.markdown("Select a movie and get similar movie recommendations!")


selected_movie_name = st.selectbox("Choose a movie you like:", movies['title'].values)


if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.markdown("### 🎥 Recommended Movies:")
    for i, title in enumerate(recommendations, start=1):
        st.markdown(f"{i}. **{title}**")
