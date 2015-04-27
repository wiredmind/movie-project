import os
import requests

# Loads environmental variables from a file,
# by default it will load all variables from '.env'
from env_tools import apply_env; apply_env()

# TMDb API configuration
API_VERSION = '3'
API_ROOT_URL = 'https://api.themoviedb.org/{version}'.format(version=API_VERSION)
API_KEY = os.environ['TMDB_API_KEY']

# To build image URL from TMDb three elements are required: base URL, size, and file path.
# Base URL and a list of sizes is returned from calling TMDb API /configuration method
# http://docs.themoviedb.apiary.io/#reference/configuration
url = API_ROOT_URL + '/configuration'
request = requests.get(url, params={'api_key': API_KEY})
IMAGE_BASE_URL = request.json()['images']['base_url']
IMAGE_BASE_URL += request.json()['images']['poster_sizes'][4]


class movie(object):
    """Movie object with three properties: a writable title, poster image URL,
    and trailer youtube id.

    Attributes:
        title: A string.
        poster_image_url: String, the URL for the movie's poster image
        trailer_youtube_id: String, youtube trailer video id, used to fetch trailer.

    To use:
        >>> the_matrix = movie(683)
        >>> the_matrix.title
        u'The Matrix'
        >>> the_matrix.poster_image_url
        u'https://image.tmdb.org/t/p/w780/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg'
        >>> the_matrix.trailer_youtube_id
        u'533ec655c3a368544800047b'
        >>> the_matrix.release_date
        u'1999-03-30'
        >>> the_matrix.tagline
        u'Welcome to the Real World.'
    """

    def __init__(self, id):
        # Request a movie from TMBb API, with extended attributes
        # http://docs.themoviedb.apiary.io/#reference/movies
        url = API_ROOT_URL + '/movie/{id}'.format(id=str(id))
        request = requests.get(url, params={'api_key': API_KEY,
            'append_to_response': 'videos'})
        movie = request.json()

        self.title = movie['title']
        self.poster_image_url = IMAGE_BASE_URL + movie['poster_path']
        self.trailer_youtube_id = movie['videos']['results'][0]['key']
        self.release_date = movie['release_date']
        self.tagline = movie['tagline']

