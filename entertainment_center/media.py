import webbrowser

class Movie():

    """ This class provides a way to store movie related information

    Attributes:
        attr1 (str): This attribute represents the movie's title.
        attr2 (str): This attribute represents the movie's storyline.
        attr3 (str): This attribute represents the movie's poster image url
                     With this attribute is possible to show the movie poster.
        attr4 (str): This attribute represents the movie's youtube url
                     With this attribute is possible to show the movie trailer.
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
         webbrowser.open(self.trailer_youtube_url)
