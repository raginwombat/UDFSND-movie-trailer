import json
import urllib


class Movie():

    """Documentation for Movie class:
        Requires; Movie title, Movie Year and Youtube Trailer URL
        Modifies: Nothing
        Returns: Nothing
        Movie object takes movie title, year and trailer URL the rest of the 
        movie data is pulled from  OMBAPI and stored in appropriately title 
        vars.
    """

    def __init__(self, movie_title, year, movie_trailer_youtube_url):
        """Documentation for Custructor:
            Gets: Move TItle, movie Year and Youtube URL
            Sets: Title and Tariler URL variables
            Calls: pull_extra_nfo to load additional movie information"""

        self.title = movie_title
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.pull_extra_nfo(year)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def pull_extra_nfo(self, year):
        """Dcocumentation for Setter method:

            Requires:  Movie title
            Gets: Movie Year 
            Set: Year, Poster URL, Awards, Rating, Storyline"""
        url = url = "http://www.omdbapi.com/?t=" + self.title + "&y=" + year
        resposne = urllib.urlopen(url)
        json_data = json.loads(resposne.read())

        self.year = json_data["Year"]
        self.poster_image_url = json_data["Poster"]
        self.awards = json_data["Awards"]
        self.rated = json_data["Rated"]
        self.storyline = json_data["Plot"]