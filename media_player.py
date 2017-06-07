import media
import fresh_tomatoes

<<<<<<< HEAD
amelie = media.Movie(
    "Amelie", "2001", "https://www.youtube.com/watch?v=sECzJY07oK4")
the_400_blows = media.Movie(
    "The 400 Blows", "1959", "https://www.youtube.com/watch?v=SYCD1IBzzC0")
zatoichi = media.Movie(
    "The Tale of ZatoIchi", "1962", "https://www.youtube.com/watch?v=RewZupIDQiM")
dev_D = media.Movie(
    "Dev D", "2009", "https://www.youtube.com/watch?v=FRLjycn11Rw")
let_the_right_one_in = media.Movie(
    "Let the Right One In", "2008", "https://www.youtube.com/watch?v=qrIcYgS8nRc")
magadheera = media.Movie(
    "Magadheera", "2009", "https://www.youtube.com/watch?v=SWYytrcTy6I")
# Dev D and Magadheera movie poster urls are bad, overriding them from api call
=======
amelie = media.Movie("Amelie", "2001", "https://www.youtube.com/watch?v=sECzJY07oK4")
the_400_blows = media.Movie("The 400 Blows", "1959", "https://www.youtube.com/watch?v=SYCD1IBzzC0")
zatoichi = media.Movie("The Tale of ZatoIchi", "1962", "https://www.youtube.com/watch?v=RewZupIDQiM")
dev_D = media.Movie("Dev D", "2009", "https://www.youtube.com/watch?v=FRLjycn11Rw")
let_the_right_one_in = media.Movie("Let the Right One In", "2008", "https://www.youtube.com/watch?v=qrIcYgS8nRc")
magadheera = media.Movie("Magadheera", "2009", "https://www.youtube.com/watch?v=SWYytrcTy6I")
#Dev D and Magadheera movie poster urls are bad, overriding them from api call
>>>>>>> origin/master
dev_D.poster_image_url = "http://www.impawards.com/intl/india/2009/posters/dev_d_ver5.jpg"
magadheera.poster_image_url = "https://sairamkunala.files.wordpress.com/2009/09/magadheera-poster-1.jpg"


<<<<<<< HEAD
movies = [amelie, the_400_blows, zatoichi,
          dev_D, let_the_right_one_in, magadheera]


'''Open the resulting movie title list '''
=======
movies = [amelie,the_400_blows, zatoichi, dev_D, let_the_right_one_in, magadheera]

print(amelie.storyline)

fresh_tomatoes.create_movie_tiles_content(movies)
>>>>>>> origin/master
fresh_tomatoes.open_movies_page(movies)
