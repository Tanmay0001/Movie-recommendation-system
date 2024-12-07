import pickle
import streamlit as st
import requests

# Function to fetch the movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies based on similarity
def recommend(movie):
    # Get index of the movie selected by the user
    index = movies[movies['title'] == movie].index[0]
    
    # Calculate similarities using the similarity matrix
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Prepare lists to store recommended movie names and posters
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:  # Skipping the first one as it's the selected movie itself
        # Get movie id
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    
    return recommended_movie_names, recommended_movie_posters

# Streamlit app header
st.header('Movie Recommender System')

# Load movie data and similarity matrix
movies = pickle.load(open('model/movie_list.pkl', 'rb'))  # Load movie data
similarity = pickle.load(open('model/similarity.pkl', 'rb'))  # Load similarity matrix

# Get the list of movie titles for dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Button to trigger recommendation
if st.button('Show Recommendation'):
    # Get recommendations for the selected movie
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
