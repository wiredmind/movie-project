# Movie Trailer Website for Udacity Full Stack Web Developer Nanodegree course

This is a simple Python module that stores a list of movies, including box art imagery and a movie trailer URL, and generates an HTML file for viewing in a browser. The generated HTML file will open in your default browser, even if tht is [w3m](http://w3m.sourceforge.net/).

## Quickstart
To run this project you must have Python 2.7 installed on your system, preferably inside virtualenv as there are some third party libraries required to run this project. You don't want to pollute your golbal python environment. If you not familiar with virtualenv, have a look at [virtualenv documentation](https://virtualenv.pypa.io/en/latest/).

This project makes use of TMDb API, which requires authorization. You need to sign up for an account and generate an api_key for use with this application. This app reads the api key from environment variable TMDB_API_KEY, make sure this variable is set before you run this app: `export TMDB_API_KEY=your_api_key`.

1. Download or clone this repository to your computer
2. Install required dependency libraries: `pip install -r requirements.txt`
3. Run `python entertainment_center.py`

