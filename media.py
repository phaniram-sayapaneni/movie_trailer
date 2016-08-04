import webbrowser

class Movie():
    
    """ This contains movie title, story line, poster, youtube url."""
    
    def __init__(self, movie_title, movie_storyine, movie_poster, movie_youtube):
        self.title = movie_title
        self.storyline = movie_storyine
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_youtube

    def show_trailer(self):
        webbrowser.open(self.youtube_url)
    
        
      
    
