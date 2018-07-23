"""
In this I'm going to build a data structure in order to save movie informations
the data structure chosen in this case is a class.
"""
import webbrowser


class Movie:
    """
    This class defines a movie object with 4 attributes

    Attributes
    ----------
    movie_title: str
        the title of the movie
    movie_storyline: str
        the description of the movie
    poster_image: str
        the box art image of the movie
    trailer_youtube: str
        the movie trailer URL.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method open the movie trailer URL on the default browser"""
        webbrowser.open(self.trailer_youtube_url)
