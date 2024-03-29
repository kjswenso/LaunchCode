from flask import Flask
from werkzeug.serving import run_simple
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_titles = ["Tangled", "The Little Mermaid", "Mulan", "Hercules", "Finding Dory"]
    # TODO: randomly choose one of the movies, and return it
    rand_movie_idx = random.randrange(0, len(movie_titles));
    
    return movie_titles[rand_movie_idx]


app.run(host='0.0.0.0',port=12345)

