import json, urllib

class Movie():
    valid_ratings = ["G", "PG", "PG-13", "R"]
    
    """Documentation for Movie class"""
    def __init__(self, movie_title, year, movie_trailer_youtube_url):        
        self.title = movie_title
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.pull_extra_nfo(year)


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def pull_extra_nfo(self, year):
        url= url = "http://www.omdbapi.com/?t="+self.title+"&y="+year
        resposne = urllib.urlopen(url)
        json_data = json.loads(resposne.read())
        

        self.year = json_data["Year"]
        self.poster_image_url = json_data["Poster"]
        self.awards = json_data["Awards"]
        self.rated = json_data["Rated"]
        self.storyline = json_data["Plot"]
