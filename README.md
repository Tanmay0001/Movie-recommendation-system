__Movie Recommender System__
This is a Content Based Movie Recommender System built using Python and Streamlit. It suggests similar movies based on the movie selected by the user.
Movie posters are dynamically fetched using the TMDB (The Movie Database) API.

**WORKING** :

1. Loading Pre trained Data
2. User Input Users can select a movie title from a dropdown list in the Streamlit interface.
3. Finding Similar Movies - When the "Show Recommendation" button is clicked:
The app finds the index of the selected movie.
It retrieves the top 5 most similar movies based on the cosine similarity(excluding the selected movie itself).

For each recommended movie, the app fetches:
The movie title
The movie poster (via TMDB API)

4. Fetching Posters from TMDB
The app sends a request to the TMDB API to get the movie poster path using the movie ID and constructs a full image URL for display.

5. Displaying Results
Recommended movies are displayed side-by-side in 5 columns using Streamlit’s layout. Each column shows:
The movie title
The movie poster
