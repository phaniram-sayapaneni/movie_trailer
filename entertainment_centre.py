#This file enables us to diplay a set of
#image posters along with their trailers when clicked on them.

# It is essestial to import the ready made modules such as fresh tomatoes,
#which has all the functionalities to display the information in a browser.

import fresh_tomatoes
import media

# media is a class contructed just
#for storing all movie attributes in to objects 



toy_story = media.Movie("Toy Story",
                        "the story of toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",# noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# This object toy_story is all about the toy_story movie and it's elements


avatar = media.Movie("Avatar",
                     "James cameron is just awesome" ,
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # noqa
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
# This object avatar is all about the avatar movie and it's elements

jim_carrey = media.Movie("Dumb and Dumber",
                         "Jim carrey is just awesome" ,
                         "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg", # noqa
                         "https://www.youtube.com/watch?v=l13yPhimE3o")
# This object jim_carrey is all about the jim_carrey movie and it's elements

matrix1 =  media.Movie("The Matrix",
                       "Matrix is ultimate",
                       "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", # noqa
                       "https://www.youtube.com/watch?v=m8e-FF8MsqU")
# This object matrix1 is all about the matrix movie(part 1) and it's elements

matrix2= media.Movie("The Matrix Reloaded",
                     "Again Matrix is ultimate",
                     "https://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",  # noqa
                     "https://www.youtube.com/watch?v=kYzz0FSgpSU")
# This object matrix2 is all about the matrix reloaded (-part2: mounica belluci)movie and it's elements

matrix3= media.Movie("The Matrix Revolutions",
                     "Matrix is the revolution",
                     "https://upload.wikimedia.org/wikipedia/en/3/34/Matrix_revolutions_ver7.jpg",
                     "https://www.youtube.com/watch?v=hMbexEPAOQI")
# This object matrix 3 is all about the matrix revolutions movie(-part3:) and it's elements



movies= [toy_story, avatar, jim_carrey, matrix1, matrix2, matrix3]
# This creates an array of objects of all
#the movies to be displayed on to the web site

fresh_tomatoes.open_movies_page(movies)
#this just one lines performs all the work of displaying
#movie information on to the website, all that
#you are doing is just send an array to the func.
