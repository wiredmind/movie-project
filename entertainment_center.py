from media import movie
from fresh_tomatoes import open_movies_page

# Build a list of movie objects
movies = [movie(id) for id in range(600, 609)]

# Generate a static HTML file to display all movie objects
open_movies_page(movies)
