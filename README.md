# 🎬 Movie Recommender System

This is a simple and intuitive movie recommender system built using **Python**, **pandas**, and **Streamlit**. It suggests movies similar to the one selected by the user based on content similarity (e.g., genre, description, keywords).

## 🚀 Features

- Recommends 5 similar movies based on the selected title
- Fast and lightweight recommendation using precomputed similarity matrix
- Interactive and user-friendly Streamlit interface


## 🔧 How It Works

- Movie data is loaded from a pickle file (`movie_dict.pkl`)
- A similarity matrix (cosine similarity or NLP-based) is loaded from `similarity.pkl`
- When a movie is selected, the system fetches the top 5 most similar titles

## ▶️ Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```
2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```


