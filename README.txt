 ----------------------------
|	Movie Trailer website    |
 ----------------------------

UDacity Project 1 submittion for R. Nelson

Overview
---------------
This project takes a list of movies and builds a movie website that gives basic information abut the movie and plays a trailer when the link is clicked.

Instructions
---------------
To Use Movie Trailer website:
	Click the movie poster to get a popup that plays the movies  trailer.

 To Generate New Movie Trailer Website:
 	Run the program run the media_player.py file.
	python media_player.py

Loading movies new movies:
	List movies in media_player.py
	title = media.Movie( title, year, trailer_url)

	move = [title_1, ..., title_N]


	Ex: amelie = media.Movie(
    "Amelie", "2001", "https://www.youtube.com/watch?v=sECzJY07oK4")
    
    ...

    movies = [amelie, the_400_blows, zatoichi,
          dev_D, let_the_right_one_in, magadheera]

Documenttaion
---------------

fresh_tomatoes.html - File template for fresh tomatoes
fresh_tomatoes.py  - Python source that drives the Python html. IT parses the media objects and serves it to the fresh tomatoes html file.
fresh_tomatoes.pyc
media_player.py - Python source that loads data into the media.py objects and ues fresh_tomatoes to generate html file.
media.py - Python source that defines the media object for the fresh tomatoes code
media.pyc
Project 1.zip
README.txt
